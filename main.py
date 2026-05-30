from typing import List
import json

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    lines = open(path, 'r').read().split('\n')
    lines = [line for line in lines if line.strip() != '']
    return lines

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]):
    """Reads english and german file lists and returns a list of json objects"""
    json_list = []
    for eng, ger in zip(english_file_list, german_file_list):
        json_list.append({"English": eng, "German": ger})
    return json_list

def save_json(json_list, path: str):
    """Saves a list of json objects to a file"""
    with open(path, 'w') as f:
        for json_object in json_list:
            f.write(json.dumps(json_object, ensure_ascii=False) + '\n')

if __name__ == '__main__':
    english_file_list = path_to_file_list('english.txt')
    german_file_list = path_to_file_list('german.txt')
    json_list = train_file_list_to_json(english_file_list, german_file_list)
    save_json(json_list, 'concated.json')
