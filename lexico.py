"""
lexico.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #30

Each letter of the word "first" appears in correct lexicographic order.
Find the first and last such words in the SGB words.
"""
from get_words import get_words

def in_sorted_order(word):
    chars = list(word)
    if(str(chars)==str(sorted(chars))):
        return True
    else:
        return False

if __name__=="__main__":

    words = get_words()

    words = sorted(words)


    count = 0
    print("-"*40)
    print("ALL lexicographically sorted words:")
    for word in words:
        if(in_sorted_order(word)):
            print(word)
            count += 1
    print("{0:d} total.".format(count))

    print("-"*40)
    for word in words:
        if(in_sorted_order(word)):
            print("First lexicographically sorted word:")
            print(word)
            break

    words.reverse()

    print("-"*40)
    for word in words:
        if(in_sorted_order(word)):
            print("Last lexicographically sorted word:")
            print(word)
            break
