#
# 파이썬 자료 구조 - 리스트 / 튜플 / 딕셔너리 / 세트
#

# 여러 값을 한 변수에 담는 방법

# 4가지 한 눈에 보기
# 리스트   [1, 2, 3] 순서 o, 수정 o, 중복 o
# 튜플    (1, 2, 3) 순서 o, 수정 x, 중복 o
# 딕셔너리  {"a":1, "b":2} >> 키 : 값 /// 수정 o 키 중복 x
# -> 리스트가 가장 기본, 사용 빈도 압도적.
#    나머지 셋은 리스트와 뭐가 다른가로 이해하면 쉽다.


#
# 리스트(list) >> 가장 많이 씀.
#

# 리스트가 왜 필요한가

score1 = 90  # 변수만 쓰면 사람이 늘어날 때마다
score2 = 85  # 변수를 계속 만들어야 함
score3 = 77  # 100명이면 변수 100개..

scores = [90, 85, 77, 92, 68]  # 리스트면 한 줄로 끝
print(scores)

# 리스트 >> 대괄호 [ ] 안에 쉼표로 나열

numbers = [1, 2, 3, 4, 5]
fruits = ["사과", "바나나", "포도"]
empty = []  # 빈 리스트
mixed = [1, "안녕", 3.14, True, None]  # 종류가 섞여도 됨
nested = [[1, 2], [3, 4]]  # 리스트 안에 리스트

print(type(numbers))  # list
print(len(fruits))  # 3 >> 들어있는 개수

#
# 값 꺼내기
#
fruits = ["사과", "바나나", "포도", "딸기"]

print(fruits[0])  # 사과
print(fruits[2])  # 포도
print(fruits[-1])  # 딸기

print(nested[0][1])  # 2

#
# 슬라이싱 - 잘라내기
#
numbers = [10, 20, 30, 40, 50]
print(numbers[1:3])  # 슬라이싱 끝 번호 포함 안 됨
print(numbers[:3])  # 처음부터
print(numbers[2:])  # 끝까지

print(numbers[-2:])  # 뒤에서 2개
print(numbers[::2])  # 두 칸씩 건너뛰기

print(numbers[::-1])  # 뒤집기
# reverse()와 달리 원본을 건드리지 않고 새 리스트를 만듦.
# 문자열도 가능
# "안녕하세요"[::-1] >> 요세하녕안

#
# 리스트는 수정 가능
#
# 문자열과의 결정적 차이

word = "PYTHON"
# word[0] = 'J' 불가능
fruits = ["apple", "banana"]
fruits[0] = "grape"
print(fruits)


#
# 값 추가
#
# append(value) >> list 넣으면 한 덩어리로 들어감
# insert(index, value)
# expend(list) >> 이어서 붙어짐

print([0] * 5)  # [0, 0, 0, 0, 0]
print([1, 2] + [3, 4])  # [1, 2, 3, 4]

#
# 값 삭제
#
# remove(value) >> value 제거
# pop(index) >> index 값 삭제 + 그 값만 추출
# del list[index] >> index 값 삭제
# clear() >> 리스트 비우기

numbers = [10, 20, 30, 40]
last = numbers.pop()
print(last)  # 40

del numbers[0]
print(numbers)  # [20, 30]

numbers.clear()  # 전체 비우기
print(numbers)

#
# ㅇ
#

print([1, 2, 2, 3].count(2))  # 2 >> count(value) value 개수

# index()와 remove()는 없는 값이면 에러
# in으로 먼저 확인

#
# 리스트 정렬
#

a = [30, 10, 50, 20]
result = sorted(a)
print(result, a)  # 원본 값은 그대로

a.sort(reverse=True)
print(a)
# 원본 지키기 sorted(), 바꾸고 싶으면 sort()

#
# 문자열 리스트
#

fruits = "사과,바나나,포도".split(",")  # 문자열 >> 리스트  # ruff >> noqa: SIM905

print(", ".join(fruits))  # 사과, 바나나, 포도
print("-".join(fruits))  # 사과-바나나-포도

print(fruits)  # ['사과', '바나나', '포도']

# ! >> join은 문자열 리스트만 해당. 숫자면 str()로 변환.
