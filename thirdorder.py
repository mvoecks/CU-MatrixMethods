#This file generates random text based off a inputed text using a third order markov chain model

import random
import sys
#define the lastWord varibale to be an array of the last three variables in the text.
lastWord = ('', '', '')
ptm = {}
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            if word != '':
                #again populate the lastword variable with the first three words in the text
                if lastWord[0] == '':
                    lastWord = (word, '', '')
                elif lastWord[1] == '':
                    lastWord = (lastWord[0], word, '')
                elif lastWord[2] == '':
                    lastWord = (lastWord[0], lastWord[1], word)
                else:
                    if not(lastWord in ptm):
                        ptm[lastWord] = [word]
                    else:
                        ptm[lastWord].append(word)
                    #again, the 2 most recent words are shifted down one position and the new word is added to the lastWord variable
                    lastWord = (lastWord[1], lastWord[2], word)

#Randomly generated words are still calculated the same
start = random.choice(list(ptm))
for i in range(1, int(sys.argv[1])):
    word = random.choice(ptm[start])
    start = (start[1], start[2], word)
    sys.stdout.write(word+' ')
    sys.stdout.flush()
print()
