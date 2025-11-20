import os


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def count_characters(filename: str) -> dict:
    counts = {}
    with open(filename, "r", encoding="utf-8") as file:
        for char in file.read():
            counts[char] = counts.get(char, 0) + 1
    return counts


if __name__ == "__main__":
    base_dir = "FileOperationTxts"
    ensure_directory(base_dir)

    target_file = os.path.join(base_dir, "char_count_sample.txt")

    with open(target_file, "w", encoding="utf-8") as file:
        file.write("Hello world!\nCounting characters in this file.")

    frequencies = count_characters(target_file)

    print(f"Character frequencies in {target_file}:")
    for character, count in sorted(frequencies.items()):
        display = character if character.strip() else repr(character)
        print(f"{display}: {count}")

