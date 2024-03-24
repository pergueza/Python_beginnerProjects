import random

maxNumber = int(input("Enter the maximum number that it can take"))


def guessUser(maxNumber):
    randomNumber = random.randint(1, maxNumber)
    guess = 0

    while guess != randomNumber:
        guess = int(input(f"Guess a number between 1 and {maxNumber}: "))

        if guess < randomNumber:
            print("Sorry, guess again. Too low.")
        elif guess > randomNumber:
            print("Sorry, guess again. Too high.")

    print("Wow, congrats. You have guessed the number",
          "{} correctly".format(randomNumber))


def guessSystem(maxNumber):
    return 0


guessUser(maxNumber)
