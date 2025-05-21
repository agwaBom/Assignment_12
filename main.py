from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    def process_file(line: str) -> str:
        # Escape characters that might interfere with JSON format
        line = line.replace('\\', '\\\\')
        line = line.replace('/', '\\/')
        line = line.replace('"', '\\"')
        return line

    processed_file_list = []
    for english_line, german_line in zip(english_file_list, german_file_list):
        english_line = process_file(english_line)
        german_line = process_file(german_line)
        json_line = f'{{"English":"{english_line}", "German":"{german_line}"}}'
        processed_file_list.append(json_line)

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
   with open(path, 'w', encoding='utf-8') as f:
        for line in file_list:
            f.write(line + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = path + 'german.txt'
    english_path = path + 'english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(processed_file_list, path + 'concated.json')
