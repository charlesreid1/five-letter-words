import random, math, operator
from pprint import pprint 

random.seed(1337)

"""
euclidean_dist.py 

Compute euclidean distance between 5-letter words.
"""

def euclidean_distance(word1, word2):
    v1 = word2vec(word1)
    v2 = word2vec(word2)
    return l2norm(v1,v2)

def l2norm(vec1, vec2):
    radicand = [(v2-v1)*(v2-v1) for (v1,v2) in zip(vec1,vec2)]
    return math.sqrt(sum(radicand))

def word2vec(word):
    charvec = []
    vec = []
    for c in word:
        charvec.append(c)
        vec.append(ord(c)-ord('a'))
    return vec

def print_tuple(e):
    print("Distance between {0:s} and {1:s} = {2:f}".format(*e))


if __name__=="__main__":

    # Load the file.
    with open('sgb-words.txt','r') as f:
        ## This includes \n at the end of each line:
        #words = f.readlines()
    
        # This drops the \n at the end of each line:
        words = f.read().splitlines()

    eds = []
    for i in range(100):
        w1 = words[random.randint(1,5757)]
        w2 = words[random.randint(1,5757)]
        ed = euclidean_distance(w1,w2)
        eds.append((w1,w2,ed))

    sorted_eds = sorted(eds, key=operator.itemgetter(2))

    for e in sorted_eds:
        print_tuple(e)

