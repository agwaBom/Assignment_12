from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as f:
        lines = f.readlines()
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        file = file.replace('\\', '\\\\')
        file = file.replace('/', '\\/')
        file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    processed_file_list = []
    for english_line, german_line in zip(english_file_list, german_file_list):
        english_line = process_file(english_line)
        german_line = process_file(german_line)
        processed_file_list.append(template_start + english_line + template_mid + german_line + template_end)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')

if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')

