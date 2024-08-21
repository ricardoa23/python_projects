32.5

def meal_total():
    try:
        bill_total = float(input("Cost of meal: "))
        if bill_total <= 0:
            print('Number must be greater than 0')
            return None
    except:
        print("Please enter a valid decimal number.")
        return None

    try:
        tip_percent = int(input("Tip Percent: "))
        if tip_percent <= 0:
            print('Number must be greater than 0')
            return None
    except:
        print("Must be a valid integer")
        return None

    return [bill_total, tip_percent]


def tip_calculation(user_input):
    total = user_input[0]
    tip = user_input[1]
    
    tip_amount = total * (tip / 100)
    total_w_tip = total + tip_amount
    formatted_tip_amount = "{:.2f}".format(tip_amount)
    formatted_total_w_tip = "{:.2f}".format(total_w_tip)

    


    output = print(f"Cost of Meal: ${total}\nTip Percent:{tip}%\nTip Amount: ${formatted_tip_amount}\nTotal: ${formatted_total_w_tip}")

    return output







def main():
    input = meal_total()
    print("_" * 40)
    tip_calculation(input)


if __name__ == "__main__":
    main()

