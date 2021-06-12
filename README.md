Inspired by a cs50's problem: https://cs50.harvard.edu/college/2021/spring/psets/2/readability/

This script estimates the required grade needed to comprehend a given text. It uses the Coleman-Liau index: I = 0.588L - 0.296S - 15.8 where L is is the average number of letters per 100 words and S is the average number of sentences per 100 words.

Requirements:

The last version of Phyton installed.
Instructions:

Place both .py and the text files in the same folder, open cmd and with cd navigate to the folder and run the script with: python main.py FILENAME.

For the moment it only reads plain text in .txt format
