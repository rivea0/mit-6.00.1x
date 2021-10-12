# Hangman game
#

# -----------------------------------
# Helper code

import random
import string 

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
    count = 0
    for letter in secretWord:
        if letter in lettersGuessed:
            count += 1

    if count == len(secretWord):
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
    output = ""

    for letter in secretWord:
        if letter in lettersGuessed:
            output += letter 
        else:
            output += " _ "
        
    return output 



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    letters = string.ascii_lowercase

    for i in lettersGuessed:
        if i in letters:
            letters = letters.replace(i, "")
    
    return letters

    

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("-------------")
    
    guess = 8
    lettersGuessed = []

    while guess >= 0:

        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            break
        elif guess == 0 and not isWordGuessed(secretWord, lettersGuessed):
            print("Sorry, you ran out of guesses. The word was " + secretWord + ".")
            break

        availableLetters = getAvailableLetters(lettersGuessed)

        print("You have " + str(guess) + " guesses left.")
        print("Available letters: " + availableLetters)

        guessedLetter = input("Please guess a letter: ").lower()

        if guessedLetter in lettersGuessed:
            print("Oops! You've already guessed that letter: " + guessed)
        else:
	        lettersGuessed.append(guessedLetter)        
	        guessed = getGuessedWord(secretWord, lettersGuessed)

	        if guessedLetter in secretWord:
	            print("Good guess: " + guessed)            
	        else:
	            print("Oops! That letter is not in my word: " + guessed)    
	            guess -= 1

        print("-------------")

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
