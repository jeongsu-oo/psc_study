"""
============================================================
 my_tools.py  -  직접 만든 모듈
============================================================

 [이 파일은 뭔가요?]
   지금까지 만든 유용한 함수들을 한곳에 모아둔 파일입니다.
   '실행하는 파일'이 아니라 '가져다 쓰는 파일' 입니다.

   04_import와_pip.py 에서 이렇게 씁니다.

       import my_tools
       my_tools.to_int("100")

 [왜 이렇게 나누나요?]
   같은 함수를 프로젝트마다 복사해서 쓰면
   나중에 고칠 때 모든 파일을 다 찾아 고쳐야 합니다.

   한 파일에 모아두면
     - 여러 프로젝트에서 재사용할 수 있고
     - 고칠 곳이 한 군데뿐이고
     - 다른 사람에게 파일 하나만 주면 됩니다

   pandas, numpy 도 똑같은 원리로 만들어져 있습니다.
     누군가 유용한 함수를 모아 배포한 것뿐입니다.

------------------------------------------------------------
 [파일 구성]
   1. 숫자 변환 도구
   2. 통계 도구
   3. 파일/CSV 도구
   4. 출력 꾸미기 도구
   5. 자체 테스트 (맨 아래)
============================================================
"""

from pathlib import Path
import csv


# ============================================================
#  모듈 정보
# ============================================================
# 모듈에도 변수를 둘 수 있습니다.
# 대문자로 쓰면 "바뀌지 않는 값(상수)" 이라는 뜻입니다.

VERSION = "1.0"
AUTHOR = "우리 팀"


# ============================================================
#  1. 숫자 변환 도구
# ============================================================


def to_int(value, default=0):
    """문자열을 정수로 바꾼다. 실패하면 default 를 돌려준다.

    사용 예)
        to_int("100")      -> 100
        to_int(" 100 ")    -> 100    (공백 자동 제거)
        to_int("백")        -> 0      (실패 시 기본값)
        to_int("백", -1)    -> -1     (기본값 직접 지정)

    CSV 의 값은 전부 문자열이라 이 함수를 정말 자주 씁니다.
    """
    try:
        return int(str(value).strip())
    except (ValueError, TypeError):
        return default


def to_float(value, default=0.0):
    """문자열을 실수로 바꾼다. 실패하면 default 를 돌려준다.

    사용 예)
        to_float("3.14")   -> 3.14
        to_float("3.14점") -> 0.0
    """
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default


def clean_number(value, default=None):
    """단위와 쉼표를 제거하고 숫자만 뽑아낸다.

    사용 예)
        clean_number("4,500원")  -> 4500
        clean_number(" 30개 ")   -> 30
        clean_number("없음")      -> None

    실무 데이터에는 '4,500원' 같은 값이 흔합니다.
    to_int 로는 실패하지만 이 함수는 살려냅니다.
    """
    if value is None:
        return default

    text = str(value).strip()

    # 제거할 문자들
    for remove in [",", "원", "만원", "개", "명", "건", "%", " "]:
        text = text.replace(remove, "")

    if text == "":
        return default

    try:
        return int(text)
    except ValueError:
        return default


# ============================================================
#  2. 통계 도구
# ============================================================


def get_average(numbers, digits=1):
    """숫자 리스트의 평균. 빈 리스트면 0.

    numbers : 숫자 리스트
    digits  : 소수점 아래 몇 자리까지 (기본 1)

    사용 예)
        get_average([90, 85, 100])     -> 91.7
        get_average([90, 85, 100], 0)  -> 92.0
        get_average([])                -> 0
    """
    if not numbers:  # 빈 리스트면 0으로 나누게 되므로 미리 방어
        return 0
    return round(sum(numbers) / len(numbers), digits)


def find_max(numbers, default=None):
    """가장 큰 값. 빈 리스트면 default.

    파이썬의 max() 와 같지만, 빈 리스트에서 에러가 안 납니다.
    """
    if not numbers:
        return default
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


