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


def printbv(bv):
    """
    Pretty printing for boolean bit vector
    """
    result = ""
    for bit in bv:
        if bit:
            result += "1"
        else:
            result += "0"
    return result


def btsolution(min_key, min_val, words, bt):
    """
    Reconstruct the sequence of words that gives maximum coverage and minimum word count.

    Input: minimum word key (last word), minimum value (number of words), backtrack (prior word)

    Output: list of words
    """
    solution = []
    solution.append(words[min_key])
    prior_key = bt[min_key]
    while prior_key != -1:
        solution.append(words[prior_key])
        prior_key = bt[prior_key]
    return reversed(solution)




def get_dummy_words():
    return ["aa","ab","bc","aa","dd","de","bb"]



if __name__=="__main__":

    # Searching for words covering first N letters
    N = 15 

    words = get_words()
    words = words[:1000]


    # Initialization:
    # ----------------

    # Store best coverage bitvectors for each word
    bestcoverage_bv = [np.array([False]*N) for k in range(len(words))]

    # Store number of 1s for best coverage vector for each word
    ones_bv = [-1]*len(words)

    # Store number of words in best solution for each word
    ws = [0]*len(words)

    # Store prior word for backtracking
    bt = [-1]*len(words)



    # Fencepost: Initial Step
    # Word 0
    # ----------------

    i = 0

    # Start with word 0
    wi = words[i]

    # Best letter coverage bit vector
    bestcoverage_bv[i] = word2bitvector(words[i],N)

    # Length of 1s
    ones_bv[i] = sum(bestcoverage_bv[i])

    # Number of words in best solution:
    ws[i] = 1

    # Backtracking: first word has no prior word
    bt[i] = -1

    # -----------------------------------------------------------------
    print("-"*20)
    print("Analyzing word "+str(i)+" "+words[i])

    print("----")
    print("Prior word: there is none")
    print("Best coverage bit vector at index 0: "+printbv(bestcoverage_bv[i]))
    print("Best coverage bit vector sum: "+str(ones_bv[i]))
    print("(This needs to > beat: nobody. there is none.")
    # -----------------------------------------------------------------

    #import pdb; pdb.set_trace();

    # Start by assuming the word by itself, 
    # and then examine each possible pairing
    for i in range(1,len(words)):
        wi = words[i]

        # Start with bitvector of word i's coverage
        wi_bv = word2bitvector(wi,N)

        # Fencepost: initial step
        # Word i by itself
        # Assume word i is the first word in the solution,
        # and if we find a better combination with prior word,
        # overwrite this solution.
        # ------------------------

        # Best coverage so far (first guess) is word i by itself
        bestcoverage_bv[i] = wi_bv

        # Count ones in (first guess) best bitvector
        ones_bv[i] = sum(bestcoverage_bv[i])

        # Number of words in new best solution:
        ws[i] = 1

        # Backtracking
        bt[i] = -1

        # Boolean: is this the first word in the sequence of solutions?
        first = True

        # -----------------------------------------------------------------
        print("-"*20)
        print("For word "+str(i)+" "+words[i])
        print("Bitvector coverage at index "+str(i)+" is: "+printbv(bestcoverage_bv[i]))
        print("about to loop over remaining words...")
        print("----")
        print("Prior word: there is none")
        print("Best coverage bit vector for first guess solution: "+printbv(bestcoverage_bv[i]))
        print("Best coverage bit vector sum for first guess solution: "+str(ones_bv[i]))
        print("Number of words in first guess solution: "+str(ws[i]))
        print("(first guess solution is now current solution)")
        # -----------------------------------------------------------------

        #import pdb; pdb.set_trace();

        # Now loop over the rest of the words,
        # and look for a better solution.
        for j in reversed(range(0,i)):

            ##########################
            # Note: we need to consider the word j
            # by itself, as the first word of our solution.
            # 
            # A bit lost here.
            # Something's not quite right.
            # While some of the intermediate calcs are ok,
            # we are *never* finding better solutions...???
            ##########################

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

            # -----------------------------------------------------------------
            print("----")
            print("Prior word: "+wj)
            print("Best coverage bit vector at index "+str(i))
            pprint(bestcoverage_bv_i)
            print("")
            print("Best coverage bit vector for this solution: "+printbv(bestcoverage_bv_i))
            print("Best coverage bit vector sum for this solution: "+str(ones_bv_i))
            print("Number of words in this solution: "+str(ws_i))
            print("")
            print("Best coverage bit vector for current solution: "+printbv(bestcoverage_bv[i]))
            print("Best coverage bit vector sum for current solution: "+str(ones_bv[i]))
            print("Number of words in current solution: "+str(ws[i]))
            print("")
            print( "Better ones? " + str(ones_bv_i > ones_bv[i]) )
            print( "Same ones but better words? " + str((ones_bv_i==ones_bv[i]) and ws_i < ws[i]) )
            if( (ones_bv_i > ones_bv[i]) or (ones_bv_i==ones_bv[i] and ws_i < ws[i]) ):
                print("Replacing current solution with this solution.")
            else:
                print("Keeping current solution and tossing out this solution.")
            # -----------------------------------------------------------------

            # If this solution is better than our current one,
            # overwrite the current solution.
            # (Better means, "more ones", or "same ones and fewer words".)

            #import pdb; pdb.set_trace();

            if( (ones_bv_i > ones_bv[i]) or (ones_bv_i==ones_bv[i] and ws_i < ws[i]) ):
                bestcoverage_bv[i] = bestcoverage_bv_i
                ones_bv[i] = ones_bv_i
                ws[i] = ws_i
                bt[i] = j

                # This word now follows another word in the sequence of solutions
                first = False

            # It's tempting to stop early,
            # but what if we find the perfect 
            # solution right at the end?!?

        # -----------------------------------------------------------------
        print("----")
        print("Final:")
        pprint(bestcoverage_bv[i])
        print("-"*20)
        # -----------------------------------------------------------------



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

    solution = list(btsolution(min_key, min_val, words, bt))
    print("Takes "+str(len(solution))+" words to cover "+str(N)+" letters")
    pprint(solution)

