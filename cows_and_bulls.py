"""
    Create a program that will play the “cows and bulls” game with the user. The game works like this:
    Randomly generate a 4-digit number.
    Ask the user to guess a 4-digit number.
    For every digit that the user guessed correctly in the correct place, they have a “cow”.
    For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess,
    tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
    Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""


import random


def cows_and_bulls_game():
    random_number = list((int(number) for number in str(random.randrange(1000, 9999))))
    number_of_guesses = 0

    while True:
        user_guess = input('Guess the four digit generated random number ')
        user_guess = [int(number) for number in user_guess]
        cows = 0
        bulls = 0
        number_of_guesses += 1

        print(random_number, user_guess)

        if len(user_guess) < 4:
            print('Your guess must have four digits')

        if random_number == user_guess:
            print('You guessed correct. Number of guesses are {}'.format(number_of_guesses))
            break

        for key, value in enumerate(user_guess):
            if random_number[key] == value:
                cows += 1
            elif value in random_number:
                bulls += 1

        print('You have {} cows and {} bulls at {} number of guesses'.format(cows, bulls, number_of_guesses))


cows_and_bulls_game()
