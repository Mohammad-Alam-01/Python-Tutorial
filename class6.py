#  Conditional statements
# if condition:
#     statement
# elif condition:
#     statement
# else:
#     statement

# age  = int(input("enter your age:"))
# if age >= 18:
#     print("you are elder")

# else:
#     print("you are child")


# paisa = int(input("enter your paisa:"))

# if paisa == 50:
#     print("I can eat only veg biryani")

# elif paisa == 100:
#     print("I can eat only biryani")

# else:
#     print("I can eat chicken changezi")


# question 1st
#  check which number is greater

# a = float(input("enter first number:"))
# b = float(input("enter second number:"))

# if a > b:
#     print(f"{a} is greater than {b}")

# elif a < b:
#     print(f"{b} is greater than {a}")

# else:
#     print(f"{a} and {b} both are equal") 


# ======================== Question 2nd and 3rd
# ======================== Greet by gender and Greeting by case sensitive

# gender = input("enter your gender:")

# if gender == "Male" or gender == "male" or gender == "M" or gender == "m":
#     print("Good Morning Sir")

# elif gender == "Female" or gender == "female" or gender == "F" or gender == "f":
#     print("Good Morning Ma'am")
# else:
#     print("Please enter a valid gender")


# ======================== Question 4th
# ======================== check user number is even or odd

# number = int(input("enter a number:"))

# if number % 2 == 0:
#     print(f"{number} is even")

# else:
#     print(f"{number} is odd")


# ======================== Question 5th
# ======================== check a person is eligible to vote or not

# name = input("enter your name: ")
# age = int(input("enter your age: "))

# if age >=18:
#     print(f"{name} is eligible to vote")

# else:
#     print(f"{name} is not eligible to vote. \nAfter {18-age} you will be eligible to vote")


# ======================== Question 6th
# ======================== check a Days of week checker

day = int(input("enter a number:"))
day = day % 7

if day == 1:
    print("Sunday")

elif day == 2:
    print("Monday")

elif day == 3:
    print("Tuesday")

elif day == 4:
    print("Wednesday")

elif day == 5:
    print("Thursday")

elif day == 6:
    print("Friday")

elif day == 7:
    print("Saturday")

else:
    print("Please enter a valid number")