def find_min(numbers, default=None):
    """가장 작은 값. 빈 리스트면 default."""
    if not numbers:
        return default
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest


def sum_by(rows, group_key, value_key):
    """딕셔너리 리스트를 그룹별로 합산한다.

    rows      : 딕셔너리들이 담긴 리스트
    group_key : 묶을 기준이 되는 키   (예: "부서")
    value_key : 합산할 값의 키        (예: "연봉")

    사용 예)
        data = [{"부서":"영업","연봉":100}, {"부서":"영업","연봉":200}]
        sum_by(data, "부서", "연봉")   ->  {"영업": 300}

    pandas 의 groupby().sum() 이 하는 일을 손으로 만든 것입니다.
    """
    result = {}
    for row in rows:
        key = row[group_key]
        value = row[value_key]
        result[key] = result.get(key, 0) + value
    return result


def count_by(rows, group_key):
    """그룹별 개수를 센다.

    사용 예)
        count_by(data, "부서")   ->  {"영업": 2, "개발": 1}
    """
    result = {}
    for row in rows:
        key = row[group_key]
        result[key] = result.get(key, 0) + 1
    return result


# ============================================================
#  3. 파일 / CSV 도구
# ============================================================


def read_text(path, default=""):
    """파일을 읽어 문자열로 돌려준다. 없으면 default."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return default


def read_lines(path):
    """파일을 읽어 줄 리스트로 돌려준다 (줄바꿈 제거). 없으면 빈 리스트."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            result = []
            for line in f:
                result.append(line.strip())
            return result
    except FileNotFoundError:
        return []


def read_csv(path, encoding="utf-8"):
    """CSV 를 읽어 딕셔너리 리스트로 돌려준다.

    사용 예)
        rows = read_csv("data/employees.csv")
        for row in rows:
            print(row["이름"])

    파일이 없으면 빈 리스트를 돌려줍니다.
    """
    rows = []
    try:
        with open(path, "r", encoding=encoding, newline="") as f:
            for row in csv.DictReader(f):
                rows.append(row)
    except FileNotFoundError:
        pass
    return rows


