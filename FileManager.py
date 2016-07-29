WORD_MIN_LENGTH = 3
WORD_MAX_LENGTH = 10

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