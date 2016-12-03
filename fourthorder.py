import random
import sys
lastWord = ('', '', '', '')
ptm = {}
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            if word != '':
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
                    lastWord = (lastWord[1], lastWord[2], lastWord[3], word)

start = random.choice(list(ptm))
for i in range(1, int(sys.argv[1])):
    word = random.choice(ptm[start])
    start = (start[1], start[2], start[3], word)
    sys.stdout.write(word+' ')
    sys.stdout.flush()
print()