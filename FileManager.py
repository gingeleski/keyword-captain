WORD_MIN_LENGTH = 3
WORD_MAX_LENGTH = 10

def addWordToTree(tree, word):
    """
    Add word to given tree. Can be used recursively.
    """
    if word:
        head, tail = word[0], word[1:]
        # If the word's first letter is not in the subtree, create
        # an empty node
        if head not in tree:
            tree[head] = {}
        # Add rest of the word to the subtree
        addWordToTree(tree[head], tail)
    else:
        # If given empty word, add a final state in the tree, to
        # note that the path from the root to here is a valid word
        tree[EOW] = EOW

def loadWordTree(wordfile):
    """
    Args:
        wordfile - path to a file containing one word per line
    """
    tree = dict()
    with open(wordfile) as f:
        for word in f:
            word = word.strip()
            addWordToTree(tree,word)
    return tree

def loadWordList(wordfile):
    wordlist = None
    with open(wordfile) as f:
        wordlist = f.readlines()
    return wordlist

def cleanWordList(wordlist):
    working_list = copy(wordlist)
    for word in working_list:
        if (len(word) < WORD_MIN_LENGTH) \
                or (len(word) > WORD_MAX_LENGTH):
            working_list.remove(word)
            print('removing ', word)
        elif "'" in word:
            working_list.remove(word)
            print('removing ', word)
    return working_list

def saveWordList(filename, wordlist):
    file = open(filename, "w")
    for word in wordlist:
        file.write(word)
    file.close()
