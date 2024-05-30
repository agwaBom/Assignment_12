from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n')
    #1. 'li' is not defined
    #2. We want to READ the file first, not WRITE

    tmp = [line.strip() for line in lines if line.strip()]
    #3. To delete/prevent empty lines
    return tmp

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')
            #4. Due to Python string issue, we have to add one more '\\' 
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' #5. Template's first word must be 'English'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) #6. Duplicate variable

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
        #7. Wrong order :(
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: 
        #8. We have to WRITE not read
        for file in file_list:
            f.write(file + '\n') #9. Write down contents
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) #10. Wrong function
    
    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) #11. Wrong function

    write_file_list(processed_file_list, path+'concated.json')
