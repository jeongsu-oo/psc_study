# 문제 1
# answer = 7
# cnt = 0

# while True:
#     cnt += 1
#     num = int(input("숫자를 입력하세요 : "))
#     if num > answer:
#         print("더 작게!")
#     elif num < answer:
#         print("더 크게!")
#     else:
#         print(f"정답! {cnt}번 만에 맞췄습니다.")


# 문제 2
# cart = []

# while True:
#     duct = input("상품 입력(stop -> '그만'입력)")
#     if duct == "그만":
#         break
#     else:
#         cart.append(duct)
# print(f"{cart} / 총 {len(cart)}개")


# 문제 3
# scores = []

# while True:
#     scr = int(input('점수 입력 (stop -> "-1"입력)'))
#     if scr > 100:
#         print("잘못된 점수입니다.")
#     elif scr == -1:
#         print(
#             f"평균 : {round(sum(scores) / len(scores), 1)} / 최고 : {max(scores)} / 최저 : {min(scores)}"
#         )
#     else:
#         scores.append(scr)


# 문제 4
# word_count = {}
# while True:
#     word = input('단어 입력 (stop -> "end"입력)')
#     if word == "end":
#         print(word_count)
#         break
#     elif word in word_count:
#         word_count[word] += 1
#     elif word not in word_count:
#         word_count[word] = 1
# for i, j in word_count.items():  # items()
#     print(f"{i} : {j}개")


# 문제 5
# menu = {"콜라": 1500, "사이다": 1300, "물": 800}
# money = 5000
# bought = []

# while True:
#     drink = input("음료 이름을 입력하세요 : ")
#     if drink == "종료" or money < min(menu.values()):
#         print(f"""산 음료 목록 : {bought}
# 남은 돈 : {money}원""")
#         break
#     elif drink not in menu:
#         print("그런 음료는 없습니다.")
#     elif menu[drink] > money:
#         print("잔액이 부족합니다.")
#     else:
#         bought.append(drink)
#         money = money - menu[drink]
