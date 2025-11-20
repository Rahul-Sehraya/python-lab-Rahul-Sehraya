class RahulNameError(Exception):
    pass


def greet_user():
    name = input("Enter your name: ").strip()
    if name.lower() == "rahul":
        raise RahulNameError("Name 'Rahul' is not allowed. Please quit the program.")
    print(f"Hello, {name}!")


if __name__ == "__main__":
    try:
        greet_user()
    except RahulNameError as error:
        print(error)

