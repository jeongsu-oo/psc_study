#
# 예외 처리
#

# [에러 메시지의 구조]
#
# Traceback (most recent call last):
# File "C:/work/test.py", line 5, in <module>
# num = int("가나다")
# ValueError: invalid literal for int() with base 10: '가나다'

# get()함수
# 없으면 값을 넣어줌

# 오류
# user_input = "스물다섯"

# print("1단계 : 입력값 받음 >>", user_input)
# age = input(user_input)
# print("2단계 : 나이 계산 >>", age + 1)

#
# try
#
# age = input("나이를 입력하세요")
# try:
#     print(f"내년이면{int(age) + 1}살이에요.")
# except Exception:
#     print(f"숫자를 입력하세요. 입력값 : {age}")

#
# except 뒤엔 반드시 에러 이름을 적어라
#

# except 뒤에 아무것도 안 쓰면 '모든 에러'를 잡는다.
# 그러나 지양


def divide(a, b):
    # 문제가 있으면 안내 메시지로 돌려준다.
    try:
        return a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없다."
    except TypeError:
        return "숫자만 넣어라."


print(divide(1, 2))
print(divide(1, 0))
print(divide(1, "이"))

# except를 여러개 쓰면 위에서부터 차례로 확인
# 해당하는 것을 만나면 그것만 실행하고 나머지는 건너뛴다
# if / elif와 같은 방식


#
# 에러 메시지 직접 꺼내기
#

# except ValueError as e :
# e 대신 다른 이름

try:
    num = int("가나다")
except ValueError as e:
    print("에러 발생")
    print("에러 종류 : ", type(e).__name__)
    print("에러 내용 : ", e)


#
# else & finally
#
# try : 위험한 코드
# except : 에러가 났을 때만
# else : 에러가 안 났을 때만
# finally : 에러가 나든 말든 무조건

# 실행 순서 정리
# 에러가 안 나면 : try 전체 >> else >> finally
# 에러가 나면 : try 일부 >> except >> finally
# 어느 쪽이든 finally는 항상 실행


def check(value):
    print(f"\n [{value}] 처리 시작")
    try:
        num = int(value)
    except ValueError:
        print("except 실행 : 변환 실패")
    else:
        print(f"else 실행 : 변환 성공!{num}")
    finally:
        print("finally 실행 : 이 줄은 항상 나옴")


check(1)
check("200")
check("a")


# else 사용법
# try는 최소한의 코드
# 성공시 할 일은 else에 넣으면 명확

# finally 사용법
# 뒷정리에 쓴다. 대표적으로 파일 닫기
# 좀 있다 배우는 with문이 자동으로 해줌


#
# 실전 패턴 - 올바른 값 넣을 때까지 다시 묻기
#
# while True와 try/except 조합 패턴

# # 구조
# while True:
#     # 입력 받기
#     try :
#         # 변환 시도
#         return # 결과
#     except :
#         # 안내


def ask_num(msg):
    # 숫자를 제대로 입력할 때까지 계속 질문
    while True:
        value = input(msg)
        try:
            return int(value)
        except ValueError:
            print("숫자가 아닙니다.")


# n = ask_num("숫자를 입력하세요")
# print(n)


def ask_age():
    while True:
        value = input("나이 0~120 : ")
        try:
            age = int(value)
            if 0 <= age <= 120:
                return age
            print("0에서 120 사이로 입력하세요.")
        except ValueError:
            print("숫자를 입력해주세요.")


# ask_age()


def ask_age2():
    while True:
        value = input("나이 0~120 : ")
        try:
            age = int(value)
        except ValueError:
            print("숫자를 입력해주세요.")
            continue

        if 0 <= age <= 120:
            return age
        print("0에서 120 사이로 입력하세요.")


# ask_age2()


def ask_age3():
    while True:
        value = input("나이 0~120 : ")
        try:
            age = int(value)
        except ValueError:
            print("숫자를 입력해주세요.")
        else:
            if 0 <= age <= 120:
                return age
            print("0에서 120 사이로 입력하세요.")


# ask_age3()


# 실제 데이터는 더럽다.
raw_data = ["100", "200", "삼백", "400", "", "600"]

