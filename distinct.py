"""
distinct.py

Number of words that contain exactly k distinct letters,
1 <= k <= 5


Donald Knuth
Art of Computer Programming 
Volume 4 Facsimile 0
Exercise #27

How many SGB words contain exactly k distinct letters, for 1 <= k <= 5?
"""

def get_words():
    # Load the file.
    with open('sgb-words.txt','r') as f:
        ## This includes \n at the end of each line:
        #words = f.readlines()
    
        # This drops the \n at the end of each line:
        words = f.read().splitlines()

    return words

if __name__=="__main__":
    words = get_words()

    lengths = [[] for i in range(5+1)]

    for i in range(1,5+1):
        for word in words:
            if(len(set(word))==i):
                lengths[i].append(word)
    
    for i in range(1,5+1):
        print("Number of words with {0:d} letters: {1:d}".format(i, len(lengths[i])))
