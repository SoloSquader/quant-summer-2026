import random

while True:
    try:
        number = input("What is your POSITIVE number? ")
        number = int(number)
        if number>0:
            break
        else:
            "POSITIVE, please."
    except ValueError:
        continue


correct_number = random.randint(1,number) 
while True:
    try:
        guess = input("What is your guess? ")
        guess = int(guess)
        if guess<=0:
            continue
        if guess>correct_number:
            print("Too Large!")
        if guess<correct_number:
            print("Too Small!")
        if guess==correct_number:
            print("Correct!")
            break
    except ValueError:
        continue
