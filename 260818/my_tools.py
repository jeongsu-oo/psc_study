#
# 직접 만든 모듈
#

# 실행하는 파일이 아니라 가져다 쓰는 파일
#
# import my_tools
# my_tools.to_int('100')

# [파일 구성]
# 1. 숫자 변환 도구
# 2. 통계 도구
# 3. 파일 / csv 도구
# 4. 출력 꾸미기 도구
# 5. 자체 테스트 (맨 아래)

from pathlib import Path
import csv

# 모듈에도 변수를 둘 수 있다.
# 대문자로 써서 상수를 표현하자

VERSION = "1.0"
AUTHOR = "우리 팀"


# 1. 숫자 변환 도구
# 문자열을 정수로, 실패 시 default
# 사견 : csv값은 전부 문자열, 이 함수를 자주 씀
def to_int(x, default=0):
    try:
        return int(str(x).strip())
    except (ValueError, TypeError):
        return default


# 문자열을 실수로, 실패 시 default
def to_flt(x, default=0.0):
    try:
        return float(str(x).strip())
    except (ValueError, TypeError):
        return default


# 단위와 쉼표를 제거하고 숫자만 뽑아낸다.
def clean_number(x, default=None):
    if x is None:
        return default

    text = str(x).strip()

    remove_char = [",", "원", "만원", "개", "명", "건", "%", " "]

    for remove in remove_char:
        text = text.replace(remove, "")
    if text == "":
        return default

    try:
        return int(x)
    except ValueError:
        return default
