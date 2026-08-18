# # 문제 1
# name = input("이름을 입력하세요 : ")
# age = int(input("나이를 입력하세요 : "))
# is_adult = bool(age >= 19)

# dic = {"name": name, "age": age, "adult": is_adult}

# print(f"""
# 문제 1번 답변 :
# {dic}

# {name}님 / {age}세 / 성인 여부 : {is_adult}
# """)

# # 문제 2
# num1 = int(input("계산하고 싶은 첫번째 숫자를 입력하세요 : "))
# num2 = int(input("계산하고 싶은 두번째 숫자를 입력하세요 : "))
# cacul = input("원하는 연산자를 입력하세요 : ")

# plus = num1 + num2
# minus = num1 - num2
# multiply = num1 * num2
# division = num1 / num2
# quotient = num1 // num2
# remainder = num1 % num2
# square = num1**num2
# dic = {
#     "+": plus,
#     "-": minus,
#     "*": multiply,
#     "/": division,
#     "//": quotient,
#     "%": remainder,
#     "**": square,
# }

# if cacul not in dic:
#     print("지원하지 않는 연산자입니다.")
# else:
#     print(f"""
# {dic}
# {num1} {cacul} {num2} = {dic[cacul]}""")


# # 문제 3

# menu = {
#     "아메리카노": {"price": 3000, "kcal": 10},
#     "라떼": {"price": 4000, "kcal": 180},
#     "케이크": {"price": 5500, "kcal": 420},
# }

# order = input("메뉴 이름을 적어주세요 : ")
# cnt = int(input("수량을 입력하세요 :"))

# print(f"""
# {order} x {cnt} = {menu[order]["price"] * cnt}원 / {menu[order]["kcal"] * cnt}kcal
# """)

# price = menu[order]["price"] * cnt
# if price >= 10000:
#     print("무료 배송 대상입니다.")
# else:
#     print(f"무료 배송까지 {10000 - price}원 남았습니다.")


# # 문제 4

# num = int(input("숫자를 입력하세요 : "))
# even = bool(num % 2 == 0)
# quotient = num // 3
# remainder = num % 3

# dic = {"number": num, "짝수": even, "몫": quotient, "나머지": remainder}

# if even:
#     result = "짝수"
# else:
#     result = "홀수"

# print(f"""
# 4번 문제 답변 :
# {dic}
# {dic["number"]}은(는) {result}입니다.
# """)


# # 문제 5

# bills = {"오만원권": 50000, "만원권": 10000, "천원권": 1000}

# cash = int(input("현금을 입력하세요 : "))

# st_bill = cash // bills["오만원권"]
# nd_bill = (cash - (st_bill * bills["오만원권"])) // bills["만원권"]
# rd_bill = (cash - (st_bill * bills["오만원권"]) - (nd_bill * bills["만원권"])) // bills[
#     "천원권"
# ]
# coins = (
#     cash
#     - (st_bill * bills["오만원권"])
#     - (nd_bill * bills["만원권"])
#     - (rd_bill * bills["천원권"])
# )

# print(f"""
# 5번 문제 답변 :
# 오만원권 {st_bill}장
# 만원권 {nd_bill}장
# 천원권 {rd_bill}장
# 남은 돈 {coins}원
# """)


# # 문제 6
# weight = float(input("몸무게(kg)를 입력하세요 : "))
# height = float(input("키(m)를 입력하세요 : "))
# BMI = round(weight / height**2, 2)

# if BMI >= 25:
#     result = "비만"
# elif 25 > BMI >= 23:
#     result = "과체중"
# elif 23 > BMI >= 18.5:
#     result = "정상"
# else:
#     result = "저체중"

# dic = {"bmi": BMI, "판정": result}

# print(f"""
# 6번 문제 답변 :
# {dic}
# BMI {dic["bmi"]} -> {dic["판정"]}
# """)


# # 문제 7

# sec = int(input("초를 입력하세요 : "))
# hr = sec // 3600
# mn = (sec - (hr * 3600)) // 60
# sc = sec - (hr * 3600) - (mn * 60)

# print(f"{sec}초 = {hr}시간 {mn}분 {sc}초")


# # 문제 8
# temp = int(input("섭씨 온도를 입력하세요 : "))
# f = temp * 9 / 5 + 32

