from datetime import datetime


def days_between(date1_str, date2_str, fmt="%Y-%m-%d"):
    date1 = datetime.strptime(date1_str, fmt).date()
    date2 = datetime.strptime(date2_str, fmt).date()
    return abs((date2 - date1).days)


if __name__ == "__main__":
    fmt = "%Y-%m-%d"
    print("Enter both dates in YYYY-MM-DD format.")
    first = input("First date: ").strip()
    second = input("Second date: ").strip()

    try:
        difference = days_between(first, second, fmt)
        print(f"Number of days between the two dates: {difference}")
    except ValueError as error:
        print(f"Invalid date supplied: {error}")

