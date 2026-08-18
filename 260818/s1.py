import math

print("16 제곱근 : ", math.sqrt(16))
print("원주율 : ", round(math.pi, 4))
print("2의 10제곱 : ", math.pow(2, 10))
print("올림", math.ceil(3.2))
print("내림", math.floor(3.8))


#
# 특정 함수만
#
# from 모듈이름 import 함수이름

from math import sqrt, pi

print(sqrt(16), pi)


# 별칭 (as)
import random as rd

print("주사위 : ", rd.randint(1, 6))
print("무작위 : ", rd.choice(["김밥", "돈가스", "라면"]))

lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
rd.shuffle(lst)
print(lst)

print("중복 없이 6개 : ", rd.sample(range(1, 46), 6))


#
# import하면
#

# import my_tools를 실행하면 파이썬은 이렇게 한다.

# 1) my_tools.py 파일을 찾는다.
#    찾는 순서 : 현재 폴더 >> 파이썬 설치 폴더 >> 패키지 폴더

# 2) 그 파일을 위에서 아래로 한 번 실행
#    def 문들이 실행되면서 함수가 메모리에 등록

# 3) my_tools라는 이름으로 사용 가능

# 여기서 중요한 건 2번
# my_tools.py 안에 print문이 있으면 실행


#
# 설치 없이 쓰는 것
#

import datetime
import os

today = datetime.date.today()
now = datetime.datetime.now()

print("날짜와 시간")
print("오늘 날짜 : ", today)
print("현재 시각 : ", now)
print("현재 시각 : ", now.strftime("%H시 %M분"))

# 요일 (0 = 월 ~ 6 = 일)
week = ["월", "화", "수", "목", "금", "토", "일"]
print("요일 : ", week[today.weekday()] + "요일")

# 날짜 계산
tomorrow = today + datetime.timedelta(days=1)
next_week = today + datetime.timedelta(days=7)

print(datetime.timedelta(days=1))


# 간단 실습
# import datetime 한 후 timedelta없이
# def date_calcul(x):
#     dt = datetime.date("")
#     result = datetime.date.today() + datetime.date(1, 1, x)
#     return result


# print(date_calcul(3))


#
# 자주 쓰는 라이브러리
#
# math >> 수학 계산 (제곱근, 올림, 내림)
# random >> 무작위 (뽑기, 섞기, 난수)
# datetime >> 날짜와 시간
# csv >> csv 파일 읽고 쓰기
# pathlib >> 경로 다루기
# os >> 운영체제 기능
# json >> JSON 데이터 (웹에서 많이 쓰는 형식)
# re >> 문자열 패턴 찾기


# 같은 폴더에 있는 my_tools.py 가져오기
# 파일 이름만 (확장자 x)

import my_tools_43_260818 as my_tools

print("모듈 버전 : ", my_tools.VERSION)
print("작성자 : ", my_tools.AUTHOR)
print("\n[숫자 변환 도구]")
print(my_tools.to_int("   4500    "))
print(my_tools.to_float("사천오백"))
print(my_tools.to_float("사천오백,-1"))
print(my_tools.clean_number("4,500원"))
print("\n [통계 함수]")
print(my_tools.get_average([90, 85, 100]))
print(my_tools.find_max([3, 9, 1]))
print(my_tools.find_min([3, 9, 1]))

from my_tools_43_260818 import make_bar, format_money

print(make_bar(5000))
print(format_money(12345))


#
# __name__의 정체
#

# [원리]
# 파이썬 파일마다 __name__이라는 변수가 자동으로 만들어짐
# 직접 실행한 파일 >> __name__은 '__main__'
# import된 파일 >> __name__은 파일 이름 ("my_tools")
# 그래서 __name__ == '__main__'인지 확인하면
# 직접 실행되는지 알 수 있음

# 파이썬이 특별하게 다루는 이름
# __name__, __file__ 등

print(__name__)
print(my_tools.__name__)


#
# 모듈 만들 떄 규칙
#

"""
    1) 관련 있는 함수끼리 모아
       숫자 변환끼리, 통계끼리, 코끼리

    2) 각 함수에 설명을 단다
       def 바로 아래에 설명을 쓴다
       이걸 docstring이라고 한다

    3) 실행 코드는 if __name__ == "__main__" : 안에 넣는다

    4) 파일 맨 뒤 파일이 뭔지 적는다

    [docstring이 좋은 이유]
    - help()로 설명 볼 수 있음
    - VS code에서 함수 이름에 마우스 올리면 설명이 뜸
"""


#
# pip 외부 패키지 설치
#

# pandas, numpy 등 직접 설치하는 것
# 설치는 터미널에서

# 자주 쓰는 pip 명령어
# pip install pandas >> 설치
# pip install pandas numpy >> 한 번에 설치
# pip install pandas==2.0.0 >> 특정 버전 설치
# pip list >> 설치된 목록
# pip show pandas >> 정보 보기
# pip install --upgrade pandas >> 최신 버전 업데이트
# pip uninstall pandas


#
# 가상환경 - 개념 알기
#

# a 프로젝트에는 pandas 1.5 버전이 필요
# b 프로젝트에는 pandas 2.0 버전이 필요

# 컴퓨터 한 대에 충돌이 되니 가상환경을 사용

# 프로젝트마다 별도의 작은 python 환경을 만든다.

# python3 -m venv venv >> 가상환경 만들기

# venv\Scripts\activate >> 켜기(윈도우)
# source venv/bin/activate >> 켜기(맥, 리눅스)
# deactivate >> 끄기

# 켜지면 터미널 앞에 (venv)가 붙는다
# 그 상태에서 pip install하면 프로젝트에만 설치

# README 파일에 '가상환경을 만들고 ...' 라고 적혀 있을 거다.


#
# import가 안 될 떄 체크리스트
#
# ModuleNotFoundError : No module named 'pandas'

# 해결법
# 1) 터미널에 pip list 목록
# 2) 대소문자 구분
# 3) 파일 이름 확인(라이브러리 명과 다르게 해야 함)
# 4) 만든 모듈일 경우 같은 파일이어야 함
# 5) 파이썬 여러 개 있는지 확인

# ctrl(command) + shift + P >> Python:Select Interpreter >> 선택


# -------------------------------------------------------------
# 정리
# -------------------------------------------------------------
#
#   [import 문법]
#
#     import math                 표준 라이브러리
#     import my_tools             내가 만든 파일 (.py 는 뺀다)
#     import pandas as pd         외부 패키지 + 별칭
#     from math import sqrt       함수만 골라오기
#
#   [모듈 만들 때 규칙]
#
#     - 관련 있는 함수끼리 한 파일에 모은다
#     - 각 함수에 docstring 으로 설명을 단다
#     - 실행 코드는 if __name__ == "__main__": 안에 넣는다
#
#
#   [pip 명령어]
#
#     pip install 패키지명         설치
#     pip list                    목록 확인
#     python -m pip install ...   안 될 때 이렇게
#
#
#   [기억할 것 5가지]
#     1. import 는 남이 만든 코드 가져오기. 내 파일도 똑같이 가져온다
#     2. import 하면 그 파일이 한 번 실행된다
#     3. 그래서 테스트 코드는 if __name__ == "__main__": 로 감싼다
#     4. 외부 패키지는 터미널에서 pip install 로 설치한다
#     5. import 가 안 되면 5-1 의 5번(파이썬이 여러 개)부터 의심하라
