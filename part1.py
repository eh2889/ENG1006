#Erik Hansen
#9/26/2019
#numberGuessingGame - guessing a number

from random import randint
tries = 0
num = randint(1,10)
while tries<5:
    guess = int(input('Guess a number between 1 and 10: '))
    tries = tries + 1
    if abs(guess-num)>5:
        print('Your guess is not even close')
    elif abs(guess-num)<=5 and abs(guess-num)>=3:
        print('Your guess is close')
    elif abs(guess-num)<3 and abs(guess-num)>0:
        print('Your guess is almost there')
    else:
        print('You got it in', tries, 'tries')
        break
if tries==5:    
    print('You lost :(')
