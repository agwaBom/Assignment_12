from typing import List


def path_to_file_list(path: str) -> List[str]:
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"오류: {path} 파일을 찾을 수 없습니다.")
        return []
    except Exception as e:
        print(f"오류: {path} 파일을 읽는 중 오류 발생 - {e}")
        return []


def train_file_list_to_json(
    english_file_list: List[str], german_file_list: List[str]
) -> List[str]:
    def process_file(text_line: str) -> str:
        processed_line = text_line.replace("\\", "\\\\")
        processed_line = processed_line.replace('"', '\\"')
        return processed_line

    processed_file_list = []
    min_len = min(len(english_file_list), len(german_file_list))
    if len(english_file_list) != len(german_file_list):
        print(
            f"경고: 영어와 독일어 파일의 줄 수가 다릅니다. 짧은 쪽({min_len}개) 기준으로 처리합니다."
        )

    for i in range(min_len):
        english_line = english_file_list[i]
        german_line = german_file_list[i]

        processed_english_line = process_file(english_line)
        processed_german_line = process_file(german_line)

        json_string = f'{{"English":"{processed_english_line}","German":"{processed_german_line}"}}'
        processed_file_list.append(json_string)

    return processed_file_list


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    try:
        with open(path, "w", encoding="utf-8") as f:
            for file_content_line in file_list:
                f.write(file_content_line + "\n")
        print(f"성공: {path} 파일에 내용을 작성했습니다.")
    except Exception as e:
        print(f"오류: {path} 파일에 쓰는 중 오류 발생 - {e}")


if __name__ == "__main__":
    current_path = "./"
    german_path = current_path + "german.txt"
    english_path = current_path + "english.txt"
    output_json_path = current_path + "concated.json"
    english_lines = path_to_file_list(english_path)
    german_lines = path_to_file_list(german_path)

    if not english_lines or not german_lines:
        print("오류: 입력 파일 중 하나 이상을 읽는데 실패하여 처리를 중단합니다.")
    else:
        processed_json_list = train_file_list_to_json(english_lines, german_lines)
        write_file_list(processed_json_list, output_json_path)
