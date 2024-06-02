from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[dict]:
    """Converts two lists of file paths into a list of json objects"""
    processed_file_list = []
    for english_word, german_word in zip(english_file_list, german_file_list):
        processed_file_list.append({"English": english_word, "German": german_word})
    return processed_file_list

def write_file_list(file_list: List[dict], path: str) -> None:
    """Writes a list of dictionaries to a json file"""
    with open(path, 'w') as f:
        json.dump(file_list, f, ensure_ascii=False, indent=4)
        
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path + 'concated.json')
