import numpy as np
import time

temps = np.array([82.0, 91.5, 78.2, 88.0, 95.1, 80.4])


t0 = time.time()
print(temps + 2)
t1 = time.time()
print(f"실행 시간 : {t1 - t0:.4f}초")

print(np.zeros_like(np.array([[1, 2, 3], [4, 5, 6]])))

a = np.array(8)
print(temps + a)


def info(x):
    print(f"shape={x.shape}, ndim={x.ndim}, dtype={x.dtype}, size={x.size}")


info(np.array(7))  # 0차원 (스칼라)
info(np.array([1, 2, 3]))  # 1차원
info(np.array([[1, 2, 3]]))  # 2차원 (1행 3열)
info(np.zeros((2, 3, 4)))  # 3차원

a = np.arange(10) * 10
print(a)

m = np.arange(12).reshape(3, 4)
print(m)
print(m[1, 2])
print(m[0:2, 1:3])
print(m[::2, ::2])

m2 = m.copy()
m2[0, 0] = 999
print(m2)
m2[:, 1] = 0
print(m2)
print(m)

m3 = m[:, 1]
print(m3)
print(np.shares_memory(m, m3))
print(m2.base is m)

print("\n문제 1")
a = np.arange(1, 21).reshape(4, 5)
print(a)
print("\n문제 2")
print(a.shape)
print(a.ndim)
print(a.dtype)
print(a.size)
print("\n문제 3")
print(a[:, 2])
print(a[:1,])
print(a[::2, ::2])
print("\n문제 4")
temps = np.array([18.5, 21.0, 23.2, 25.7, 24.1, 22.3, 19.8])
b = temps.copy()
b[0] = 0
print(b)
print(temps)
print("\n문제 5")
c = np.linspace(0, 100, 6).astype("int32")
print(c, c.dtype)

deg = np.array([0, 30, 45, 60, 90])
rad = np.deg2rad(deg)
print(rad)
"이것은 deg2rad()함수 >> 파이썬 삼각함수에는 이 함수를 사용해 변환해야 한다."


temp = np.array([-3, 12, 25, 31, 8])
print(np.where(temp >= 25, "더움", "안 더움"))
print(np.where(temp >= 25, 1, 0))

idx = np.where(temp >= 25)
print(idx)

temps2 = np.array([[-3, 12, 25], [31, 8, 26]])
idx2 = np.where(temps2 >= 25)
print(idx2)

score = np.array([-10, 45, 88, 120])
print(np.clip(score, 0, 100))

a = np.array([True, True, False])
print(a.any(), a.all())
print(np.any(score > 95), np.all(score > 20))

x = np.array([1.0, 2.0, 0.0])
with np.errstate(divide="ignore", invalid="ignore"):
    print(1 / x)
    print(np.array([0]) / np.array([0]))

grade = np.select([score >= 90, score >= 80, score >= 70], ["A", "B", "C"], default="F")
print(score)
print(grade)

# inf >> 무한대
# nan >> not a number, 정의할 수 없는 값

print(0.3 == 0.3)
print(np.isclose(0.1 + 0.2, 0.3))  # 원소별
print(np.allclose([0.1 + 0.2], [0.3]))  # 전체

#
# 연습 1
print("연습 1")
a = np.arange(1, 11)
print(np.power(a, 2))
print(a[1::2])

#
# 연습 2
print("\n연습 2")
sales = np.array([[120, 150, 90], [200, 180, 250], [90, 60, 130]])
tax = np.array([0.1, 0.05, 0.2])
print(sales * (1 + tax))

#
# 연습 3
print("\n연습 3")
scores = np.array([88, 45, 92, 67, 100, 30, 75])
print(np.where(scores >= 60, "PASS", "FAIL"))
print((scores >= 60).sum() / len(scores) * 100)

#
# 연습 4
print("\n연습 4")
data = np.array([12.0, -3.0, 250.0, 45.0, 900.0, 30.0])
print(np.clip(data, 0, 100))
print(data[(0 <= data) & (data <= 100)])

#
# 연습 5
print("\n연습 5")
X = np.array([[60.0, 70.0], [80.0, 90.0], [100.0, 50.0]])
# print((X - X.min()) / (X.max() - X.min()))
mn = X.min(axis=0)
mx = X.max(axis=0)
print((X - mn) / (mx - mn))

m = np.arange(6).reshape(2, 3)
print(m.ravel())  # n차원을 1차원으로 + view
print(m.flatten())  # n차원을 1차원으로 + copy

print("\n전치행렬")
print(m)
print(m.T)

x = np.arange(24).reshape(2, 3, 4)
print(x)
print("transpose")
print(x.transpose(1, 0, 2))
