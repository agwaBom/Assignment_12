import json

def load_file_lines(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

def escape_special_chars(text):
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('/', '\\/')

def main():
    english_lines = load_file_lines("english.txt")
    german_lines = load_file_lines("german.txt")

    if len(english_lines) != len(german_lines):
        print("❗ 영어와 독일어 줄 수가 다릅니다.")
        return

    merged = []
    for eng, ger in zip(english_lines, german_lines):
        merged.append({
            "English": escape_special_chars(eng),
            "German": escape_special_chars(ger)
        })

    with open("concated.json", "w", encoding='utf-8') as f:
        for pair in merged:
            json.dump(pair, f, ensure_ascii=False)
            f.write("\n")

if __name__ == "__main__":
    main()
