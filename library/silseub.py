print("--- 문제 1 ---")
import random as rd

books = ["사피엔스", "코스모스", "총균쇠", "이기적 유전자", "데미안", "토지"]
print(f"오늘의 추천 도서 : {rd.choice(books)}")


print("\n--- 문제 2 ---")
print(f"발급된 도서번호 : {rd.sample(range(1000, 10000), 5)}")


print("\n--- 문제 3 ---")
import datetime as dt

print(f"대출일      : {dt.date.today()}")
print(f"반납 예정일 : {dt.date.today() + dt.timedelta(days=14)}")


print("\n--- 문제 4 ---")
from math import ceil

book_counts = [8, 10, 3, 17]
for i in book_counts:
    print(f"{i}권 -> {ceil(i / 4)}번")


print("\n--- 문제 5 ---")
bks = rd.sample(books, 3)
num = rd.sample(range(1000, 10000), 3)
for i, j in zip(bks, num):
    print(f"{[bks.index(i) + 1]} {i} (번호{j})")
    print(f"    {dt.date.today()} ~ {dt.date.today() + dt.timedelta(days=14)}")


print("\n--- 문제 6 ---")
import library_tools as lt

print(f"반납 예정일 : {lt.get_due_date}")
print(f"5일 연체료 : {lt.get_late_fee(5)}원")


print("\n--- 문제 7 ---")
print(f"""
[대출 규정]
대출 기간 : {lt.LOAN_DAYS}일
연체료 : 하루 {lt.FEE_PER_DAY}원
최대 대출 권수 : {lt.MAX_BOOKS}권""")


print("\n--- 문제 8 ---")
from library_tools import get_late_fee

print(f"별칭으로 : {lt.get_late_fee(3)}원")
print(f"골라오기로 : {get_late_fee(3)}원")

print("\n--- 문제 9 ---")
print(f"이 파일의 __name__ : {__name__}")
print(f"library_tools의 __name__ : {lt.__name__}")

print("\n--- 문제 10 ---")
lst = []
for i in dir(lt):
    if "__" not in i:
        lst.append(i)
print("사용 가능한 것들 : ", lst)
print(f"""
get_due_date 함수 설명 : {lt.get_due_date.__doc__}""")
