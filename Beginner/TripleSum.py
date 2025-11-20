def triple_sum(a: int, b: int, c: int) -> int:
    total = a + b + c
    return total * 3 if a == b == c else total


if __name__ == "__main__":
    try:
        first = int(input("Enter first number: ").strip())
        second = int(input("Enter second number: ").strip())
        third = int(input("Enter third number: ").strip())
    except ValueError:
        print("Please enter valid integers only.")
    else:
        result = triple_sum(first, second, third)
        print(f"Result: {result}")

