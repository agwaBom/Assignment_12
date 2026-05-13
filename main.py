from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""

    # fixed code for reading file
    lines = open(path, 'r').read().split('\n')
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            """fixed replace string"""
            file = file.replace('\\', '\\\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    # fixed start string
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        # fixed from english_file to german_file
        german_file = process_file(german_file)
        
        #fixed append order
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # fixed open file from read to write
    with open(path, 'w') as f:
        for file in file_list:
            # added file
            f.write(file + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    # changed function from train_file_list_to_json to path_to_file_list
    german_file_list = path_to_file_list(german_path)

    # changed function from path_to_file_list to train_file_list_to_json
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
