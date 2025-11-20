def parse_sequence(sequence: str):
    items = [item.strip() for item in sequence.split(",") if item.strip()]
    return items, tuple(items)


if __name__ == "__main__":
    user_input = input("Enter comma-separated numbers: ")
    numbers_list, numbers_tuple = parse_sequence(user_input)
    print(f"List: {numbers_list}")
    print(f"Tuple: {numbers_tuple}")

