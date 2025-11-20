def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    factor = 5
    while factor * factor <= number:
        if number % factor == 0 or number % (factor + 2) == 0:
            return False
        factor += 6
    return True


if __name__ == "__main__":
    try:
        user_number = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
    else:
        if is_prime(user_number):
            print(f"{user_number} is a prime number.")
        else:
            print(f"{user_number} is not a prime number.")

