from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    f = open(path, 'r')
    return f.readlines()

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
        if '/' or '"' in file:
            file = file.replace('"', '\\"')
        file = file.rstrip("\n")
        return file

    # Template for json file
    template_start = '{\"English":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list


def write_string_list(string_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w+') as f:
        for string in string_list:
            f.write(f"{string}\n")
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_string_list(processed_file_list, path+'concated.json')
