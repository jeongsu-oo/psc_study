#
# 튜플 - 수정 불가 리스트
#

point = (10, 20)
color = ("빨", "초", "파")
print(type(color))  # tuple

point2 = 10, 20  # 괄호 생략해도 튜플
print(point2)  # (10, 20)

# ========== 주의 ============
# 값이 하나면 쉼표를 꼭 붙여야 한다.
not_tuple = 10  # 그냥 숫자 10 (괄호가 계산으로 해석됨)
yes_tuple = (10,)  # 이래야 튜플

# 사용법
color = ("red", "green", "blue")
print(color[0])  # red
print(color[-1])  # blue

# append x, del x, 새로 대입 o

# 실수로 바뀌면 안 되는 값일 경우 사용
SCREEN = (1920, 1000)
BIRTH = (2000, 5, 15)

# 리스트보다 조금 빠르고 가볍다.
# 딕셔너리의 키로 쓸 수 있다. (리스트 x)

a, b = 1, 2
a, b = b, a
print(a, b)
