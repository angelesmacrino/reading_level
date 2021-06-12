class ReadingLevel:

    sentences = 0
    words = 0
    letters = 0

    def __init__ (self, text):
        self.text = text

    def _extractor(self): #Count the number of letters, words and sentences.
        self.sentences = 0
        self.words = 0
        self.letters = 0    
    
        for i in self.text:
            if i >= 'A' and i <= 'z':
                self.letters += 1
            elif i == ' ':
                self.words += 1
            elif i in '?!.':
                self.sentences += 1
        self.words += 1

    def obtain_index(self):
        self._extractor()
        L = 100 * self.letters / self.words
        S = 100 * self.sentences / self.words
        index = 0.0588 * L - 0.296 * S - 15.8 #Coleman-Liau index, determining what grade level is needed to comprehend the text.
        if index <= 0:
            index = 1
        return round(index)