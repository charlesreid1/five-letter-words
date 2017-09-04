"""
reverse_lexico.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #30

Each letter of the word "first" appears in correct lexicographic order.
Find the first and last such words in the SGB words.
"""
from get_words import get_words

def in_reverse_sorted_order(word):
    chars = list(word)
    # Note: reversed returns a generator, 
    # so we have to pass it to list() 
    # to explicitly enumerate the reversed results.
    if(str(chars)==str(list(reversed(sorted(chars))))):
        return True
    else:
        return False

if __name__=="__main__":

    words = get_words()

    words = sorted(words)

    for word in words:
        if(in_reverse_sorted_order(word)):
            print("First reverse lexicographically sorted word:")
            print(word)
            break

    words.reverse()

    for word in words:
        if(in_reverse_sorted_order(word)):
            print("Last lexicographically sorted word:")
            print(word)
            break
