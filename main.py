from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # 쓰기모드 -> 읽기모드로 수정
    with open(path, 'r') as f:
        lines = f.readlines()
    # lines 변수 올바르게 정의
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        ## 불필요한 연산 수행 수정
        file = file.replace('\\', '\\\\')
        file = file.replace('/', '\\/')
        file = file.replace('"', '\\"')
        return file.strip()

    # Template for json file
    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        # english -> german으로 수정, 독일어 파일에 대해서도 호출
        german_file = process_file(german_file)

        # 누락된 english 키 추가, template_start~end 위치 수정
        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)
    return processed_file_list

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    # 읽기모드 -> 쓰기모드
    with open(path, 'w') as f:
        for file in file_list:
            f.write(file + '\n')
            
if __name__ == "__main__":
    english_path = './english.txt'
    german_path = './german.txt'
    output_path = './concated.json'

    # 리스트 전달 시 올바른 인수 전달 수정
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, output_path)
