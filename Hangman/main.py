import pandas as pd
import random
import string
from unicodedata import normalize
translateTab = dict.fromkeys(map(ord, u'\u0301\u0308'), None)


def lenguage() -> int:
    """The player can choose between a spanish word or english word.

    Returns:
        int: The option that the player choose.
    """
    while (True):
        print("Choose one option.")
        print("1. English word")
        print("2. Spanish word")

        try:
            option = int(input("Option: "))

            if (option in [1, 2]):
                return option
            print("\nChoose a valid option please.")

        except ValueError:
            print("\nPlease choose a valid option.")


# We going to extract the words from a JSON file.
if (lenguage() == 1):
    words = pd.read_json("https://www.randomlists.com/data/words.json")
else:
    words = pd.read_json("https://raw.githubusercontent.com/bitcoinjs/\
bip39/master/ts_src/wordlists/spanish.json")


def hangman():
    word = getValidWord(words)
    alphabet = set(string.ascii_uppercase)
    alphabet.add("ñ")
    usedLetters = set()
    wordLetters = set(word)
    opportunities = opportunitiesInput()

    while (len(wordLetters) != 0) and (opportunities > 0):
        wordList = [char if char in usedLetters else "-" for char in word]
        print("\nYou have used these letters:", " ".join(usedLetters))
        print("Current word:", " ".join(wordList))

        if (userInput(alphabet, usedLetters, wordLetters)):
            print("\nGreat job!! You guess a letter.")

        else:
            print("\nIncorrect letter, you lose one opportunitie.")
            opportunities -= 1
            print("You have {} opportunities".format(opportunities))

    wordList = [char if char in usedLetters else "-" for char in word]
    print("Current word:", " ".join(wordList))
    if opportunities == 0:
        print("\nYou lose :(")
        print("The word was", word)

    else:
        print("\nYou won!!")
        print("The word was", word)


def getValidWord(words) -> str:
    """This function choose randomly a valid word of the file .json

    Args:
        words (dataframe): List of words

    Returns:
        str: Retrun a valid word.
    """
    word = words.iloc[random.randint(0, len(words)), 0]

    while ('-' in word) or (' ' in word):
        word = words.iloc[random.randint(0, len(words)), 0]

    return normalize("NFKC",
                     normalize("NFKD", word.upper()).translate(translateTab))


def opportunitiesInput() -> int:
    """This fuction recives the number of opportunities that
    the user want for try to guess the word.

    Returns:
        int: Return the number of opportunities.
    """
    opportunities = 0
    print("\nPlease enter the number of opportunities.")

    while (opportunities <= 0):
        try:
            opportunities = int(input("Opportunities: "))
            if (opportunities <= 0):
                print("\nPlease enter a number bigger than 0.")

        except ValueError:
            print("\nPlease enter a valid number")
    return opportunities


def userInput(alphabet: set, usedLetters: set, wordLetters: set) -> bool:
    """This function recives the letter that the player enter.

    Args:
        alphabet (set): Set of letter of alphabet.
        usedLetters (set): Set of letter that the player played.
        wordLetters (set): Set of letter of the word.

    Returns:
        bool: True if the letter is in the word or False otherwise.
    """
    while (True):
        userLetter = input("Guess a letter: ").upper()

        if (userLetter in alphabet - usedLetters):
            usedLetters.add(userLetter)
            if (userLetter in wordLetters):
                wordLetters.remove(userLetter)
                return True
            return False

        elif (userLetter in usedLetters):
            print("\nYou have already used that character. Please try again.")

        else:
            print("\nInvalid character, please try again.")


hangman()
