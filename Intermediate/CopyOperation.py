import os


def ensure_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def copy_file(src: str, dest: str) -> None:
    with open(src, "r", encoding="utf-8") as source, open(
        dest, "w", encoding="utf-8"
    ) as target:
        target.write(source.read())


if __name__ == "__main__":
    base_dir = "FileOperationTxts"
    ensure_directory(base_dir)

    source_file = os.path.join(base_dir, "source.txt")
    destination_file = os.path.join(base_dir, "destination.txt")

    with open(source_file, "w", encoding="utf-8") as file:
        file.write("This text will be copied to another file using built-in file handling.")

    copy_file(source_file, destination_file)
    print(f"Copied contents from {source_file} to {destination_file}")

