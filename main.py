
import json
import sys
from pathlib import Path

def paragraphs_from_file(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    paragraphs = []
    cur = []
    for ln in lines:
        if ln.strip() == "":
            if cur:
                paragraphs.append(" ".join([l.rstrip() for l in cur]).strip())
                cur = []
        else:
            cur.append(ln)
    if cur:
        paragraphs.append(" ".join([l.rstrip() for l in cur]).strip())
    paragraphs = [p for p in paragraphs if p]
    return paragraphs

def main():
    base = Path(".")
    eng_file = base / "english.txt"
    ger_file = base / "german.txt"

    if not eng_file.exists() or not ger_file.exists():
        print("Required files english.txt and german.txt not found in current directory.", file=sys.stderr)
        sys.exit(1)

    english_pars = paragraphs_from_file(eng_file)
    german_pars = paragraphs_from_file(ger_file)

    pair_count = min(len(english_pars), len(german_pars))
    for i in range(pair_count):
        obj = {"English": english_pars[i], "German": german_pars[i]}
        print(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))

if __name__ == "__main__":
    main()
