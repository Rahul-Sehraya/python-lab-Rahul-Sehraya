def repeated_sum(n: int) -> int:
    n_str = str(n)
    return n + int(n_str * 2) + int(n_str * 3)


if __name__ == "__main__":
    try:
        number = int(input("Enter an integer: ").strip())
    except ValueError:
        print("Please enter a valid integer.")
    else:
        total = repeated_sum(number)
        print(f"n + nn + nnn = {total}")

