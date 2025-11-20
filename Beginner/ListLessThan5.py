a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# Part 1: print elements less than 5 individually.
print("Numbers less than 5 (individual print):")
for number in a:
    if number < 5:
        print(number, end=" ")
print("\n")

# (a): new list with elements less than 5.
less_than_five = [number for number in a if number < 5]
print("Numbers less than 5 (as a list):", less_than_five)

# (b): one-line version.
print("One-liner:", [number for number in a if number < 5])

# (c): filter based on user provided threshold.
try:
    limit = int(input("Enter a number to filter the list: ").strip())
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    filtered = [number for number in a if number < limit]
    print(f"Numbers less than {limit}:", filtered)

