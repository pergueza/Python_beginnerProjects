import random


def guess(x):
    randomNumber = random.randint(1, x)
    guess = 0

    while guess != randomNumber:
        guess = int(input("Guess a number between 1 and {}: ".format(x)))
        if guess < randomNumber:
            print("Sorry, guess again. Too low.")
        elif guess > randomNumber:
            print("Sorry, guess again. Too high.")

    print("Wow, congrats. You have guessed the number",
          "{} correctly".format(randomNumber))


guess(int(input("Enter the maximum number to guessed: ")))
