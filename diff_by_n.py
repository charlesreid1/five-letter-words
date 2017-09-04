"""
diff_by_n.py

Donald Knuth
Art of Computer Programming 
Volume 4 Facsimile 0
Variation on Exercise #28

Find pairs of SGB word vectors that differ by +/-n.
"""
from get_words import get_words
from euclidean_distance import euclidean_distance

def diff_by_n(n):
    k = 0
    off_by_one = []
    for i in range(len(words)):
        for j in range(i,len(words)):
            d = euclidean_distance(words[i],words[j])
            if(abs(d)==n):
                k += 1
                off_by_one.append((words[i],words[j]))
                print("{0:s}, {1:s}".format(words[i],words[j]))
        if k>5:
            break

    #print("{0:d} words have a Euclidean distance of +/-{0:d}.".format(k,n))


if __name__=="__main__":
    words = get_words()
    words = words[:1000]

    for n in [1,2,3,4,5]:
        print("-"*40)
        print("Distance of {0:d}".format(n))
        diff_by_n(n)