# if temp < 15:
#     noti = "쌀쌀합니다."
# elif 15 <= temp < 28:
#     noti = "활동하기 좋은 날씨입니다."
# else:
#     noti = "무더위입니다."

# print(f"""
# 7번 문제 답변 :
# 섭씨 {temp:.1f}도 = 화씨 {f:.1f}도
# {noti}
# """)


# # 문제 9
# week = {
#     1: {"name": "월요일", "weekend": False},
#     2: {"name": "화요일", "weekend": False},
#     3: {"name": "수요일", "weekend": False},
#     4: {"name": "목요일", "weekend": False},
#     5: {"name": "금요일", "weekend": False},
#     6: {"name": "토요일", "weekend": True},
#     7: {"name": "일요일", "weekend": True},
# }
# num = int(input("1부터 7 사이의 숫자를 입력하세요 : "))
# print("9번 문제 답변 : ")
# if num not in week.keys():
#     print("1에서 7을 입력하라고 했죠.")
# else:
#     print(f"{num}번째 요일: {week[num]['name']}")
#     if week[num]["weekend"]:
#         print("주말입니다.")
#     else:
#         print("평일입니다.")


# # 문제 10
# scores = {"김철수": [90, 85, 100], "이영희": [70, 65, 80]}
# name = input("이름을 입력하세요 : ")

# if name not in scores:
#     print("이름을 다시 입력하세요.")
# else:
#     mean = round(sum(scores[name]) / len(scores[name]), 1)
#     if mean >= 80:
#         result = "합격"
#     else:
#         result = "불합격"
#     print(f"""
# {name} 점수 : {scores[name]}
# 1과목 점수 : {scores[name][0]}
# 총점 : {sum(scores[name])} / 평균 : {mean}
# 최고점 : {max(scores[name])} / 최저점 : {min(scores[name])}
# {result}
# """)


# # 문제 11
# vending = {
#     "콜라": {"price": 1500, "stock": 2},
#     "사이다": {"price": 1400, "stock": 0},
#     "물": {"price": 800, "stock": 5},
# }
# name = input("상품명을 입력하세요 : ")
# cash = int(input("투입 금액을 입력하세요 : "))

# if name not in vending:
#     print("자판기에 없는 상품입니다.")
# elif vending[name]["stock"] == 0:
#     print("재고가 0인 상품입니다.")
# elif cash < vending[name]["price"]:
#     print(f"{vending[name]['price'] - cash}원이 부족합니다.")
# else:
#     vending[name]["stock"] = vending[name]["stock"] - 1

#     print(f"""
# {name} 구매 완료 / 거스름돈 {cash - vending[name]["price"]}원
# {name} 남은 재고 : {vending[name]["stock"]}개
# """)


# # 문제 12
# id = input("ID를 입력하세요 : ")
# pw = input("PASSWORD를 입력하세요 : ")

# accounts = {
#     "alice": {"pw": "1234", "roles": ["admin", "user"]},
#     "bob": {"pw": "abcd", "roles": ["user"]},
# }

# if id not in accounts:
#     print("없는 아이디입니다.")
# elif id in accounts and pw != accounts[id]["pw"]:
#     print("비밀번호가 틀렸습니다.")
# elif id in accounts and pw == accounts[id]["pw"]:
#     if "admin" in accounts[id]["roles"]:
#         auth = "admin"
#         noti = "관리자 페이지 접근 가능"
#     else:
#         auth = "normal"
#         noti = "일반 페이지 접속 중"

#     print(f"""
# {id}님 로그인 성공
# 권한 목록 : {accounts[id]["roles"]}
# 대표 권한 : {auth}
# {noti}
# """)


# # 문제 13
# name = input("상품 이름을 입력하세요 : ")
# cnt = int(input("주문 수량을 입력하세요 : "))

# stock = {
#     "사과": {"qty": 10, "price": 1500},
#     "바나나": {"qty": 0, "price": 3000},
#     "포도": {"qty": 5, "price": 8000},
# }
# if name not in stock:
#     print("취급하지 않는 상품입니다.")
# elif stock[name]["qty"] == 0:
#     print("재고가 0인 상품입니다.")
# elif cnt > stock[name]["qty"]:
#     print(f"현재 재고는 {stock[name]['qty']}개입니다.")
# else:
#     stock[name]["qty"] = stock[name]["qty"] - cnt
#     print(f"""
# {name} {cnt}개 주문 / 결제금액 {stock[name]["price"] * cnt}원
# {name} 남은 재고 : {stock[name]["qty"]}개
# """)


