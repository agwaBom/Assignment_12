from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file (skipping empty lines)"""
    with open(path, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines


def train_file_list_to_json(english_file_list: List[str], german_file_list: List[str]) -> List[str]:
    """Converts English and German lines into a list of JSON strings."""

    # escape characters
    def process(text):
        text = text.replace('\\', '\\\\')
        text = text.replace('/', '\\/')
        text = text.replace('"', '\\"')
        return text

    template_start = '{"English":"'
    template_mid = '","German":"'
    template_end = '"}'

    result = []
    for eng, ger in zip(english_file_list, german_file_list):
        eng = process(eng)
        ger = process(ger)
        result.append(template_start + eng + template_mid + ger + template_end)

    return result


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes each JSON item on a new line."""
    with open(path, 'w') as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    path = './'

    english_file_list = path_to_file_list(path + 'english.txt')
    german_file_list = path_to_file_list(path + 'german.txt')

    json_list = train_file_list_to_json(english_file_list, german_file_list)
    write_file_list(json_list, path + 'concated.json')
