def contains_ordered(numbers, target):
    left, right = 0, len(numbers) - 1
    while left <= right:
        mid = (left + right) // 2
        if numbers[mid] == target:
            return True
        if numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False


if __name__ == "__main__":
    ordered_list = [1, 3, 5, 7, 9, 11, 13]
    number = 7
    result = contains_ordered(ordered_list, number)
    print(f"{number} in list? {result}")

