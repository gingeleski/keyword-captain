from copy import copy
from Board import Board

def loadWordList(wordfile):
    wordlist = None
    with open(wordfile) as f:
        wordlist = f.readlines()
    return wordlist

def cleanWordList(wordlist):
    working_list = copy(wordlist)
    for word in working_list:
        if (len(word) < 3) or (len(word) > 10):
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

# Warning - hacky testing below
wordlist = loadWordList("words.txt")
brd = Board()
print(brd.board[0][0].value)