def find_divisors(number: int):
    return [i for i in range(1, number + 1) if number % i == 0]


if __name__ == "__main__":
    try:
        user_number = int(input("Enter a positive integer: ").strip())
        if user_number <= 0:
            raise ValueError("Number must be positive.")
    except ValueError as error:
        print(f"Invalid input: {error}")
    else:
        divisors = find_divisors(user_number)
        print(f"Divisors of {user_number}: {divisors}")