def save_csv(path, rows, fieldnames, encoding="utf-8-sig"):
    """딕셔너리 리스트를 CSV 로 저장한다.

    path       : 저장할 경로
    rows       : 딕셔너리 리스트
    fieldnames : 열 이름 리스트 (순서대로)
    encoding   : 기본 utf-8-sig (엑셀에서 한글 안 깨짐)

    사용 예)
        save_csv("결과.csv", data, ["이름", "부서", "연봉"])
    """
    with open(path, "w", encoding=encoding, newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    return Path(path)


def save_dict_csv(path, data, headers, encoding="utf-8-sig"):
    """딕셔너리를 두 열짜리 CSV 로 저장한다.

    sum_by() 의 결과를 저장할 때 씁니다.

    사용 예)
        save_dict_csv("집계.csv", {"영업": 300}, ["부서", "합계"])
    """
    with open(path, "w", encoding=encoding, newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for key, value in data.items():
            writer.writerow([key, value])
    return Path(path)


# ============================================================
#  4. 출력 꾸미기 도구
# ============================================================


def make_bar(value, unit=1000, mark="■", max_length=40):
    """숫자를 막대그래프 문자열로 만든다.

    value      : 표시할 숫자
    unit       : 막대 하나가 나타내는 크기
    mark       : 막대에 쓸 문자
    max_length : 최대 길이 (너무 길어지지 않게)

    사용 예)
        make_bar(5000)              -> "■■■■■"
        make_bar(5000, unit=2000)   -> "■■"
    """
    count = int(value / unit)
    if count > max_length:
        count = max_length
    return mark * count


def make_line(char="-", length=50):
    """구분선을 만든다.

    사용 예)
        print(make_line())        ->  --------------------
        print(make_line("=", 20)) ->  ====================
    """
    return char * length


def format_money(amount, unit="원"):
    """숫자에 천 단위 쉼표와 단위를 붙인다.

    사용 예)
        format_money(1234567)   ->  "1,234,567원"
    """
    return f"{amount:,}{unit}"


def print_table(rows, columns):
    """딕셔너리 리스트를 표 형태로 출력한다.

    rows    : 딕셔너리 리스트
    columns : 출력할 열 이름 리스트

    사용 예)
        print_table(data, ["이름", "부서", "연봉"])
    """
    if not rows:
        print("(데이터 없음)")
        return

    # 각 열의 너비를 내용에 맞게 계산
    widths = {}
    for col in columns:
        widths[col] = len(col)
        for row in rows:
            text = str(row.get(col, ""))
            if len(text) > widths[col]:
                widths[col] = len(text)

    # 헤더 출력
    header = ""
    for col in columns:
        header += col.ljust(widths[col] + 2)
    print(header)
    print(make_line("-", len(header)))

    # 데이터 출력
    for row in rows:
        line = ""
        for col in columns:
            line += str(row.get(col, "")).ljust(widths[col] + 2)
        print(line)


# ============================================================
#  5. 자체 테스트
# ============================================================
#
# if __name__ == "__main__": 의 의미
#
#   아래 블록은 '이 파일을 직접 실행했을 때만' 돌아갑니다.
#   다른 파일에서 import 할 때는 실행되지 않습니다.
#
#   [원리]
#     파이썬은 파일마다 __name__ 이라는 변수를 자동으로 만듭니다.
#
#       직접 실행 (python my_tools.py)  -> __name__ 은 "__main__"
#       import 될 때                    -> __name__ 은 "my_tools"
#
#     그래서 __name__ == "__main__" 인지 확인하면
#     "지금 내가 직접 실행된 건가?" 를 알 수 있습니다.
#
#   [왜 필요한가]
#     이게 없으면, 다른 파일에서 import 하는 순간
#     아래 테스트 코드가 전부 실행되어 버립니다.
#     원하지 않는 출력이 잔뜩 나오겠죠.
#
#   모듈을 만들 때는 항상 이 블록으로 감싸세요.

if __name__ == "__main__":
    print("=" * 55)
    print(f" my_tools.py 자체 테스트 (버전 {VERSION})")
    print("=" * 55)

    print("\n[1] 숫자 변환")
    print("  to_int('  42 ')        =", to_int("  42 "))
    print("  to_int('사십이')        =", to_int("사십이"))
    print("  to_int('사십이', -1)    =", to_int("사십이", -1))
    print("  to_float('3.14')       =", to_float("3.14"))
    print("  clean_number('4,500원') =", clean_number("4,500원"))

    print("\n[2] 통계")
    print("  get_average([1, 2, 3]) =", get_average([1, 2, 3]))
    print("  get_average([])        =", get_average([]))
    print("  find_max([3, 9, 1])    =", find_max([3, 9, 1]))
    print("  find_min([3, 9, 1])    =", find_min([3, 9, 1]))

    sample = [
        {"부서": "영업", "연봉": 4500},
        {"부서": "개발", "연봉": 5200},
        {"부서": "영업", "연봉": 5100},
    ]
    print("  sum_by(...)            =", sum_by(sample, "부서", "연봉"))
    print("  count_by(...)          =", count_by(sample, "부서"))

    print("\n[3] 출력 꾸미기")
    print("  make_bar(5000)         =", make_bar(5000))
    print("  format_money(1234567)  =", format_money(1234567))

    print("\n[4] 표 출력")
    print_table(sample, ["부서", "연봉"])

    print("\n" + "=" * 55)
    print(" 테스트 완료")
    print(" 이 출력은 my_tools.py 를 직접 실행했을 때만 나옵니다.")
    print("   다른 파일에서 import 하면 나오지 않습니다.")
    print("=" * 55)
