"""
diff_by_one.py

Donald Knuth
Art of Computer Programming 
Volume 4 Facsimile 0
Exercise #28

Find pairs of SGB word vectors that differ by +/-1.
"""
from get_words import get_words
from euclidean_distance import euclidean_distance

if __name__=="__main__":
    words = get_words()

    ## To limit the output:
    #words = words[:1000]

    k = 0
    off_by_one = []
    for i in range(len(words)):
        for j in range(i,len(words)):
            d = euclidean_distance(words[i],words[j])
            if(abs(d)==1):
                k += 1
                off_by_one.append((words[i],words[j]))
                print("{0:s}, {1:s}".format(words[i],words[j]))

    print("{0:d} words have a Euclidean distance of +/-1.".format(k))
