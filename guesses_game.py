import random


def guesses_game():
    random_number = random.randint(1, 10)
    number_of_guesses = 0

    while True:
        user_guess = input('Guess the number generated ')

        if user_guess == 'exit':
            break

        user_guess = int(user_guess)

        number_of_guesses += 1

        if user_guess == random_number:
            print('You guesed right. Number of guesses is ', number_of_guesses)

        if user_guess > random_number:
            print('You guessed too high')

        if user_guess < random_number:
            print('Your guess is too low')


guesses_game()