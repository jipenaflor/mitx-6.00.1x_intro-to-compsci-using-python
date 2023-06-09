# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    checker = ""
    for i in secretWord:
        for j in lettersGuessed:
            if i == j:
                checker += i
                break
    print(checker)
    if checker == secretWord:
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    tmp = []
    ans = ""
    for i in range(len(secretWord)):
        tmp.append("_ ")
    for j in range(len(lettersGuessed)):
        for k in range(len(secretWord)):
            if lettersGuessed[j] == secretWord[k]:
                tmp[k] = lettersGuessed[j]
    for m in tmp:
        ans += m
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    tmp = []
    availableLetters = ""
    for i in string.ascii_lowercase:
        tmp.append(i)
    for j in lettersGuessed:
        if j in tmp:
            tmp.remove(j)
    for k in tmp:
        availableLetters += k
    return availableLetters
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    secretLetters = 0
    play = ""l
    guesses = 8
    lettersGuessed = []
    mistakesMade = 0
    
    for i in secretWord:
        secretLetters += 1
        play += "_ "
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is ", secretLetters, " letters long." )
    print("-----------")

    while guesses != 0:
        print("You have ", guesses, " guesses left.")
        print("Available letters: ", getAvailableLetters(lettersGuessed))
        playerAttempt = input("Please guess a letter: ")
        if playerAttempt in lettersGuessed:
            print("Oops! You've already guessed that letter: " + playerAns)
            print("-----------")
            continue
        lettersGuessed.append(playerAttempt)
        playerAns = getGuessedWord(secretWord, lettersGuessed)
        if playerAns == play:
            print("Oops! That letter is not in my word: " + playerAns)
            guesses -= 1
        else:
            print("Good guess: " + playerAns)
            if "_ " not in playerAns:
                print("-----------")
                print("Congratulations, you won!")
                break
        play = playerAns
        print("-----------")
    
    if "_ " in playerAns:
        print("Sorry, you ran out of guesses. The word was", secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
