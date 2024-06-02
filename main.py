from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # Changed file open mode to 'w' to 'r'
    li = open(path, 'r')
    lines = li.readlines()
    lines = [l.strip() for l in lines]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            # Changed backslashes characters
            file = file.replace('\\', '\\\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    # Fixed the template string
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        # Changed the processing properly
        german_file = process_file(german_file)
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # Changed file open mode to 'r' to 'w
    with open(path, 'w') as f:
        for file in file_list:
            # Changed the variable
            f.write(file+'\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    # Changed the function
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
