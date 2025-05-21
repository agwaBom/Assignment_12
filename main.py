from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file lines into a list of JSON strings"""
    def process_line(line: str) -> str:
        line = line.replace('\\', '\\\\')  # Escape backslashes
        line = line.replace('/', '\\/')    # Escape forward slashes
        line = line.replace('"', '\\"')    # Escape quotes
        return line

    result = []
    for eng, ger in zip(english_file_list, german_file_list):
        eng = process_line(eng)
        ger = process_line(ger)
        result.append(f'{{"English":"{eng}","German":"{ger}"}}')
    return result

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file in JSON array format"""
    with open(path, 'w', encoding='utf-8') as f:
        f.write('[\n')
        for i, line in enumerate(file_list):
            f.write(line)
            if i != len(file_list) - 1:
                f.write(',\n')
            else:
                f.write('\n')
        f.write(']')

if __name__ == "__main__":
    german_path = './german.txt'
    english_path = './english.txt'
    output_path = './concated.json'

    english_lines = path_to_file_list(english_path)
    german_lines = path_to_file_list(german_path)

    processed_lines = train_file_list_to_json(english_lines, german_lines)

    write_file_list(processed_lines, output_path)
