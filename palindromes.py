"""
palindromes.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #29

Find all SGB words that are palindromes (kayak)
or that are palindrome pairs (regal lager)
"""
from get_words import get_words
from pprint import pprint

def is_palindrome(word):
    test1 = word[0]==word[4] 
    test2 = word[1]==word[3]
    if(test1 and test2):
        return True
    return False

def is_palindrome_pair(word1,word2):
    test0 = word1[0]==word2[4]
    test1 = word1[1]==word2[3]
    test2 = word1[2]==word2[2]
    test3 = word1[3]==word2[1]
    test4 = word1[4]==word2[0]
    if(test0 and test1 and test2 and test3 and test4):
        return True
    return False

if __name__=="__main__":
    words = get_words()

    kp = 0
    palindromes = []

    kpp = 0
    palindrome_pairs = []

    # Check for palindromes
    for i in range(len(words)):
        if(is_palindrome(words[i])):
            kp += 1
            palindromes.append(words[i])

    print("-"*40)
    print("Palindromes: \n")
    print(", ".join(palindromes))
    print("There are {0:d} palindromes.".format(kp))

    # Check for palindrome pairs
    for i in range(len(words)):
        for j in range(i,len(words)):
            if(is_palindrome_pair(words[i],words[j])):
                # Palindromes shouldn't count as palindrome pairs
                if(words[i] is not words[j]):
                    kpp += 1
                    palindrome_pairs.append((words[i],words[j]))

    print("-"*40)
    print("Palindrome Pairs: \n")
    for pair in palindrome_pairs:
        print(", ".join(pair))
    print("There are {0:d} palindrome pairs.".format(kpp))
