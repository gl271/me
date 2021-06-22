"""Set 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """
    # the tests are looking for the exact string "You got it!". Don't modify that!

    print("Welcome to the guessing game!")
    print("A number between 0 and _ ?")
    correct_answer = False
    while correct_answer == False:
        LowerBound = input("Enter a lower bound \n")
        if isinstance(LowerBound, int) == True:
            correct_answer = True
        # isinstance checks variable to see what type it is (number or word etc) - specificed in int or chr
        else:
            print("Not a number, try again")
    print("OK then, a number between {} and 0 ?".format(LowerBound))
    LowerBound = int(LowerBound)

    correct_answer = False
    while correct_answer == False:
        UpperBound = input("Enter an upper bound \n")
        try:
            UpperBound / 2
            correct_answer = True
        except:
            print("Not a number, try again")
    print("OK then, a number between 0 and {} ?".format(UpperBound))
    UpperBound = int(UpperBound)

    actualNumber = random.randint(LowerBound, UpperBound)

    guessed = False

    while not guessed:
        guessedNumber = int(input("Guess a number: "))
        print(
            "You guessed {},".format(guessedNumber),
        )
        if guessedNumber == actualNumber:
            print("You got it!! It was {}".format(actualNumber))
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again :'(")
        else:
            print("Too big, try again :'(")
    return "You got it!"


if __name__ == "__main__":
    print(advancedGuessingGame())
