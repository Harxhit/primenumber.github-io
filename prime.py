# def check_prime(number):
#     is_prime = True
#     if number < 2:
#         is_prime = False
#     for i in range(2, int(number ** 0.5) + 1): 
#         if number % i == 0: 
#             is_prime = False
#             break
#     if is_prime: 
#         print(f"{number} is a prime number.")
#     else: 
#         print(f"{number} it is a composite number.")

# n = int(input("Enter a number: "))

# check_prime(n)


def is_prime(number):
    """
    This function checks if a number is prime.
    
    Parameters:
    number (int): The number to check.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    """
    This function prompts the user for a number and checks if it is prime or composite.
    """
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is a composite number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()