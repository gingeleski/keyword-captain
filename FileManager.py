WORD_MIN_LENGTH = 3
WORD_MAX_LENGTH = 10

def addWordToTree(word_tree, word):
    """
    Add word to given tree. Can be used recursively.
    """
    if word == "":
        word_tree[True] = True
        return
    head, tail = word[0], word[1:]
    if head not in word_tree:
        word_tree[head] = {}
    addWordToTree(word_tree[head], tail)

def loadWordTree(wordfile):
    """
    Args:
        wordfile - path to a file containing one word per line
    """
    word_tree = {}
    for word in open(wordfile):
        addWordToTree(word_tree, word)
    return word_tree

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
        elif "'" in word:
            working_list.remove(word)
    return working_list

def saveWordList(filename, wordlist):
    file = open(filename, "w")
    for word in wordlist:
        file.write(word)
    file.close()
