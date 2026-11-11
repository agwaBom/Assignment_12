
from typing import List
import json


def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file."""
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n\r') for line in f]


def train_file_list_to_json(
    english_file_list: List[str],
    german_file_list: List[str]
) -> List[str]:
    """Converts two lists of file paths into a list of JSON strings."""

    if len(english_file_list) != len(german_file_list):
        raise ValueError(
            "English and German file lists must have equal lengths."
        )

    processed_file_list = []

    for english_file, german_file in zip(
        english_file_list, german_file_list
    ):
        data = {
            "English": english_file,
            "German": german_file
        }

        processed_file_list.append(json.dumps(data, ensure_ascii=False))

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line."""
    with open(path, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(file + '\n')


if __name__ == "__main__":
    german_path = './german.txt'
    english_path = './english.txt'
    output_path = './concated.json'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(
        english_file_list,
        german_file_list
    )

    write_file_list(processed_file_list, output_path)
