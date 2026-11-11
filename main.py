import json
from typing import List


def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()


def train_file_list_to_json(
    english_file_list: List[str], german_file_list: List[str]
) -> List[str]:
    processed_file_list = []

    for english_line, german_line in zip(english_file_list, german_file_list):
        entry = {"English": english_line, "German": german_line}
        processed_file_list.append(
            json.dumps(entry, ensure_ascii=False, separators=(',', ':'))
        )

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        for line in file_list:
            f.write(line + '\n')


if __name__ == "__main__":
    english_file_list = path_to_file_list('./english.txt')
    german_file_list = path_to_file_list('./german.txt')

    processed_file_list = train_file_list_to_json(
        english_file_list, german_file_list
    )

    write_file_list(processed_file_list, './concated.json')
