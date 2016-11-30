import random
import sys
lastWord1 = ''
lastWord2 = ''
lastWord3 = ''
lastWord4 = ''
ptm = {}
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = ''.join(e for e in word if e.isalnum())
            word = word.lower()
            if word != '':
                if lastWord4 == '':
                    lastWord4 = word
                elif lastWord3 == '':
                    lastWord3 = word
                elif lastWord2 == '':
                    lastWord2 = word
                elif lastWord1 == '':
                    lastWord1 = word
                else:
                    enterWord = str(lastWord4)+str(lastWord3)+str(lastWord2)+str(lastWord1)
                    if not(enterWord in ptm):
                        ptm[enterWord] = [word]
                    else:
                        ptm[enterWord].append(word)
                    lastWord4 = lastWord3
                    lastWord3 = lastWord2
                    lastWord2 = lastWord1
                    lastWord1 = word
                    
for i in range(1, 2500):
    sys.stdout.write(str(random.choice(ptm[random.choice(list(ptm))]))+' ')
    sys.stdout.flush()
