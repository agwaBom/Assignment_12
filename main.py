import json
from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of trimmed lines."""
    with open(path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts English/German sentence lists into JSON lines."""
    json_lines = []

    for eng, ger in zip(english_file_list, german_file_list):
        json_obj = {"English": eng, "German": ger}
        json_lines.append(json.dumps(json_obj, ensure_ascii=False))
    
    return json_lines

def write_file_list(file_list: List[str], path: str) -> None:
    """Writes each JSON string on its own line."""
    with open(path, "w", encoding="utf-8") as f:
        for line in file_list:
            f.write(line + "\n")

if __name__ == "__main__":
    english_file_list = path_to_file_list("english.txt")
    german_file_list = path_to_file_list("german.txt")

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, "concated.json")
