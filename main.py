import json

def main():
    with open('english.txt', 'r', encoding='utf-8') as eng_file:
        eng_lines = eng_file.readlines()
        
    with open('german.txt', 'r', encoding='utf-8') as ger_file:
        ger_lines = ger_file.readlines()

    result = []
    
    for eng, ger in zip(eng_lines, ger_lines):
        result.append({
            "English": eng.strip(),
            "German": ger.strip()
        })

    with open('concated.json', 'w', encoding='utf-8') as json_file:
        for item in result:
            json_file.write(json.dumps(item) + '\n')

if __name__ == "__main__":
    main()