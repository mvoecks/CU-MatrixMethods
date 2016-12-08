#This file generates random text based off a inputed text using a first order markov chain model

#import necessary libraries
import random
import sys

#define the probability transition matrix hashtable and the lastword variable
lastWord = ''
ptm = {}

#This section populates the probability transition matrix by scanning every word of the document and updates
#the entries of the corrisponding words in the hashtable so that its rows are all the words in the document 
#and their columns consist of all the words that follow that specific word

#these lines get the next word from the text
with open('sample.txt', 'r') as f:
    for line in f:
        for word in line.split():
            
            #the word is first converted to lowercase and checked to see if it is actually a word
            word = word.lower()
            if word != '':

                #this first if will only return true once at the very start of the algorithm, and just sets the first word of the document to the variable lastWord
                if lastWord == '':
                    lastWord = word

                #For every subsequent word in the document the following code runs
                else:
                    #if the previous word is not in the probability transition hashtable then add it and make its only entry the word we are processing
                    if not(lastWord in ptm):
                        ptm[lastWord] = [word]
                    #if the previous word exists in the probability transition hashtable then update its columns to include the word we are currently processing
                    else:
                        ptm[lastWord].append(word)
                    #set the variable lastWord to the word currently being processed so the next loop associates the correct words
                    lastWord = word

#This section of the code generates the text by picking a random starting word, and then based of that random
#starting word it picks the next word randomly from the previous words probabiliy transition hashtable

#pick a random word from the hashtable
start = random.choice(list(ptm))

#loop until the user specified number of words have been randomly generated
for i in range(1, int(sys.argv[1])):
    #choose a random word to be printed next based of the previous word
    word = random.choice(ptm[start])
    #reset the previous word to be the current word that was just picked
    start = word
    #print out the word set that was set aside for printing
    sys.stdout.write(word+' ')
    sys.stdout.flush()
print()
