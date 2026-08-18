#
# 반복문 - for문
#

fruits = ["사과", "바나나", "포도"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

for i in fruits:
    print(i)

a = [
    {"name": "김철수", "age": 25, "city": "서울"},
    {"name": "안철수", "age": 35, "city": "부산"},
    {"name": "박수수", "age": 15, "city": "인천"},
    {"name": "한동수", "age": 65, "city": "대구"},
    {"name": "이준수", "age": 45, "city": "대전"},
]
for i in a:
    print(i)
    for j in i:
        print(i[j])


a = "문자열"
print(a[0])


# 간단 실습
student = [
    {"name": "철수", "subjects": {"국어": 85, "영어": 96, "수학": 77}},
    {"name": "민수", "subjects": {"국어": 35, "영어": 56, "수학": 100}},
]

# 간단 실습
# 1. 각 평균
# 2. 두 사람 평균
# 3. 누가 더 우수한 사람인지

student = [
    {"name": "민수", "국어": 95, "영어": 100},
    {"name": "철수", "국어": 75, "영어": 50},
]

for i in student:
    print(f"{i['name']} 평균 : {(i['국어'] + i['영어']) / 2}")

for i in student:
    if i["name"] == "민수":
        min = (i["국어"] + i["영어"]) / 2
    else:
        cheol = (i["국어"] + i["영어"]) / 2

print(f"두 사람의 평균은 {(min + cheol) / 2}입니다.")

if min > cheol:
    print("민수가 더 우수한 학생입니다.")
elif min < cheol:
    print("철수가 더 우수한 학생입니다.")
elif min == cheol:
    print("두 학생이 동일합니다.")


#
# min()
#
numbers = [44, 22, 66, 32, 11, 677, 22]
mini = numbers[0]
for i in numbers:
    if i < mini:
        mini = i
print(mini)
