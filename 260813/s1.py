#
# 파일 다루기 - 경로 ~ csv
#

# 필요한 도구 가져오기
# pathlib : 경로를 다루는 도구(파이썬 기본 내장)
# csv : csv파일을 다루는 도구
# os : 운영체제 관련 도구
# 이 셋은 설치가 필요 없다. import만 하면 바로 가능

from pathlib import Path
import csv
import os


# 경로란
# 파일이 어디 있는지 알려주는 주소
# Users/jones/Documents/보고서.txt
# 드라이브      폴더들       파일명

# 두 가지 종류
# 1. 절대경로 - 처음부터 끝까지 다 적기
# 장점 - (어디든 같은 파일, 정확성 good) / 단점 - (다른 컴퓨터인 불가능, 확장성 아쉽)
# 2. 상대경로 - 지금 있는 위치 기준
# 장점 - (짧고 편함, 확장성 좋음) / 단점 - (지금 위치가 어딘지에 따라 달라짐)


# 대부분 상대경로 사용
# current working directory >> cwd

print("현재 작업 폴더 : ", os.getcwd())
print("이 파일의 위치 : ", Path(__file__).parent)
# os.getcwd() - 현재 작업 폴더
# __file__ - 지금 실행중인 파일 경로
#            파이썬이 자동으로 만들어주는 변수
#            앞 뒤에 언더바 2개씩 붙어있으면 '특별한 변수'

# Path(__file__) - 그 경로를 Path 객체로 만든것
#                  문자열보다 다루기 편함

# .parent - 그 파일이 들어 있는 폴더 (부모폴더, 상위폴더)


# 해결책 - 항상 '이 파일 기준'으로 경로를 잡는다

# 중요(***)
# BASE = Path(__file__).parent  이 .py 파일이 있는 폴더
# DATA = BASE / 'data'          그 안의 data 폴더
# DATA.mkdir(exist_ok=True)     파일 만드는데 없으면 만들어
# 파일 다루는 코드 시작은 이렇게 하자.

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

print("기준 폴더 : ", BASE)
print("데이터 폴더 : ", DATA)
print("이제 어디서 실행하든 항상 같은 곳을 가리킨다.")


# mkdir 옵션 설명
# DATA.mkdir()
#   폴더를 만든다. 이미 있으면 FileExistsError 발생
#
# exist_ok=True를 넣어야 있어도 넘어감
#
# DATA.mkdir(parents=True, exist_ok=True)
#   중간 폴더까지 다 만든다.
#   a/b/c 만들 때 a, b도 없으면 함께 생성


## 파일 보면서 정리

# glob()를 통해 원하는 파일만
# * 아무 글자 0개 이상
# ? 아무 글자 하나

#
# 파일 쓰기 - open & with
#

#   with open(경로, 모드, encoding="utf-8") as f:
#       f.write("내용")
#
# r 읽기(read)      파일 읽기(기본값)
# w 쓰기(write)     *파일이 있으면 내용 전부 지우고* 새로 씀
# a 추가(append)    기존 내용 뒤에 이어 붙이기

# encoding='utf-8'
# 컴퓨터는 글자를 숫자로 저장
# 변환 규칙이 인코딩

# utf-8     전 세계 표준. 한글도 잘 됨
# cp949     옛날 윈도우, 한국어 방식


# with 사용 이유

# with를 쓰면 블록이 끝나면 파일이 자동으로 닫힘
# 에러가 나도 닫힘

# with 없이 쓰면 - 권장하지 않음
#   f = open(경로, 'w', encoding='utf-8')
#   f.write('내용')
#   f.close() <<< 이거 까먹지 마

# as f 의미
#   열린 파일 f 라는 이름으로 부르겠다.
#   f 대신 다른 이름을 써도 되지만 관례상 f를 많이 쓴다.

memo = DATA / "memo.txt"

with open(memo, "w", encoding="utf-8") as f:
    f.write("첫 번째 줄입니다\n")  # \n 을 직접 넣어야 줄이 바뀜
    f.write("두 번째 줄입니다\n")
    f.write("세 번째 줄입니다\n")

with open(memo, "r", encoding="utf-8") as f:
    print(f.read())


#
# ㅇ
#


# 없는 파일을 열려고 하면 FileNotFoundError가 난다
# 대응방법
ghost = DATA / "없는 파일.txt"

# 방법 1 확인하기
if ghost.exists():
    with open(ghost, "r", encoding="utf-8") as f:
        print(f.read())
else:
    print(f"{ghost.name}은(는) 없습니다.")

# 방법 2 try / except
try:
    with open(ghost, "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print(f"{ghost.name}을(를) 찾을 수 없습니다.")

# 보통 방법 2를 권장
# 확인하고 여는 순간 사이 파일이 사라질 수 있음
# 권한 문제 등 exists()로 못잡는 상황도 있음


# 안전하게 읽는 함수
def read_text(path, default=""):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default


def read_lines(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for line in f:
                result.append(line.strip())
            return result
    except FileNotFoundError:
        return []


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")
    return path


#
# ㅇ
#
print("\n" + "=" * 60)
print(" 3-1. 실습용 CSV 만들기")
print("=" * 60)

employees_file = DATA / "employees.csv"

# 2부에서 배운 파일 쓰기로 CSV 를 만들어 봅니다
rows = [
    "이름,부서,연봉,입사년도",
    "김철수,영업,4500,2019",
    "이영희,개발,5200,2020",
    "박민수,개발,4800,2021",
    "최지은,영업,5100,2018",
    "정하늘,인사,4200,2022",
]

with open(employees_file, "w", encoding="utf-8") as f:
    for row in rows:
        f.write(row + "\n")

print(f"  '{employees_file.name}' 생성 완료")


# !r은 값을 따옴표까지 포함
# '4500'처럼 보이면 문자열 아니면 숫자
