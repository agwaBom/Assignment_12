from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""

    """
    'li' is a target to be returned, but the name is different from the return variable. So, the name should be the same.
    And, it set the mode to 'w' when a file is opened, which is write mode. It must changed to read mode('r').
    """
    lines = open(path, 'r') # changed
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
    """
    have to start with a 'English'
    """
    template_start = '{\"English\":\"' # changed
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        """
        Since the variable name overlaps with 'english_file', change it to 'german_file'.
        """
        german_file = process_file(german_file) # changed

        """
        Since the order of the templates is different, change it to the correct order.
        """
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end) # changed
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""

    """
    When writing a file, it should be set to write mode, but since it is read mode, it is changed.
    """
    with open(path, 'w') as f: # changed
        for file in file_list:
            f.write('\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)

    """
    'path_to_file_list' function converts a file path into a file list and has one parameter.
    'train_file_list_to_json' functio converts a file list into a json file format and has two file parameters.
    However, since the function of the code below was not used properly, it is corrected appropriately.
    """
    german_file_list = path_to_file_list(german_path) # changed

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) # changed

    write_file_list(processed_file_list, path+'concated.json')
