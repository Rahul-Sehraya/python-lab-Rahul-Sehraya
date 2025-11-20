def is_vowel(letter: str) -> bool:
    """Return True if the provided letter is a vowel."""
    return letter.lower() in {"a", "e", "i", "o", "u"}


if __name__ == "__main__":
    character = input("Enter a single letter: ").strip()

    if len(character) != 1 or not character.isalpha():
        print("Please enter exactly one alphabetic character.")
    else:
        if is_vowel(character):
            print(f"{character} is a vowel.")
        else:
            print(f"{character} is not a vowel.")

