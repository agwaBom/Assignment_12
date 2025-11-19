from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n') # 1. 변수명 동일하게. 2. 'w' -> 'r'로 바꾸어 읽기 모드. 3. 줄바꿈을 기준으로 쪼개기.
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\') # \\는 한개만 표현되기때문에, 2개를 표현하기 위해 \\\\로 교체. 
        if '/' in file or '"' in file: # if 뒤에 '/'만 있다면 항상 true이기 때문에 in file을 추가하였다.
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"' # German -> English로 수정.
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file) # english_file -> german_file로 변경.

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
        # 순서 조합이 잘못되었음.
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f: # 쓰기 모드를 실행해야하므로 r -> w로 변경.
        for file in file_list:
            f.write(file + '\n') # 파일 내용도 작성해야함.
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path) # 독일어 파일을 읽어와야하므로 path_to_file_list를 사용.

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list) # 두 리스트를 합쳐야하므로 train_file_list_to_json 사용.

    write_file_list(processed_file_list, path+'concated.json')
