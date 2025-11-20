from datetime import datetime


class InvalidDateError(Exception):
    pass


def collect_person_details():
    name = input("Enter your name: ").strip()
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ").strip()
    email = input("Enter your email: ").strip()
    phone = input("Enter your phone number: ").strip()

    try:
        dob = datetime.strptime(dob_input, "%Y-%m-%d").date()
    except ValueError:
        raise InvalidDateError("Invalid date format or value. Please use YYYY-MM-DD.")

    return {
        "name": name,
        "date_of_birth": dob,
        "email": email,
        "phone": phone,
    }


if __name__ == "__main__":
    try:
        details = collect_person_details()
    except InvalidDateError as error:
        print(error)
    else:
        print("Collected details:")
        for key, value in details.items():
            print(f"{key}: {value}")

