#!/usr/bin/env python3
#Grade conversion project
def letter_grade(num):
    if num_grade >= 90:
        return "A"
    elif num_grade >= 80:
        return "B"
    elif num_grade >= 70:
        return "C"
    elif num_grade >= 60:
        return "D"
    else: 
        return "F"

def should_continue():
    user_input = input("Would you like to continue? (y/n)")
    if (user_input.lower() == "y"):
        return True
    elif (user_input.lower() != 'n'):
        print("(PLEASE ENTER y OR n)")
        should_continue()
        return True
    else:
        return print("Bye!!!")  and  False


while True:
    num_grade = int(input("Please enter your numerical grade:"))
    result = letter_grade(num_grade)
    print(f"Your letter grade is: {result}")

    continue_prompt = should_continue()
    if not continue_prompt:
        break