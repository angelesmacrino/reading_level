import sys, os   
from readinglevel import ReadingLevel
import pypandoc
from pypandoc.pandoc_download import download_pandoc


#Usage: write on the console "python main.py FILENAME" FILENAME being the text archive one wishes to analize.
def main():
    filename = sys.argv[1]
    
    #If the user does not write the command correctly
    if len(sys.argv) != 2:
        sys.exit("Usage: python main.py FILENAME")
    

    if os.path.exists(filename):
        try:
            
            handler = open(filename, 'r')
            lector = ReadingLevel(handler.read())
            handler.close()
            index = lector.obtain_index()
            print(f'Reading level: {index}')
        except Exception as e:
            print(e)
            sys.exit("An error occured, please try again")

if __name__ == "__main__":
    main()
    
