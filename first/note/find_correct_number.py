import random

secret_number = random.randint(1, 20)

for guess_taken in range(1, 7):
    print("input the number of your guess")
    guess = int(input())

    if guess < secret_number:
        print("Small")
    elif guess > secret_number:
        print("Big")
    else:
        break

if guess == secret_number:
    print("corect " + str(guess_taken) + "dd")
else:
    print("sorry corect answer is" + str(secret_number))
