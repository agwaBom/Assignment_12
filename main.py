"""Pair English and German text lines as JSON records."""

import json
from typing import List


def path_to_file_list(path: str) -> List[str]:
    """Read the lines of a UTF-8 text file without changing the file."""
    with open(path, 'r', encoding='utf-8') as input_file:
        return input_file.read().splitlines()


def train_file_list_to_json(
    english_file_list: List[str], german_file_list: List[str]
) -> List[str]:
    """Encode corresponding English and German lines as JSON strings."""
    if len(english_file_list) != len(german_file_list):
        raise ValueError('English and German files must have the same number of lines')

    return [
        json.dumps({'English': english, 'German': german}, ensure_ascii=False)
        for english, german in zip(english_file_list, german_file_list)
    ]


def write_file_list(file_list: List[str], path: str) -> None:
    """Write each string to a UTF-8 file on its own line."""
    with open(path, 'w', encoding='utf-8') as output_file:
        for item in file_list:
            output_file.write(item + '\n')


if __name__ == '__main__':
    english_file_list = path_to_file_list('./english.txt')
    german_file_list = path_to_file_list('./german.txt')
    processed_file_list = train_file_list_to_json(
        english_file_list, german_file_list
    )
    write_file_list(processed_file_list, './concated.json')
