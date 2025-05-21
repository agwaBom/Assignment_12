import json
from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of non-empty lines"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return [line.strip() for line in lines if line.strip()]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of English and German lines into a list of JSON strings"""
    result = []
    for en, de in zip(english_file_list, german_file_list):
        en_processed = en.replace('\\', '\\\\').replace('"', '\\"').replace('/', '\\/')
        de_processed = de.replace('\\', '\\\\').replace('"', '\\"').replace('/', '\\/')
        result.append(json.dumps({"English": en_processed, "German": de_processed}))
    return result

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w', encoding='utf-8') as f:
        for line in file_list:
            f.write(line + '\n')

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'

    english_lines = path_to_file_list(english_path)
    german_lines = path_to_file_list(german_path)

    concated_json_lines = train_file_list_to_json(english_lines, german_lines)

    write_file_list(concated_json_lines, './concated.json')
