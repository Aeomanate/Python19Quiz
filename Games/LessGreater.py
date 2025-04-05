# A less-greater numbers game
from Common import decode
from Hints import encoded


def side():
    import random

    secret = random.randint(1, 100)
    print('I have a number from 1 to 100. Try to guess it!')

    while True:
        guess = int(input('Твой вариант: '))
        if guess < secret:
            print('Greater!')
        elif guess > secret:
            print('Less!')
        else:
            print('Correct! 🎉')
            break

side()

