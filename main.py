from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n') # 변수명을 lines로, read방식으로 읽고, \n기준으로 split해야함
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\') # \\를 \\\\로 replace해야함
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' # German이 아니라 English임임
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # 변수명이 german_file이여야 함

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end) # append 순서 잘못됨
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: # write를 해야함
        for file in file_list:
            f.write(file + '\n') # file변수와 합쳐서 출력을 해야함
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) # path_to_file_list함수를 사용해야함

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) #train_file_list_to_json함수를 사용해야함

    write_file_list(processed_file_list, path+'concated.json')
