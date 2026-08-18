from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "test_data"
DATA.mkdir(exist_ok=True)


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    return path


top = DATA / "top100.txt"

lst = []
while True:
    a = input("리스트를 입력해 주세요 (end 입력 시 종료) : ")
    if a == "end":
        break
    else:
        lst.append(a)
write_lines(top, lst)
