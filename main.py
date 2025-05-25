import json
from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of stripped lines"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def train_file_list_to_json(english_lines: List[str], german_lines: List[str]) -> List[dict]:
    """Converts two lists of sentences into a list of dictionaries"""
    result = []
    for en, de in zip(english_lines, german_lines):
        result.append({
            "English": en,
            "German": de
        })
    return result

def write_file_list(json_data: List[dict], path: str) -> None:
    """Writes a list of dictionaries to a JSON file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_lines = path_to_file_list(english_path)
    german_lines = path_to_file_list(german_path)

    processed_data = train_file_list_to_json(english_lines, german_lines)

    write_file_list(processed_data, output_path)
