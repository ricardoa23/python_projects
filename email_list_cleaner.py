#!/usr/bin/env python3


import csv


def title_f(name):
    return name.title()


def cleaned_email_list(source_file, cleaned_file):
    with open(source_file, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = ['First_Name', 'Last_Name', 'email']
        cleaned_data = []

        for row in reader:
            first_name = title_f(row['FIRST_NAME'].strip())
            last_name = title_f(row['LAST_NAME'].strip())
            email = row['EMAIL'].strip().lower()

            cleaned_data.append({
                'First_Name': first_name,
                'Last_Name': last_name,
                'email': email
            })

    with open(cleaned_file, 'w', newline='') as cleaned_csvfile:
        writer = csv.DictWriter(cleaned_csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(cleaned_data)


def main():
    print("Welcome to the Email List Cleaner")

    input_file = 'prospects.csv'
    cleaned_file = 'prospects_clean.csv'

    cleaned_email_list(input_file, cleaned_file)

    print("Congratulations! Your list has been cleaned!")

if __name__ == "__main__":
    main()
