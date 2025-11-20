import re

MOBILE_PATTERN = re.compile(r"^[789]\d{9}$")


def is_valid_mobile(number: str) -> bool:
    return bool(MOBILE_PATTERN.match(number.strip()))


if __name__ == "__main__":
    mobile = input("Enter a 10-digit mobile number: ").strip()
    if is_valid_mobile(mobile):
        print("Valid mobile number.")
    else:
        print("Invalid mobile number. It must start with 7/8/9 and be 10 digits.")

