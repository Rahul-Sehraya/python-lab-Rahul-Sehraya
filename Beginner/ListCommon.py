a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def common_elements(list1, list2):
    return sorted(set(list1).intersection(list2))


if __name__ == "__main__":
    result = common_elements(a, b)
    print("Common elements (without duplicates):", result)

