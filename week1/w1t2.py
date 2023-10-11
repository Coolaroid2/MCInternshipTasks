import numpy as np
x = np.random.randint(1,100)
print("-----Number Guessing Game-----")
print("You have 7 tries to guess the number. 'g' can be entered anytime to give up.")
guesses = 6
while True:
    if guesses == -1:
        print(f'Good Try! The number was {x}')
        break
    useri = input("Enter your guess: ")
    if useri == 'g':
        print(f'Good Try! The number was {x}')
        break
    if int(useri) == x:
        print(f'Correct! The number was {x}')
        break
    if guesses > 0:
        if int(useri) < x:
            print(f'Guess higher. Number of tries left: {guesses}')
        if int(useri) > x:
            print(f'Guess lower. Number of tries left: {guesses}')
    guesses -= 1