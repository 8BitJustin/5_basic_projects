from random import randint
import time

def random():
    """Function titled 'random'. Will take a number you provide, and will give a random number between that and 1."""
    numInput = input('Roll between 1 and what? (type in a number) ')  # Asks for number, stores in numImput
    run = input('Roll for random number from 1 to ' + str(numInput) + '? (y or n) ')  # Confirms the number provided
    while True:  # While loop, will run until broke (break)
        if run == 'y':  # If the run input was 'y', run below script
            rand_num = randint(1, int(numInput))  # Gives random number from 1 to num provided
            comment = 'You rolled a ...'
            print(comment)
            time.sleep(2)  # Gives a 2 sec pause (anticipation yo)
            print(str(rand_num) + '!')  # Prints the number as a string (as it's an int)
            again = input('Run again? (y or n) ')
            if again == 'y':
                continue  # If ran again, it'll continue
            else:
                print('Thank you for rolling with us!')
                break  # If not, it breaks
        else:
            break  # Will also break if other than 'y' was provided to run

random()  # Runs script