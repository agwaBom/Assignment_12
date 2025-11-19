from typing import List
import json


def path_to_file_list(path: str) -> List[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    if len(english_file_list) != len(german_file_list):
        raise ValueError("English and German files must have the same number of lines.")
    return [
        json.dumps({"English": english, "German": german}, ensure_ascii=False)
        for english, german in zip(english_file_list, german_file_list)
    ]


def write_file_list(file_list: List[str], path: str) -> None:
    with open(path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(file_list))


if __name__ == "__main__":
    german_path = './german.txt'
    english_path = './english.txt'
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(processed_file_list, './concated.json')
