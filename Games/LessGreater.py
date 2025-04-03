# A less-greater numbers game
import random
from base64 import b64encode, b64decode

secret = random.randint(1, 100)
print('Я загадал число от 1 до 100. Попробуй угадать!')

while True:
    guess = int(input('Твой вариант: '))
    if guess < secret:
        print('Больше!')
    elif guess > secret:
        print('Меньше!')
    else:
        print('Правильно! 🎉')
        break
