from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # original code opened with 'w' and returned undefined 'lines'
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""

    # very small cleanup of the original process_file
    def process_file(file):
        file = file.replace('\\', '\\\\')
        file = file.replace('/', '\\/')
        file = file.replace('"', '\\"')
        return file

    processed_file_list = []

    for english_file, german_file in zip(english_file_list, german_file_list):
        eng = process_file(english_file)
        ger = process_file(german_file)

        # instead of manually constructing JSON, use json.dumps but keep your structure
        json_obj = {"English": eng, "German": ger}
        processed_file_list.append(json.dumps(json_obj, ensure_ascii=False))

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # original opened in 'r' and never wrote lines
    with open(path, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(file + '\n')

            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # original code used wrong variables / wrong calls
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path + 'concated.json')

