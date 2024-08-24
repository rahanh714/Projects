from random import randint
from logo import logo
print(logo)

HARD_TRIES = 5
EASY_TRIES = 10


def check_answer(user_guess, computer_number, number_of_tries):
    if user_guess == computer_number:
        print(f"You got it! The answer was {computer_number}")
        return
    elif user_guess < computer_number:
        print("Too low")
        return number_of_tries - 1
    elif user_guess > computer_number:
        print("Too high")
        return number_of_tries - 1


def difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "hard":
        return HARD_TRIES
    elif difficulty == "easy":
        return EASY_TRIES


def guess_number():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    computer_number = randint(1, 100)

    number_of_tries = difficulty()
    user_guess = 0
    while computer_number != user_guess:
        print(f"You have {number_of_tries} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        number_of_tries = check_answer(user_guess, computer_number, number_of_tries)
        if number_of_tries == 0:
            print("You've ran out of guesses, you lose.")
            return
        elif user_guess != computer_number:
            print("Guess again.")


guess_number()



