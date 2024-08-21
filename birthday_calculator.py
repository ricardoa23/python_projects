import datetime

def main():
    print("Birthday Calaculator")
    name = input("Enter name:")
    birthdate = input("Enter Birthdate:")
    birthday_object = datetime.datetime.strptime(birthdate, "%m/%d/%Y")
    formatted_birthdate = birthday_object.strftime("%A, %B %d, %Y")
    print(formatted_birthdate)
    return None

if __name__ == "__main__":
    main()