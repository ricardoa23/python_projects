import math

def is_prime(num):
    if num <= 1:
        return False
    
    for i in  range(2, int(math.sqrt(num))):
        if num % i == 0:
            return False
        
    return True


def get_factor(num):
    factors = []

    for i in range(1, num):
        if num % i == 0:
            factors.append(i)
            
    return factors
    
def validate_number(num):
    if num < 1 or num > 5000:
        return False
    
    return True


def main():
    user_num = int(input("Enter a number between 1 and 5000: "))

    if not validate_number(user_num):
        print("please enter a valid number.")
        return
    
    if is_prime(user_num):
        print(f"{user_num} is a prime number.")
        return
    else: 
        print(f"{user_num} is not a prime")
        factors = get_factor(user_num)
        print(f"{user_num} has {len(factors)} which are: {factors}")


if __name__ == "__main__":
    main()