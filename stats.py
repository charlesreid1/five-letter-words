from pprint import pprint 

"""
stats.py 

Compute statistics of the 5-letter word collection from the Stanford GraphBase.
"""

# Store frequencies of letters and bigrams
letters = {}
bigrams = {}



# Load the file.
with open('sgb-words.txt','r') as f:
    ## This includes \n at the end of each line:
    #words = f.readlines()

    # This drops the \n at the end of each line:
    words = f.read().splitlines()



# Loop through each letter of each word
for word in words:
    for c in word:
        if c in letters.keys():
            letters[c] += 1
        else:
            letters[c] = 1

    for i in range(len(word)-1):
        bigram = str(word[i]+word[i+1])
        if bigram in bigrams.keys():
            bigrams[bigram] += 1
        else:
            bigrams[bigram] = 1

# To print out the dict in sorted order,
# convert to a list of tuples.
# This creates a list of (key,value) tuples, 
# and sorts them by value (itemgettr(1))
import operator
sorted_letters = sorted(letters.items(), key=operator.itemgetter(1))
sorted_bigrams = sorted(bigrams.items(), key=operator.itemgetter(1))

print("-"*20)
print("\n\n")
pprint(sorted_letters)

print("-"*20)
print("\n\n")
pprint(sorted_bigrams)

print("-"*20)
print("\n\n")
pprint(bigrams['ch'])
pprint(bigrams['ar'])
pprint(bigrams['le'])
pprint(bigrams['es'])

