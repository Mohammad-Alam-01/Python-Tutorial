import random

# num = random.randint(1,100)

# tries = 0

# while True:
#     guessed = int(input("Enter a number between 1 and 100: "))
#     tries += 1
#     if guessed == num:
#         print(f"You guessed the number in {tries} tries!")
#         break
#     elif guessed > num:
#         print("Please guess a smaller number.\n")
#     else:
#         print("please guess a larger number.\n")  

# ===================================================== game 2

# stone paper scissors

# user = input("Enter your choice (stone, paper, scissors): ")
# computer = random.choice(["stone", "paper", "scissors"])


cscore = 0
hscore = 0 

while True:
    print(f"current scores you - {hscore} computer - {cscore}\n")
    user = int(input("1 for stone , 2 for paper , 3 for scissors choose :- "))

    com = random.randint(1,3)

    if user == 1 and com == 3:
        hscore+=1 
        print("you won the round \n")

    elif user == 2 and com == 1:
        hscore+=1 

        print("you won the round \n")

    elif user == 3 and com == 2:
        hscore+=1 

        print("you won the round \n")

    elif user == com:
        print("it was a draw")

    else:
        cscore+=1 
        print("computer won this round ")
    

    if cscore == 5:
        print("conmputer won this game 👿")
        break
    elif hscore == 5:
        print("congratulations you won 🏅")
        break