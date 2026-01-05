import random

num = random.randint(1,100)

tries = 0

while True:
    guessed = int(input("Enter a number between 1 and 100: "))
    tries += 1
    if guessed == num:
        print(f"You guessed the number in {tries} tries!")
        break
    elif guessed > num:
        print("Please guess a smaller number.\n")
    else:
        print("please guess a larger number.\n")  