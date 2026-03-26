"""
reverse_lexico.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Variation on Exercise #30

Each letter of the word "spied" appears in reversed lexicographic order.
Find more words whose letters appear in reverse lexicographic order.
"""
from get_words import get_words

def in_reverse_sorted_order(word):
    return all(a >= b for a, b in zip(word, word[1:]))

if __name__=="__main__":

    words = get_words()

    words = sorted(words)

    sorted_words = [w for w in words if in_reverse_sorted_order(w)]

    print("-"*40)
    print("ALL lexicographically reversed words:")
    for word in sorted_words:
        print(word)
    print("{0:d} total.".format(len(sorted_words)))

    print("-"*40)
    print("First reverse lexicographically sorted word:")
    print(sorted_words[0])

    print("-"*40)
    print("Last reverse lexicographically sorted word:")
    print(sorted_words[-1])
