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
