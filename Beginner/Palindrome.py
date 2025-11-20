def is_palindrome(text: str) -> bool:
    normalized = "".join(char.lower() for char in text if char.isalnum())
    return normalized == normalized[::-1]


if __name__ == "__main__":
    user_text = input("Enter a string: ").strip()
    if not user_text:
        print("You must enter a non-empty string.")
    else:
        if is_palindrome(user_text):
            print("It is a palindrome.")
        else:
            print("It is not a palindrome.")

