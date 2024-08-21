#!/usr/bin/env python3
import random

def special_rolls(die_1, die_2):
    die_sum = die_1 + die_2

    if sum == 2:
        return [die_sum, "Snake Eyes!!"]
    
    elif die_sum == 12:
        return [die_sum, "Boxcars!!"]
    
    else: return [die_sum, ""]

def die_roller():
    roll_1 = random.randint(1, 6)
    roll_2 = random.randint(1, 6)
    
    total = special_rolls(roll_1, roll_2)

    results = f"Roll the Dice?\nDie 1: {roll_1}\nDie 2: {roll_2}\nTotal: {total[0]}\n{total[1] if total [1] != '' else ''}\n"

    return results


#checks the users answer to see if program will continue
def user_choice(answer):
    if answer.lower() == "y":
        print(die_roller())
        return True
    elif answer.lower() != 'n':
        print("please answer with y/n")
        user_choice(input("Roll again?(y/n)"))
        return True
    
    else:return False

def main():
    print("Dice Roller")
    choice = input("Would you like to roll the dice?(y/n)")
    if choice.lower() == 'y':
        print(die_roller())
        while True:
            again = input("Roll again? (y/n): ")
            if not user_choice(again):
                break


if __name__ == "__main__":
    main()