"""
reverse_lexico.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Variation on Exercise #30

Each letter of the word "spied" appears in reversed lexicographic order.
Find more words whose letters appear in reverse lexicographic order.
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

    count = 0
    print("-"*40)
    print("ALL lexicographically reversed words:")
    for word in words:
        if(in_reverse_sorted_order(word)):
            print(word)
            count += 1
    print("{0:d} total.".format(count))

    print("-"*40)
    for word in words:
        if(in_reverse_sorted_order(word)):
            print("First reverse lexicographically sorted word:")
            print(word)
            break

    words.reverse()

    print("-"*40)
    for word in words:
        if(in_reverse_sorted_order(word)):
            print("Last lexicographically sorted word:")
            print(word)
            break
