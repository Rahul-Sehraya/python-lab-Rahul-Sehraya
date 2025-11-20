def remove_duplicates(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


if __name__ == "__main__":
    sample = [1, 2, 2, 3, 4, 4, 5, 1]
    print("Original list:", sample)
    print("Without duplicates:", remove_duplicates(sample))

