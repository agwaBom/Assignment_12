from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, 'r') as file:  #쓰는게 아니라 읽어야 하는 코드.
        lines = file.readlines()
    return [line.strip() for line in lines]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts two lists of file paths into a list of json strings"""
    # Preprocess unwanted characters
    def process_file(file):
        if '\\' in file:
            file = file.replace('\\', '\\\\')   #똑같은 걸로 replace를 하면 의미가 없는 코드. 
        if '/' or '"' in file:
            file = file.replace('/', '\\/')
            file = file.replace('"', '\\"')
        return file

    # Template for json file
    template_start = '{\"English\":\"'    #English -> German이므로 German을 English로 교체. 
    template_mid = '\",\"German\":\"'
    template_end = '\"}'

    # Can this be working?
    processed_file_list = []
    for english_file, german_file in zip(english_file_list, german_file_list):
        english_file = process_file(english_file)
        german_file = process_file(german_file)

        processed_file_list.append(template_start + english_file + template_mid + german_file + template_end)   #순서 알맞게 변경. mid start start가 아닌 start mid end
    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, 'w') as f:  # 쓰기 코드이기 때문에 쓰기로 변경.
        for file in file_list:
            f.write(file+'\n')
            
if __name__ == "__main__":
    path = './'
    german_path = './german.txt'
    english_path = './english.txt'

    english_file_list = path_to_file_list(english_path)  
    german_file_list = path_to_file_list(german_path)  #먼저 german 파일을 읽어 list로 만드는 코드가 필요
    processed_file_list = train_file_list_to_json(english_file_list,german_file_list)  #그 후, 읽어 list로 만드는 코드가 아닌 두개의 리스트를 json으로 변환하는 코드 필요. 

    write_file_list(processed_file_list, path+'concated.json')
