import os
import string
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "FileOperationTxts"
DICTIONARY_FILE = DATA_DIR / "dictionary_words.txt"


def load_dictionary(path: Path) -> set[str]:
    try:
        with open(path, "r", encoding="utf-8") as dictionary:
            return {
                word.strip().lower()
                for word in dictionary
                if word.strip() and not word.startswith("#")
            }
    except OSError as error:
        print(f"Unable to read dictionary file '{path}': {error}")
        sys.exit(1)


def find_misspellings(dictionary: set[str], target_path: Path) -> dict[str, set[int]]:
    punctuation = string.punctuation + "“”‘’"
    misspellings: dict[str, set[int]] = {}

    try:
        with open(target_path, "r", encoding="utf-8") as target_file:
            for line_number, line in enumerate(target_file, start=1):
                for raw_word in line.split():
                    cleaned = raw_word.strip(punctuation).lower()
                    if not cleaned or not cleaned.isalpha():
                        continue
                    if cleaned not in dictionary:
                        misspellings.setdefault(cleaned, set()).add(line_number)
    except OSError as error:
        print(f"Unable to open '{target_path}': {error}")
        sys.exit(1)

    return misspellings


def main():
    if len(sys.argv) < 2:
        print("Usage: python SpellChecker.py <file_to_check>")
        sys.exit(1)

    target_arg = Path(sys.argv[1])
    if not target_arg.is_file():
        candidate = DATA_DIR / target_arg.name
        if candidate.is_file():
            target_arg = candidate
        else:
            print(f"File '{target_arg}' does not exist.")
            sys.exit(1)

    dictionary = load_dictionary(DICTIONARY_FILE)
    misspelled_words = find_misspellings(dictionary, target_arg)

    if not misspelled_words:
        print("No spelling mistakes found.")
    else:
        print("Potential spelling mistakes:")
        for word in sorted(misspelled_words):
            lines = ", ".join(str(num) for num in sorted(misspelled_words[word]))
            print(f"{word} (line {lines})")


if __name__ == "__main__":
    main()

