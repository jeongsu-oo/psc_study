print(type(3))  # int 정수
print(type(3.14))  # float 실수
print(type("문자"))  # str 문자열
print(type(False))  # bool 불리언
print(type(None))  # None

# 특정 자료형이 맞는지 확인할 때 isinstance()
print(isinstance(10, int))  # True
print(isinstance(10, str))  # False

exp = 1.5e3  # 지수 표기 = 1.5 * 10 ** 3 = 1500.00
print(exp)  # 1500.0

# float의 가장 유명한 함정 : 소수 계산에 오차가 생긴다.
print(0.1 + 0.2)  # 0.300000004
print(0.1 + 0.2 == 0.3)  # False이기 때문에 ==으로 비교하면 안됨

# 이유 : 컴퓨터는 2진수로 저장하는데 0.1을 2진수로 정확히 표할 수 없음
# (10진수로 1/3을 0.3333333.....)으로 밖에 못 쓰는 것과 같은 원리


# 해결법 1 : 반올림 후 비교
# 해결법 2 : decimal 모듈 사용
from decimal import Decimal

print(Decimal("0.1") + Decimal("0.2"))  # 0.3 (정확함)

# 나누기(/)는 나머지가 없어도 float 형태

#
# 자주 쓰는 이스케이프 문자
#
print("줄바꿈\n다음 줄")  # \n = 줄바꿈
print("이름\t나이")  # \t = 탭(간격)
print("역슬래시 \\ 출력")  # \\ = 역슬래시 자체
print(r"C:\new\folder")  # 앞에 r을 붙이면 \를 그대로 (경로 쓸 때 좋음)


#
# 자주 쓰는 문자열 기능
#

text = "        Hello Python       "
print(text.strip())  # "Hello Python" 앞 뒤 공백 제거
print(text.upper())
print(text.lower())
print(text.replace("o", "0"))  # o를 0으로 바꾸기
print("사과, 배, 감".split(","))  # ['사과','배','감'] 구분자로 사용

# bool은 사실 숫자다.

print(True + True)  # 2

# 아래 모두 False
print(bool(0))
print(bool(0.0))
print(bool(""))  # 빈 문자열
print(bool(None))
print(bool([]))  # 빈 리스트

# 그 외 모든 값은 참
# 예를 들어
print(bool(1))
print(bool(-5))
print(bool("0"))


#
# None
#

result = None  # 첫 글자 대문자
print(type(None))  # Nonetype

# "아직 값이 정해지지 않았다"를 표현할 때 사용
# 0, "", False와는 다르다

# 0     >> 숫자 0이라는 값이 '있음'
# ""    >> 빈 문자열이라는 값이 '있음'
# None  >> 값 자체가 '없음'

# None인지 확인할 땐 == 대신 is 사용
print(result is None)  # True
print(result is not None)  # False

# ===================================

#
# 정리
#

# 자료형
# int, float, str, bool, None
# 정수, 실수, 문자열, 불리언, 값 없음
