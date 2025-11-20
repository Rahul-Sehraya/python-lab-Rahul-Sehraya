import random


def play_game():
    target = random.randint(1, 9)
    while True:
        guess = input("Guess a number between 1 and 9 (or 'exit' to quit): ").strip()
        if guess.lower() == "exit":
            print(f"The number was {target}. Goodbye!")
            break

        try:
            guess_num = int(guess)
        except ValueError:
            print("Please enter a valid integer or 'exit'.")
            continue

        if guess_num < 1 or guess_num > 9:
            print("Number must be between 1 and 9.")
            continue

        if guess_num < target:
            print("Too low! Try again.")
        elif guess_num > target:
            print("Too high! Try again.")
        else:
            print("Exactly right! You guessed it!")
            break


if __name__ == "__main__":
    play_game()

