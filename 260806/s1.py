#
# 딕셔너리 - key : value
#

# 리스트의 불편함을 개선

person = ["김철수", 25, "서울"]
print(person[1])  # 25

person = {"name": "김철수", "age": 25, "city": "서울"}
print(person["age"])  # 25


#
# 만들고 꺼내기
#

person = {"name": "김철수", "age": 25}
#           키       값
print(type(person))  # dict


empty = {}  # 빈 딕셔너리

print(person["name"])  # 김철수

# tip - get()을 쓰면 키가 없어도 에러가 안 남
print(person.get("phone"))
print(person.get("phone"), "있는지 없는지 확인")

# 사용자 입력처럼 뭐가 들어올지 모를 땐 [] 대신 get()이 안전.
print("name" in person)  # True >> 값이 아니라 key 검사
print("김철수" in person)  # False


#
# 추가, 수정, 삭제
#
person = {"name": "김철수", "age": 25}

person["city"] = "서울"  # 없는 key >> 추가
person["age"] = 26  # 있는 key >> 수정
# 추가와 수정의 문법이 같음. 오타 시 새로운 key가 생김.

person["agee"] = 30

del person["agee"]  # agee 삭제
removed = person.pop("city")  # 삭제하면서 값을 받음

print(removed)  # 서울
print(person)


#
# key, value 한번에 다루기
#

scores = {"국어": 90, "과학": 90, "영어": 85, "음악": 85, "수학": 77}
print(list(scores.keys()))  # ['국어', '영어', '수학']
print(list(scores.values()))  # [90, 85, 77]
print(len(scores))

print(list(set(scores.values()))[len(set(scores)) // 2])

#
# key 규칙 & 중첩
#

d = {"문자열": 1, 10: 2, (1, 2): 3}  # 0, 문자열, 숫자, 튜플은 key 가능
# 리스트는 key 불가

# value엔 뭐든 가능
# value에 딕셔너리도 가능
