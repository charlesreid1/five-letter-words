"""
diff_by_one.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Exercise #28

Find pairs of SGB word vectors that differ by +/-1 in each component.
"""
from get_words import get_words


def gen_variations(word,fragment,depth,variations):
    """
    Recursive backtracking method to assemble strings
    differing by +/-1 at each position
    """
    if depth==5:
        variations.add(fragment)
    else:
        # make a choice
        fragment_p1 = fragment + chr(ord(word[depth])+1)
        fragment_m1 = fragment + chr(ord(word[depth])-1)
        for new_fragment in [fragment_p1,fragment_m1]:
            gen_variations(word,new_fragment,depth+1,variations)


def get_all_variations(word):
    """
    Return all possible words that differ
    from `word` by +/-1 in each index.
    This does not include `word` in the 
    variations.
    """
    word_variations = set()
    gen_variations(word,'',0,word_variations)

    word_variations = list(word_variations)
    return word_variations


def main():
    """
    Find pairs of SGB word vectors that differ by +/-1 in each component.
    
    To do this, iterate through each word,
    generate the 32 possible candidate matchings,
    and if they exist, add the pair to a set.
    """
    # words is a hash table (unsorted)
    words = get_words()
    #words = words[:1000]
    words = set(get_words())

    # List of string tuples
    off_by_one = set()

    # Iterate over every word
    for iw,word in enumerate(words):
        # Generate all 2^5 = 32 possible candidate
        # matches for this word (total 185k strings)
        all_vars = get_all_variations(word)
        for word_var in all_vars:
            # O(1) check if this variation exists
            # in the five letter words set
            if word_var in words:
                # Found a new (unordered) pair
                if word<word_var:
                    left=word
                    right=word_var
                else:
                    left=word_var
                    right=word
                off_by_one.add((left,right))
    
    off_by_one = list(off_by_one)
    off_by_one.sort()

    for o in off_by_one:
        print("{:s} {:s}".format(o[0],o[1]))

    print("Found {0:d} pairs of words that differ by +/-1 in each component.".format(len(off_by_one)))

if __name__=="__main__":
    main()
