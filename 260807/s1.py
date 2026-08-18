#
# break, continue
#

for i in range(1, 10):
    if i == 5:
        break
    print(i)  # 1 2 3 4

for i in range(1, 6):
    if i == 3:
        continue  # 건너 뛰고 계속
    print(i)

# break >> 반복문 전체 종료
# continue >> 이번 회차 skip


#
# 중첩 반복문
#

for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i}x{j}={i * j}")
    print()

# # 정삼각형
# n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i), "*" * (2 * i - 1))

# #     *     4
# #    ***    3
# #   *****   2
# #  *******  1
# # ********* 0


n = 5
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ********* 0
#  *******  1
#   *****   2
#    ***    3
#     *     4

for i in range(9, 1, -1):
    for j in range(9, 0, -1):
        print(f"{i}x{j}={i * j}")
    print()

##############

n = 5
for i in range(1, 2 * n):
    if i <= n:
        print(" " * (n - i) + "*" * (2 * i - 1))
    else:
        print(" " * (i - n) + "*" * ((2 * n - 1) - (i - n) * 2))


#                 i   별
#     *       4   1
#    ***      3   2
#   *****     2   3
#  *******    1   4
# *********   0   5   9
#  *******    1   6   7
#   *****     2   7   5
#    ***      3   8   3
#     *       4   9   1


# 알면 좋은 기능

fruits = ["사과", "바나나", "포도"]

for i, fruit in enumerate(fruits):
    print(f"{i}번 : {fruit}")

# enumerate() >> 번호와 값을 한번에

for i, j in enumerate(fruits, 1):  # 1번부터
    print(f"{i}번 : {j}")

names = ["철수", "영희"]
ages = [25, 22]

for i, j in zip(names, ages):
    print(f"{i} : {j}살")

#
# 시그마 (∑) - 수학 기호
#

# 모양
#  5
#  ∑ i^2
# i=1
