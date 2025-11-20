def largest_of_three(a, b, c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest


if __name__ == "__main__":
    try:
        first = float(input("Enter first number: "))
        second = float(input("Enter second number: "))
        third = float(input("Enter third number: "))
    except ValueError:
        print("Please enter valid numeric values.")
    else:
        print(f"The largest number is {largest_of_three(first, second, third)}")

