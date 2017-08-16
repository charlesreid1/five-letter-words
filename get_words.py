"""
get_words.py

Utility method to load the SBG words
and retun them as a list of strings.
"""

def get_words():
    # Load the file.
    with open('sgb-words.txt','r') as f:
        ## This includes \n at the end of each line:
        #words = f.readlines()
    
        # This drops the \n at the end of each line:
        words = f.read().splitlines()

    return words


