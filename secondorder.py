#This file generates random text based off a inputed text using a second order markov chain model

import random
import sys
#Define the last word to be an array of two words to represent the last two word in the text
lastWord = ('', '')
ptm = {}
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            if word != '':
                #the first if and elif sets the lastWord variable to be the first two words of the text
                if lastWord[0] == '':
                    lastWord = (word, '')
                elif lastWord[1] == '':
                    lastWord = (lastWord[0], word)
                else:
                    if not(lastWord in ptm):
                        ptm[lastWord] = [word]
                    else:
                        ptm[lastWord].append(word)
                    #The lastword variable still includes the most recent word and the currennt word, 
                    #however the most recent word is shifted one position down.
                    lastWord = (lastWord[1], word)

#The words are chosen in the same manner that they were in the first order example
start = random.choice(list(ptm))
for i in range(1, int(sys.argv[1])):
    word = random.choice(ptm[start])
    start = (start[1], word)
    sys.stdout.write(word+' ')
    sys.stdout.flush()
print()
