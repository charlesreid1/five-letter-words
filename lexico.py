"""
lexico.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #30

Each letter of the word "first" appears in correct lexicographic order.
Find the first and last such words in the SGB words.
"""
from get_words import get_words

def in_sorted_order(word):
    return all(a <= b for a, b in zip(word, word[1:]))

if __name__=="__main__":

    words = sorted(get_words())

    sorted_words = [w for w in words if in_sorted_order(w)]

    print("-"*40)
    print("ALL lexicographically sorted words:")
    for word in sorted_words:
        print(word)
    print("{0:d} total.".format(len(sorted_words)))

    print("-"*40)
    print("First lexicographically sorted word:")
    print(sorted_words[0])

    print("-"*40)
    print("Last lexicographically sorted word:")
    print(sorted_words[-1])
