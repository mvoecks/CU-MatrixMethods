#This file generates random text based off a inputed text using a fourth order markov chain model

import random
import sys
#Define the lastWord variable to contain an array of the 4 most recent words
lastWord = ('', '', '', '')
ptm = {}
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            if word != '':
                #populate the lastWord variable to contain the first four words to start
                if lastWord[0] == '':
                    lastWord = (word, '', '', '')
                elif lastWord[1] == '':
                    lastWord = (lastWord[0], word, '', '')
                elif lastWord[2] == '':
                    lastWord = (lastWord[0], lastWord[1], word, '')
                elif lastWord[3] == '':
                    lastWord = (lastWord[0], lastWord[1], lastWord[2], word)
                else:
                    if not(lastWord in ptm):
                        ptm[lastWord] = [word]
                    else:
                        ptm[lastWord].append(word)
                    #Shift the position of the 3 most recent words and add the word currently being processed
                    lastWord = (lastWord[1], lastWord[2], lastWord[3], word)

#Text is generated the same way it has in the previous algorithms
start = random.choice(list(ptm))
for i in range(1, int(sys.argv[1])):
    word = random.choice(ptm[start])
    start = (start[1], start[2], start[3], word)
    sys.stdout.write(word+' ')
    sys.stdout.flush()
print()
