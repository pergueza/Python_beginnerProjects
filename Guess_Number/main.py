import random


def main():
    """The main function, this is the initialize of whole program.
    """

    print("Hello dear user, we going to play Guess the number.")
    print("First, we need a integer bigger than 1, this number will be the",
          "maximum number that it can take.")
    showMenu()


def showMenu():
    """This function print multiple options for the user.
    """

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


def guessUser(maxNumber: int):
    """With this function the user can play against the computer, the computer
    choose a random number between 1 and the max number and the user try to
    guess it.

    Args:
        maxNumber (int): The maximum number that it can take.
    """
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


def guessSystem(maxNumber: int):
    """With this function the computer can play against the user, the user
    needs to think in one number between 1 and the max number and the computer
    try to guess his number.

    Args:
        maxNumber (int): The maximum number that it can take.
    """
    low = 1
    high = maxNumber
    correctNumber = False
    while (not correctNumber):
        guessNumber = ((high - low) // 2) + low
        print(f"\nThe number is {guessNumber}?")
        print("1. It's correct.")
        print("2. The number is too high.")
        print("3. The number is too low.")
        print("4. Return to the menu.")
        try:
            option = int(input("Option: "))
            if option == 1:
                print("Oh yeah, good game!!!")
                correctNumber = True
            elif option == 2:
                high = guessNumber
            elif option == 3:
                low = guessNumber
            elif option == 4:
                break
            else:
                print("Please enter a valid option.")
        except ValueError:
            print("Please enter a valid option")


main()
