from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    """파일 읽기가 아닌 쓰기로 설정되어 있음, line을 반환하나 line이 정의되어 있지 않음"""
    with open(path, 'r') as f:
        lines = f.readlines()
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
    """German이 중복"""
    template_start = '{\"English\":\"'
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        english_file = process_file(german_file)

        processed_file_list.append(template_mid + english_file + template_start + german_file + template_start)
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    """파일 쓰기 이나 r 로 설정"""
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)#함수 수정

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)#함수 수정

    write_file_list(processed_file_list, path+'concated.json')
