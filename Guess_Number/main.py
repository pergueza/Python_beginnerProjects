import random


def main():
    print("Hello dear user, we going to play Guess the number.")
    print("First, we need a integer bigger than 1, this number will be the",
          "maximum number that it can take.")
    showMenu()


def showMenu():
    maxNumber = 0
    showOptions = True

    while maxNumber <= 1:
        try:
            maxNumber = int(input("Enter a number: "))
            if maxNumber <= 1:
                print("Please enter a number bigger than 1.")
        except ValueError:
            print("Please enter a valid number.")

    while (showOptions):
        print("\nNow choose the option that you want.")
        print("1. Guess the number of the system generated.")
        print("2. System try to guess your number.")
        print("3. Exit")
        try:
            option = int(input("Option: "))
        except ValueError:
            print("Please enter the number of the option.")

        if option == 1:
            guessUser(maxNumber)
        elif option == 2:
            guessSystem(maxNumber)
        elif option == 3:
            print("Goodbye!")
            showOptions = False
        else:
            print("Invalid option. Please enter a number between 1 and 3")


def guessUser(maxNumber):
    randomNumber = random.randint(1, maxNumber)
    guess = int

    while guess != randomNumber:
        try:
            guess = int(input(f"Guess a number between 1 and {maxNumber}: "))

            if guess < randomNumber:
                print("Sorry, guess again. Too low.")
            elif guess > randomNumber:
                print("Sorry, guess again. Too high.")
        except ValueError:
            print("Please enter a valid number.")

    print("Wow, congrats. You have guessed the number",
          "{} correctly".format(randomNumber))


def guessSystem(maxNumber):
    return 0


main()
