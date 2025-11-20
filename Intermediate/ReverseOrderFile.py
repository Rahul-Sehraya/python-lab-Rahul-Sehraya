import os


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def print_lines_in_reverse(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip("\n")[::-1])


if __name__ == "__main__":
    base_dir = "FileOperationTxts"
    ensure_directory(base_dir)

    file_path = os.path.join(base_dir, "reverse_lines.txt")
    sample_lines = ["First line", "Second line", "Third line"]

    with open(file_path, "w", encoding="utf-8") as file:
        for line in sample_lines:
            file.write(line + "\n")

    print(f"Reversed lines from {file_path}:")
    print_lines_in_reverse(file_path)

