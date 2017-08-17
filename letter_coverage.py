"""
word_coverage.py

Compute the minimum number of words from five-letter-words
needed to cover N letters from the alphabet.

This can be done in O(N^2) time with a dynamic program.
For each word that we choose, we have to look at all other words
to see how many letters those two cover, combined. 

https://charlesreid1.com/wiki/Five_Letter_Words
https://charlesreid1.com/wiki/Letter_Coverage
"""
from get_words import get_words
import numpy as np
from pprint import pprint


def word2bitvector(word,N):
    """
    Turns a five-letter word into a bit vector representing character coverage.
    Uses 26 letters by default.
    """
    bit_vector = [False,]*N
    for c in word:
        i = ord(c)-ord('a')
        try:
            bit_vector[i] = True
        except IndexError:
            pass
    return np.array(bit_vector)



if __name__=="__main__":

    # Searching for words covering first N letters
    N = 13

    words = get_words()
    words = words[:1000]



    # Initialization:
    # ----------------

    # Store best coverage bitvectors for each word
    bestcoverage_bv = [[False]*N for k in range(len(words))]

    # Store number of 1s for best coverage vector for each word
    ones_bv = [0]*len(words)

    # Store number of words in best solution for each word
    ws = [0]*len(words)

    # Store prior word for backtracking
    bt = [-1]*len(words)



    # Fencepost: Initial Step
    # Word 0
    # ----------------

    # Start with word 0
    wi = words[0]

    # Best letter coverage bit vector
    bestcoverage_bv[0] = word2bitvector(words[0],N)

    # Length of 1s
    ones_bv[0] = sum(bestcoverage_bv[0])

    # Number of words in best solution:
    ws[0] = 1

    # Backtracking: first word has no prior word
    bt[0] = 0

    for i in range(1,len(words)):
        wi = words[i]

        # Start with bitvector of word i's coverage
        wi_bv = word2bitvector(wi,N)

        # Fencepost: Initial Step 
        # Word i-1 
        # Assume this is the solution,
        # and if we find a better one later,
        # we can overwrite it.
        # ------------------------

        # word i-1
        wj = words[i-1]

        # Get the best coverage bitvector for i-1
        wj_bv = bestcoverage_bv[i-1]

        # Get combined bitvector for word i and best coverage bitvector for word j
        bestcoverage_bv[i] = np.logical_or(wi_bv,wj_bv)

        # Count ones in new combined bitvector
        ones_bv[i] = sum(bestcoverage_bv[i])

        # Number of words in new best solution:
        ws[i] = ws[i-1]+1

        # Backtracking
        bt[i] = i-1

        # Now loop over the rest of the words,
        # and look for a better solution.
        for j in reversed(range(1,i)):

            # Get the prior word
            wj = words[j]

            # Get best coverage bitvector 
            wj_bv = bestcoverage_bv[j]

            # (potential) new combined coverage vector
            bestcoverage_bv_i = np.logical_or(wi_bv, wj_bv)

            # Number of ones in (potential) new combined coverage vector
            ones_bv_i = sum(bestcoverage_bv_i)

            # Number of words in (potential) new best solution
            ws_i = ws[j]+1

            # If this solution is better than our current one,
            # overwrite the current solution.
            # (Better means, more ones or fewer words.)

            if(ones_bv_i > ones_bv[i]):
                bestcoverage_bv[i] = bestcoverage_bv_i
                ones_bv[i] = ones_bv_i
                ws[i] = ws_i
                bt[i] = j

            # It's tempting to stop early,
            # but what if we find the perfect 
            # solution right at the end?!?



    # Okay, now actually get the solution.
    # The solution is the maximum of ones_bv and the minimum of ws
    # 
    # Start by finding the maximum(s) of ones_bv
    # Then check each corresponding index of ws
    ones_bv_indices = [k for k,v in enumerate(ones_bv) if v==max(ones_bv)]

    min_key = ones_bv_indices[0]
    min_val = ones_bv[ones_bv_indices[0]]
    for ix in reversed(ones_bv_indices[1:]):
        if(ones_bv[ix] < min_key):
            min_key = ix
            min_val = ones_bv[ix]

    print("Min key:")
    print(min_key)
    print("Min val:")
    print(min_val)



