from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as f:
        return f.readlines()

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of strings into a list of JSON strings"""
    def process_file(file):
        file = file.replace('\\', '\\\\').replace('"', '\\"')
        return file

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        eng = process_file(english_file.strip())
        ger = process_file(german_file.strip())
        json_str = f'{{"English":"{eng}","German":"{ger}"}}'
        processed_file_list.append(json_str)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, output_path)