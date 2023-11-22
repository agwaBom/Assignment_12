from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # changed multiple things inside.
    # li -> lines
    # w -> r
    # added readlines() so that actual contents can be returned
    with open(path, 'r') as file:
        lines = file.readlines()
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
    # changed so that template_start will be English not German
    template_start = '{\"English\":\"'
    template_mid = ',\"German\":\"'
    template_end = '\"}'
    
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        # changed so that german content will be stored in german_file var
        german_file = process_file(german_file)

        # changed the order so it will be start-mid-end
        processed_file_list.append(template_start + english_file.strip() + template_mid + german_file.strip() + template_end)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    #  r -> w
    with open(path, 'w') as f:
        for file in file_list:
            # added file+ to actually write contents
            f.write(file+'\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    # wrong function call
    german_file_list = path_to_file_list(german_path)

    # wrong function call
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, path+'concated.json')
