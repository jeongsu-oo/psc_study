# import numpy as np


#
# 함수 안에 함수
#
def buga(p):
    return int(p * 1.1)


def discount(p):
    return int(p * 0.8)


def f_price(p):
    return buga(discount(p))  # 안쪽 함수인 discount가 먼저 실행


print("원가 50000원")
print("할인만 : ", discount(50000), "원")
print("부가세만 : ", buga(50000), "원")
print("할인 후 부가세 : ", f_price(50000), "원")


# pw = "abc12345"

# if len(pw) >= 8 and any(ch.isdigit() for ch in pw) and any(ch.isalpha() for ch in pw):
#     print("사용 가능한 비밀번호입니다.")
# else:
#     print("사용할 수 없습니다.")


def safe_pw(pw):
    "8자 이상 + 숫자 포함 + 영문자 포함 >> True"
    if len(pw) < 8:
        return False
    if not any(ch.isdigit() for ch in pw):
        return False
    if not any(ch.isalpha() for ch in pw):
        return False
    return True


# print(safe_pw("qlalfqjsgh"), "확인")

# if safe_pw("qlalfqjsgh"):
#     print("사용 가능")
# else:
#     print("사용 불가")

# # 간단 실습
# while True:
#     pw = input("비밀번호를 설정하세요 : ")
#     if safe_pw(pw):
#         print("사용할 수 있는 비밀번호입니다.")
#         break
#     else:
#         print("사용 할 수 없는 비밀번호입니다 다시 입력해주세요.")


# 함수 이름 짓는 tip
# 규칙
# 1. 동사 시작 get_, make_, send_, print_
# 2. 결과값이 bool이면 is_, has_, can_
# 3. 주석 없이 이해하는 이름이면 best


# 함수 없이 학생 성적 처리
kor = [90, 85, 100]
eng = [70, 95, 80]
mth = [60, 75, 88]

# 국어
avg = sum(kor) / len(kor)
print("국어 평균", round(avg, 1))

if avg >= 90:
    print("등급 : A")
elif avg >= 80:
    print("등급 : B")
else:
    print("등급 : C")

# 영어 수학은 복붙


# 평균 구하는 함수
def get_avg(scores):
    return round(sum(scores) / len(scores), 1)


def get_grade(x):
    if x >= 90:
        return "A"
    elif x >= 80:
        return "B"
    return "C"


def print_std(sub, score):
    avg = get_avg(score)
    grade = get_grade(avg)
    print(f"{sub} 평균 : {avg} / 등급 : {grade}")


print_std("국어", kor)
print_std("영어", eng)
print_std("수학", mth)


#
# 전역변수와 지역변수
#

# 전역변수(global) : 함수 밖에서 만든 변수 >> 프로그램 전체에 생존
# 지역변수(local) : 함수 안에서 만든 변수 >> 함수 내에만 존재


def test():
    temp = 5
    print(temp)


# print(temp)   # 지역변수라 불가능

test()


num = 10


def change():
    num = 99
    print("함수 안에서 본 num : ", num)


change()
print(num)


# 매개변수도 지역변수

score = 50


def add_ten(s):
    s = s + 10


#
# global 키워드
#

total = 0


def add_global(x):
    global total
    total = total + x


add_global(6)
print(total)


# global 쓰면 안 되는 이유 >> 많아지면 추적이 쉽지 않다

money = 10000


def buy_cof():
    global money
    money -= 4500


def buy_lun():
    global money
    money -= 8000


def charge():
    global money
    money += 5000


buy_cof()
buy_lun()
charge()
print("남은 돈 : ", money)


#
num = 10


def plus_num(number, num):
    return number + num


number = plus_num(num, 5)
print(number)


def buy(money, price):
    return money - price


money = 10000
print("시작", money)
money = buy(money, 4500)
print("커피 구매 후 >>", money)


# 리스트와 딕셔너리는 다르게 동작

scores = [90, 85]


def add_score():
    scores.append(100)


print(scores)
add_score()
print(scores)

# append(), remove(), sort()의 경우 원본을 건드린다.
# 딕셔너리 dict['키'] = 값도 마찬가지

names = ["김철수", "이영희"]


def replace_all():
    # names = ["박민수"]    # 주석 풀면 지역변수가 돼.
    names.append("박민수")


replace_all()
print(names)


# 리스트도 return하는 것이 안전
og = [3, 1, 2]


def sort_bad(data):
    data.sort()
    return data


print(sort_bad(og))

og = [3, 1, 2]


def sort_good(data):
    new_data = sorted(data)
    return new_data


result = sort_good(og)
print(og)
print(result)


#
# 우선순위 지역 vs 전역
#
name = "전역"


def show():
    name = "지역"
    print(name)


show()  # 지역
print(name)  # 전역