numbers = []  # 성공할 떄 넣는 값
errors = []  # 실패할 때 넣는 값

for i in raw_data:
    try:
        numbers.append(int(i.strip()))
    except ValueError:
        errors.append(i)

print("정상처리", numbers)
print("처리실패", errors)
print(f"{len(raw_data)}건 중 {len(numbers)}건 성공, {len(errors)}건 실패")
print("합계", sum(numbers))


#
# 중요
# 실전 패턴 - 안전한 변환 함수 만들기
#


def to_int(value, default=0):
    # 문자열을 정수로 바꾼다. 실패하면 default를 돌려준다.
    # value : 바꿀 값
    # default : 실패했을 때 돌려주는 값
    try:
        return int(str(value).strip())  # 공백제거
    except (ValueError, TypeError):
        # 괄호로 묶으면 한 번에 가능
        return default


print(to_int("100"))
print(to_int("삼백"))
print(to_int("삼백", -1))
print(str([1, 2, 3, 4]).strip())


def to_float(value, default=0.0):
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default


print(to_float("3.14"))
print(to_float(None))
print(to_float("31만"))
print(to_float("31"))


#
# 에러 만들기
#
def set_age(age):
    # 나이를 설정. 이상한 값이면 에러
    if age < 0:
        raise ValueError("나이는 음수가 될 수 없다.")
    if age > 150:
        raise ValueError("거짓말 금지.")
    return f"나이 {age}세로 설정되었습니다."


print(" ", set_age(30))
# print(" ", set_age(-30))
# print(" ", set_age(190))

# 잘못된 값을 넣으면
try:
    print(set_age(-5))
except ValueError as e:
    print("설정 실패", e)

# raise >> 에러를 던진다
# except >> 에러를 받는다


# 이럴 땐 try를 쓰지 마라
# try / except 만능 x, 남용 금지

# 나쁜 예 >> 범위가 너무 넓은 경우
# try :
#     data = read_file()
#     result = calculate(data)
#     save(result)
# except :
#     print('에러')

# 정리

# if로 가능하면 if로
# try는 미리 막을 수 없는 상황
# try 범위를 넓게 잡지 마라 (문제점을 확인하기 힘들다)
# except에서 pass 하지마(문제점을 확인 몬한다)


# 예제

# 1. 위 리스트에서 숫자로 바꿀 수 있는 것만 골라 합계와 실패 개수를 돌러주는 함수

practice_data = ["10", "20", "삼십", "40", "", "60"]

# 2. 두 수를 나누는 함수 (0으로 나눌 수 없, 숫자 아니면 숫자 아님 출력)

# 3. 점수(0~100)를 받아 등급을 돌려주는 함수 (범위를 벗어나면 raise 사용)


# 예제 1
nums = []
errors = []


def ex_1(a):
    for i in a:
        try:
            nums.append(int(i.strip()))
        except ValueError:
            errors.append(i)
    return sum(nums), len(errors)


print("-" * 20, "\n예제 1 답변\n" + "-" * 20)
print(ex_1(practice_data))


# 예제 2        두 수를 나누는 함수 (0으로 나눌 수 없, 숫자 아니면 숫자 아님 출력)
def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "0으로 나눌 수 없다"
    except (ValueError, TypeError):
        return "숫자를 입력하세요"


print("-" * 20, "\n예제 2 답변\n" + "-" * 20)
print(divide(1, 2))
print(divide(1, 0))
print(divide(1, "이"))


# 예제 3        점수(0~100)를 받아 등급을 돌려주는 함수 (범위를 벗어나면 raise 사용)
def get_grade(score):
    try:
        if score < 0 or score > 100:
            raise ValueError("백점 만점이에요")
        if score >= 90:
            return "A"
        elif score >= 80:
            return "B"
        elif score >= 70:
            return "C"
        else:
            return "D"
    except TypeError:
        return "숫자를 입력하라"
    except ValueError:
        return "백점만점이다"


print("-" * 20, "\n예제 3 답변\n" + "-" * 20)
print(get_grade(100))
print(get_grade("백점"))
print(get_grade(500))
