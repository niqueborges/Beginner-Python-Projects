import random

def guess(x):
    randow_number = random.randint(1, x)
    guess = 0
    while guess != randow_number:
        guess = int(input(f'Guess a number between 1 and (x): '))
        if guess < randow_number:
            print('Sorry, guess again. Too low. ')
        elif guess > randow_number:
            print('Sorry, guess again. Too high. ')
            
    
guess(10)