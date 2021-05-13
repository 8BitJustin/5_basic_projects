# Guess random number
from random import randint

def guess_game():
    """Function that runs a simple number guessing game"""
    mystery = randint(1, 10)
    attempt = 2

    while attempt > -1:

        guess = input('Give me a number ranging from 1 to 10 please: ')
        if int(guess) > 10:
            continue

        if int(guess) == mystery:
            print('\nYou guessed ' + str(mystery) + ' and won!')
            break

        elif int(guess) < mystery:
            if attempt == 0:
                print('\nYou failed, the number was ' + str(mystery) + '.')
                break
            else:
                print('\nHigher... you have ' + str(attempt) + ' attempts left.')
                attempt -= 1

        elif int(guess) > mystery and int(guess) < 11:
            if attempt == 0:
                print('\nI\'m sorry, the number was ' + str(mystery) + '.')
                break
            else:
                print('Lower... you have ' + str(attempt) + ' attempts left.')
                attempt -= 1

        else:
            break

guess_game()