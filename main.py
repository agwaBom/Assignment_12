import json
from typing import List

def path_to_file_list(path: str) -> List[str]:

    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[dict]:

    json_list = []
    min_len = min(len(english_file_list), len(german_file_list))
    for i in range(min_len):
        json_list.append({
            "English": english_file_list[i],
            "German": german_file_list[i]
        })
    return json_list

def write_file_list(json_list: List[dict], path: str) -> None:

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_list, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, output_path)
