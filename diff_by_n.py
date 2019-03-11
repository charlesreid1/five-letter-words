"""
diff_by_n.py

Donald Knuth, Art of Computer Programming, Volume 4 Facsimile 0
Variation on Exercise #28

Find pairs of SGB word vectors that differ by +/-n.
"""
from get_words import get_words
import timeit

def gen_variations(word,fragment,distance,depth,variations):
    """
    Recursive backtracking method to assemble strings
    differing by +/-distance at each position
    """
    if depth==5:
        variations.add(fragment)
    else:
        for d in range(1,distance+1):
            fragment_pd = fragment + chr(ord(word[depth])+d)
            fragment_md = fragment + chr(ord(word[depth])-d)
            for new_fragment in [fragment_pd,fragment_md]:
                gen_variations(word,new_fragment,distance,depth+1,variations)


def get_all_variations(word,d):
    """
    Return all possible words that differ
    from `word` by +/-d in each index.
    This does not include `word` in the 
    variations.
    """
    word_variations = set()
    gen_variations(word,'',d,0,word_variations)

    word_variations = list(word_variations)
    return word_variations


def main():
    """
    Find pairs of SGB word vectors that differ by 
    +/-d in each component.
    
    To do this, iterate through each word,
    generate the possible candidate matchings,
    and if they exist, add the pair to a set.
    """
    words = get_words()
    #words = words[:1000]
    words = set(get_words())

    for d in [1,2,3]:

        tic = timeit.default_timer()

        # List of string tuples
        off_by_n = set()

        # Iterate over every word
        for iw,word in enumerate(words):
            # Generate all possible candidate matches
            # distance +/-d from this word at each
            # position
            all_vars = get_all_variations(word,d)
            for word_var in all_vars:
                if word_var in words:
                    # Found a new (unordered) pair
                    if word<word_var:
                        left=word
                        right=word_var
                    else:
                        left=word_var
                        right=word
                    off_by_n.add((left,right))
        
        off_by_n = list(off_by_n)
        off_by_n.sort()

        toc = timeit.default_timer()

        for o in off_by_n[:10]:
            print("{:s} {:s}".format(o[0],o[1]))

        print("Found {0:d} pairs of words that differ by +/-{1:d} in each component.".format(len(off_by_n),d))
        print("Time: %0.4f"%(toc-tic))

if __name__=="__main__":
    main()

