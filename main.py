from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[dict]:
    """Converts two lists of file paths into a list of json strings"""
    if len(english_file_list) != len(german_file_list):
        raise ValueError("The number of lines in english.txt and german.txt do not match.")
    
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        json_obj = {"English": english_file, "German": german_file}
        processed_file_list.append(json_obj)
    return processed_file_list

def write_file_list(file_list: List[dict], path: str) -> None:
    """Writes a list of json objects to a file"""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_list, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    german_path = './german.txt'
    english_path = './english.txt'
    
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, './concated.json')