# # 문제 14
# score = int(input("점수를 입력하세요 : "))
# if score >= 90:
#     tier = "A"
# elif score >= 80:
#     tier = "B"
# else:
#     tier = "C"

# print(f"""
# 입력값 타입 : {type(score)}
# 문자열로 변환 : {str(score)}점
# 실수로 변환 : {float(score)}
# 등급 : {tier}
# """)


# # 문제 15
# words = input("이름,나이,도시를 입력하세요 : ")
# word = words.split(",")
# dic = {"name": word[0], "age": int(word[1]), "city": word[2]}

# if dic["city"] == "서울":
#     noti = "수도권 거주지입니다."
# else:
#     noti = "지방 거주자입니다."

# print(f"""
# {dic}
# 10년 뒤 나이 : {10 + dic["age"]}
# {noti}
# """)


# # 문제 16
# num = int(input("상품 번호를 입력하세요 : "))

# cart = {
#     "items": ["티셔츠", "양말", "모자"],
#     "prices": [15000, 3000, 12000],
# }

# print(f"""
# {num}번 상품 : {cart["items"][num - 1]} / {cart["prices"][num - 1]}원
# 전체 합계 : {sum(cart["prices"])}원
# """)


# # 문제 17
# name = input("요금제 명을 입력하세요 : ")
# call = int(input("이번 달 통화 사용량(분)을 입력하세요 : "))

# plans = {
#     "basic": {"기본요금": 12000, "무료통화": 100, "초과요금": 50},
#     "premium": {"기본요금": 25000, "무료통화": 300, "초과요금": 30},
# }

# if call < plans[name]["무료통화"]:
#     over = 0
# else:
#     over = call - plans[name]["무료통화"]

# if name not in plans:
#     print("없는 요금제 입니다.")
# else:
#     print(f"""
# 요금제 : {name} / 사용량 {call}분 / 초과 {over}분
# 이번 달 요금 : {plans[name]["기본요금"] + plans[name]["초과요금"] * over}원
# """)


# # 문제 18
# survey = {"질문": "개인정보 수집에 동의하십니까?", "응답": [], "동의수": 0}
# print(f"{survey['질문']}")
# is_agree = input("동의 여부 (y/n)")

# if is_agree.lower() == "y":
#     survey["응답"] = ["동의"]
#     survey["동의수"] += 1
#     print("동의해주셔서 감사합니다.")
# else:
#     survey["응답"] = "비동의"
#     print("다음엔 동의 해주세요.")

# print(f"""
# {survey}
# 마지가 응답 : {survey["응답"][0]}
# """)


# # 문제 19
# age = int(input("나이를 입력하세요 : "))
# job = input("신분을 입력하세요 : ")

# if age >= 20:
#     fee = "성인"
# elif 20 > age >= 13:
#     fee = "청소년"
# else:
#     fee = "어린이"

# ticket = {
#     "성인": {"price": 12000, "학생할인": 2000},
#     "청소년": {"price": 9000, "학생할인": 1000},
#     "어린이": {"price": 6000, "학생할인": 0},
# }

# print(f"""
# 학생 할인 {ticket[fee]["학생할인"]}원 적용
# 구분 : {fee} / 최종요금 : {ticket[fee]["price"] - ticket[fee]["학생할인"]}원
# """)


# 문제 20
cls = input("반 이름을 입력하세요 : ")
num = int(input("번호를 입력하세요 : "))

school = {
    "3학년": {
        "1반": {"teacher": "박선생", "students": ["김철수", "이영희", "박민수"]},
        "2반": {"teacher": "최선생", "students": ["정수진", "한동훈"]},
    }
}

if cls not in school["3학년"]:
    print("없는 반입니다.")
elif num > len(school["3학년"][cls]["students"]):
    print("해당 번호의 학생은 없습니다.")
else:
    print(f"""
3학년 {cls} 담임 : {school["3학년"][cls]["teacher"]}
학생 수 : {len(school["3학년"][cls]["students"])}
{num}번 학생 : {school["3학년"][cls]["students"][num - 1]}
""")

# 3학년 대신 {list(school.keys())[0]} 가능은 해
