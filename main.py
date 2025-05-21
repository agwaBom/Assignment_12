from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file lines into a list of JSON strings"""
    def process_line(line: str) -> str:
        line = line.replace('\\', '\\\\')
        line = line.replace('/', '\\/')
        line = line.replace('"', '\\"')
        return line

    result = []
    for en, de in zip(english_file_list, german_file_list):
        en = process_line(en)
        de = process_line(de)
        json_line = f'{{"English":"{en}","German":"{de}"}}'
        result.append(json_line)
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

    processed = train_file_list_to_json(english_lines, german_lines)

    write_file_list(processed, 'concated.json')
