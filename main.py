from typing import List

def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    with open(path, "r", encoding="utf-8") as f:
        lines = [line.rstrip("\n") for line in f]
    return lines


def escape_for_json(text: str) -> str:
    """Escapes characters that need to be escaped in JSON."""
    text = text.replace("\\", "\\\\")   # \  -> \\
    text = text.replace("/", "\\/")     # /  -> \/
    text = text.replace('"', '\\"')     # "  -> \"
    return text


def train_file_list_to_json(english_file_list: List[str],
                            german_file_list: List[str]) -> List[str]:
    """Converts two lists of sentences into a list of JSON strings."""
    template = '{{"English":"{}","German":"{}"}}'
    processed_file_list = []

    for english_line, german_line in zip(english_file_list, german_file_list):
        eng = escape_for_json(english_line)
        ger = escape_for_json(german_line)
        processed_file_list.append(template.format(eng, ger))

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line."""
    with open(path, "w", encoding="utf-8") as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    german_path = "./german.txt"
    english_path = "./english.txt"
    output_path = "./concated.json"

    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    processed_file_list = train_file_list_to_json(english_file_list, german_file_list)

    write_file_list(processed_file_list, output_path)
