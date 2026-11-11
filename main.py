
from typing import List
import json


def path_to_file_list(path: str) -> List[str]:
    """Read a file and return its lines."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\r\n") for line in f]


def train_file_list_to_json(
    english_file_list: List[str],
    german_file_list: List[str]
) -> List[str]:
    """Convert English and German lines into JSON strings."""
    processed_file_list = []

    for english, german in zip(english_file_list, german_file_list):
        data = {"English": english, "German": german}
        processed_file_list.append(
            json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        )

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Write each string on a separate line."""
    with open(path, "w", encoding="utf-8") as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    english_path = "./english.txt"
    german_path = "./german.txt"

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(
        english_file_list, german_file_list
    )

    write_file_list(processed_file_list, "./concated.json")
