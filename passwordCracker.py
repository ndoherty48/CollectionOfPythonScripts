import itertools
import string
from datetime import datetime
import time
import secrets

chars = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits


def generate_secure_password(number_of_characters):
    return ''.join(secrets.choice(chars) for i in range(number_of_characters))


def how_many_combinations(password_length):
    possible_combinations = 0
    for password_len in range(1, password_length):
        possible_combinations += (len(chars) * password_len)
    print('Total Number of combinations for a {} length password with {} different characters is {}'
          .format(password_length, len(chars), possible_combinations))


def guess_password(real):
    attempts = 0
    for password_length in range(1, len(real)):
        for guess in itertools.product(chars, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            print('Guess: {}. Attempt: {}'.format(guess, attempts))
            if guess == real:
                end_date_time = datetime.now()
                print('End Time: {}'.format(end_date_time))
                duration = start_date_time - end_date_time
                return 'password is {}. found in {} guesses. total time taken {} seconds'.format(guess, attempts,
                                                                                                 duration * 60)
    return "Password Not Found"


if input("Would you like to create a Secure Password: (y/n) ") == "y":
    print('Secure Password: {}'.format(generate_secure_password(int(input("How many Characters do you want "
                                                                          "in your password: ")))))
if input("Would you like to see how long it would take to crack your password: (y/n) ") == "y":
    password_to_crack = input("Please Enter the password you would like to crack: ")
    how_many_combinations(len(password_to_crack))
    time.sleep(10)
    start_date_time = datetime.now()
    print('Start Time: {}'.format(start_date_time))
    print(guess_password(password_to_crack))
