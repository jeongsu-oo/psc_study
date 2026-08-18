#
# 함수 (수학 vs python)
#

# [수학]              [python]
# f(x) = 2x + 1     def f(x) :
#                       return 2 * x + 1
#
# x 미지수            매개변수(parameter)
# x = 3, ans = 7    x = 3, ans = 7
# x에 3을 대입        f(3) 호출
#
# f(x) = 2x + 1


def f(x):
    return 2 * x + 1


#
# return vs print
#
# return : 계산 결과 "값으로 돌려줌" >> 다시 계산에 쓸 수 있음
# print ; 화면에 보여주기만 >> 값이 안 남음

# return 있는 함수 = f(x) >> f(2) >> f(3) 계산 가능
# print만 있는 함수 = 칠판에 답만 써놓은 격, 다시 못 씀


#
# 함수값 표 만들기 (while문 복습)
#

print("x    |     f(x)")
print("-----*---------")

x = -3
while x <= 3:
    print(f"{x:3}  |    {f(x):4}")
    x += 1


# y = ax - b
# a, b 인자로 받으면 "모든 일차함수"를 하나의 함수로 표현할 수 있다.


def linear(a, b, x):
    # a >> 기울기, b >> y절편
    return a * x + b


print(linear(2, 1, 4))
print(linear(-3, 5, 2))


#
# 기울기와 y절편 구하기
#

# 두 점 (x1, y1) (x2, y2)를 지나는 직선의 기울기

#     y의 증가량    y2 - y1
# a = --------- = -------
#     x의 증가량    x2 - x1


def f(x1, y1, x2, y2):
    # 두 점을 지나는 직선의 기울기
    return (y2 - y1) / (x2 - x1)


print(f(1, 2, 3, 4))
print(f(4, 2, 1, 6))

# # eval()

# num1 = input("숫자를 입력하세요 : ")
# giho = input("기호를 입력하세요(ex. + - * ** / // %) : ")
# num2 = input("숫자를 입력하세요 : ")


# def gs(num1, giho, num2):
#     return eval(f"{num1} {giho} {num2}")


# print(gs(num1, giho, num2))


def line_eq(x1, y1, x2, y2):
    # 두 점을 지나는 기울기, y절편 호출
    a = f(x1, y1, x2, y2)
    b = y1 - a * x1
    return a, b


print(line_eq(1, 3, 4, 9))


#
# x절편 구하기 (y = 0이 되는 x)
#

# ax + b = 0
# x = -b / a


def x_in(a, b):
    # y = ax + b의 x 절편
    if a == 0:
        return
    return -b / a


print("y = 2x + 1의 x 절편", x_in(2, 1))
print("y = 3의 x 절편", x_in(0, 3))


#
# y = ax^2 + bx + cc
#

# g(x) = x^2 - 4x + 3
# g(x) = 6x^2 - 3x + 10


def g1(x):
    return x**2 - 4 * x + 3


def g2(x):
    return 6 * x**2 - 3 * x + 10


def g3(a, b, c, x):
    return a * x**2 + b * x + c
