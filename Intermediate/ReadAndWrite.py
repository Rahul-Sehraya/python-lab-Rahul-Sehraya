import os


def ensure_directory(path: str) -> None:
    """Create directory if it does not already exist."""
    os.makedirs(path, exist_ok=True)


def write_to_file(filename: str, content: str) -> None:
    """Write content to a file using built-in open()."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def read_from_file(filename: str) -> str:
    """Read and return file content using built-in open()."""
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


if __name__ == "__main__":
    target_dir = "FileOperationTxts"
    ensure_directory(target_dir)

    filename = os.path.join(target_dir, "sample.txt")
    message = "Hello, this text will be written to the file using built-in operations."

    write_to_file(filename, message)
    print(f"Written to {filename}: {message}")

    content = read_from_file(filename)
    print(f"Read from {filename}: {content}")


