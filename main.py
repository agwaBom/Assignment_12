from typing import List
import json


def path_to_file_list(path: str) -> List[str]:
    """Reads a file and returns a list of lines in the file"""
    # 파일을 읽기 모드로 열고, 줄 끝 개행(\n)을 제거해서 리스트로 반환
    with open(path, "r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def train_file_list_to_json(english_file_list: List[str],
                            german_file_list: List[str]) -> List[str]:
    """Converts two lists of sentences into a list of json strings"""
    json_lines: List[str] = []

    for en, de in zip(english_file_list, german_file_list):
        data = {"English": en, "German": de}
        # json.dumps를 사용해서 안전하게 JSON 문자열 생성
        json_lines.append(json.dumps(data, ensure_ascii=False))

    return json_lines


def write_file_list(file_list: List[str], path: str) -> None:
    """Writes a list of strings to a file, each string on a new line"""
    with open(path, "w", encoding="utf-8") as f:
        for line in file_list:
            f.write(line + "\n")


if __name__ == "__main__":
    base_path = "./"
    german_path = base_path + "german.txt"
    english_path = base_path + "english.txt"

    # 1) 영어/독일어 파일에서 문장 리스트 읽기
    english_file_list = path_to_file_list(english_path)
    german_file_list = path_to_file_list(german_path)

    # 2) JSON 문자열 리스트 만들기
    processed_file_list = train_file_list_to_json(
        english_file_list, german_file_list
    )

    # 3) concated.json에 저장
    write_file_list(processed_file_list, base_path + "concated.json")
