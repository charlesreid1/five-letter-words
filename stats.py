"""
stats.py 

Compute statistics of the 5-letter word collection from the Stanford GraphBase.
"""
from pprint import pprint 
from get_words import get_words

if __name__=="__main__":

    # Store frequencies of letters and bigrams
    letters = {}
    bigrams = {}
    
    words = get_words()    
    
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
    
    print("\n\n")
    pprint(sorted_letters)
    
    print("\n\n")
    pprint(sorted_bigrams)
    
