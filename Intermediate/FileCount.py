import os


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def file_counts(filename: str):
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    characters = sum(len(line) for line in lines)
    words = sum(len(line.split()) for line in lines)
    line_count = len(lines)

    return characters, words, line_count


if __name__ == "__main__":
    base_dir = "FileOperationTxts"
    ensure_directory(base_dir)

    file_path = os.path.join(base_dir, "count_sample.txt")

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("First line of text.\nSecond line here!\nThird line with words.")

    chars, words, lines = file_counts(file_path)

    print(f"File: {file_path}")
    print(f"Characters: {chars}")
    print(f"Words: {words}")
    print(f"Lines: {lines}")

