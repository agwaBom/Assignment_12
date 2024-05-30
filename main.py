from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file: str) -> str:
            file = file.replace('\\', '\\\\')
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file


    # Can this be working?
    processed_file_list = []
    for english_line, german_line in zip(english_file_list, german_file_list):
        english_line = process_file(english_line)
        english_line = process_file(german_line)

        json_string = json.dumps({"English": english_line,"German": germain_line})
        processed_file_list.append(json_string)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as file:
        for line in file_list:
            f.write(line + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = train_file_list_to_json(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
