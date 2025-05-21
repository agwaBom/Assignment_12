from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # [Start]
    # <----- Before
    # li = open(path, 'w')
    # <----- After
    lines = open(path, 'r').read().split("\n")
    # [End]
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\')
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    # [Start]
    # <----- Before
    # template_start = '{\"German\":\"'
    # template_mid = '\",\"German\":\"'
    # <----- After
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    # [End]
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        # [Start]
        # <----- Before
        # english_file = process_file(english_file)
        # english_file = process_file(german_file)
        # <----- After
        english_file = process_file(english_file)
        german_file = process_file(german_file)
        # [End]

        # [Start]
        # <----- Before
        # processed_file_list.append(template_mid + english_file + template_start + german_file + template_start)
        # <----- After
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
        # [End]
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # [Start]
    # <----- Before
    # with open(path, 'r') as f:
    #     for file in file_list:
    #         f.write('\n')
    # <----- After
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')
    # [End]
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    # [Start]
    # <----- Before
    # english_file_list = path_to_file_list(english_path)
    # german_file_list = train_file_list_to_json(german_path)
    # processed_file_list = path_to_file_list(english_file_list, german_file_list)
    # <----- After
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)
    # [End]

    write_file_list(processed_file_list, path+'concated.json')
