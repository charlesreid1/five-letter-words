#!/usr/bin/env python
from get_words import get_words
import sys
import math

"""
tries.py

Donald Knuth, Art of Computer Programming, Volume 4 Fascicle 0
Exercise #35

Problem:
What letters of the alphabet can be used
as the starting letter of sixteen words that
form a complete binary trie within
WORDS(n), given n?

Example trie: 

   Left side:
                    s
         h               
    e        o
  e   l    r   w

   Right side:

     s
            t
        a       e
      l   r   a    e

"""


ALPHABET = "abcdefghijklmnopqrstuvwxyz"
FIVE = 5


class Node(object):
    def __init__(self, letter, count=0):
        self.letter = letter
        self.count = count
        self.children = []
        self.parent = None


class TryTrieTree(object):
    def __init__(self,words):
        self.root = None
        self.words = words

    def __str__(self):
        final = ""
        depth = 1
        runner = self.root

        def _str_recursive(runner,depth):
            # In order traversal:
            # visit this node first,
            # then visit children if any
            s = ""
            s += ">"*depth
            s += " "
            s += self.get_prefix_from_node(runner)
            s += runner.letter
            s += ": %d"%(runner.count)
            s += "\n"

            # Base case
            if runner.children == []:
                # leaf node
                return s

            # Recursive case
            else:
                for child in runner.children:
                    s += _str_recursive(child,depth+1)
                return s

        final = _str_recursive(runner,depth)
        return final


    def set_root(self,root_letter):
        self.root = Node(root_letter)


    def get_prefix_from_node(self,node):
        """Given a node in the trie,
        return the string prefix that
        would lead to that node.
        """
        if node==None:
            return ""
        elif node==self.root:
            return ""
        else:
            prefix = ""
            while node.parent != None:
                node = node.parent
                prefix = node.letter + prefix
            return prefix


    def get_node_from_prefix(self,prefix):
        """Given a string prefix,
        return the node that represents
        the tail end of that sequence
        of letters in this trie. Return
        None if the path does not exist.
        """
        assert self.root!=None

        if prefix=='':
            return None

        assert prefix[0]==self.root.letter

        # Base case
        if len(prefix)==1:
            return self.root

        # Recursive case
        parent_prefix, suffix = prefix[:len(prefix)-1],prefix[len(prefix)-1]
        parent = self.get_node_from_prefix(parent_prefix)
        for child in parent.children:
            if child.letter == suffix:
                return child

        # We know this will end because we handle
        # the base case of prefix="", and prefix
        # is cut down by one letter each iteration.


    def assemble(self):
        """Assemble the trie from the set of words
        passed to the constructor.
        """
        assert self.root!=None

        words = self.words

        # start with an empty prefix
        prefix = ''
        candidate = self.root.letter
        self._assemble(prefix,candidate,words)


    def _assemble(self,prefix,candidate,words):
        """Recursive private method called by assemble().
        """
        prefix_depth = len(prefix)
        candidate_depth = prefix_depth+1

        ppc = prefix+candidate
        words_with_candidate = [w for w in words if w[:candidate_depth]==ppc]

        min_branches_req = int(math.pow(2,5-candidate_depth))
        max_number_branches = len(words_with_candidate)

        # If we exceed the minimum number of 
        # branches required, add candidate
        # as a new node on the trie.
        if max_number_branches >= min_branches_req:

            parent = self.get_node_from_prefix(prefix)
            
            # If we are looking at the root node,
            if prefix=='':
                # parent will be None.
                # In this case don't worry about
                # creating new child or introducing
                # parent and child, b/c the "new child"
                # is the root (already exists).
                pass

            else:
                # Otherwise, create the new child,
                # and introduce the parent & child.
                new_child = Node(candidate)
                new_child.parent = parent
                parent.children.append(new_child)

            # Base case
            if candidate_depth==4:
                new_child.count = max_number_branches
                return

            # Recursive case
            for new_candidate in ALPHABET:
                new_prefix = prefix + candidate
                self._assemble(new_prefix,new_candidate,words_with_candidate)

        # otherwise, we don't have enough
        # branches to continue downward,
        # so stop here and do nothing.
        return


    def bubble_up(self):
        """Do a depth-first traversal of the
        entire trytrietree, pruning as we go.
        This is a pre-order traversal,
        meaning we traverse children first,
        then the parents, so we always 
        know the counts of children
        (or we are on a leaf node).
        """
        self._bubble_up(self.root)


    def _bubble_up(self,node):
        """Pre-order depth-first traversal
        starting at the leaf nodes and proceeding
        upwards.
        """
        if len(node.children)==0:
            # Base case
            # Leaf nodes already have counts          
            # Do nothing
            return

        else:
            # Recursive case
            # Pre-order traversal: visit/bubble up children first
            for child in node.children:
                self._bubble_up(child)

            # Now that we've completed leaf node counts, we can do interior node counts.
            # Interior node counts are equal to number of large (>=2) children.
            large_children = [child for child in node.children if child.count >= 2]
            node.count = len(large_children)


def trie_search(n, verbose=False):

    words = get_words()
    words = words[:n]

    perfect_count = 0
    imperfect_count = 0
    for letter in ALPHABET:

        tree = TryTrieTree(words)
        tree.set_root(letter)
        tree.assemble()
        tree.bubble_up()
        #print(tree)

        if tree.root.count >= 2:

            if verbose:
                print("The letter {0:s} has a perfect binary trie in WORDS({1:d}).".format(
                    letter, n))
            perfect_count += 1

        else:

            if verbose:
                print("The letter {0:s} has no perfect binary trie in WORDS({1:d}).".format(
                    letter, n))
            imperfect_count += 1

    if verbose:
        print("")
        print("Perfect count: {:d}".format(perfect_count))
        print("Imperfect count: {:d}".format(imperfect_count))

    return perfect_count, imperfect_count


def trie_table():
    """Compute and print a table of
    number of words n versus number of
    perfect tries formed.
    """
    print("%8s\t%8s"%("n","perfect tries"))

    ns = range(1000,5757,500)
    for n in ns:
        p,i = trie_search(n)
        print("%8d\t%8d"%(n,p))

    n = 5757
    p,i = trie_search(n)
    print("%8d\t%8d"%(n,p))


if __name__=="__main__":
    if len(sys.argv)<2:
        n = 5757
    else:
        n = int(sys.argv[1])
        if n > 5757:
            n = 5757

    _,_ = trie_search(n, verbose=True)

    #trie_table()

