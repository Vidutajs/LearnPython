import random

guess = random.randint(1, 20)
answer = ''
count = 0

print('I am thinking of a number from 1 to 20.')
print('Can you guess it?')

while answer != guess :
    print('Taka guess!')
    answer = int(input())
    if answer > guess :
        print('Your guess is too high.')
    elif answer < guess :
        print('Your guess is too low.')
    count = count + 1
print('Good job! You guessed my number (' + str(guess) + ') in ' + str(count) + ' guesses!')