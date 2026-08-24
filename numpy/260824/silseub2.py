import numpy as np

temps = np.array([78.5, 84.0, 91.2, 87.6, 80.1, 95.4, 83.3, 89.9])

# 문제 1
print("\n=============== 문제 1 ===============")
print(temps[0])
print(temps[3])
print(temps[-1])


# 문제 2
print("\n=============== 문제 2 ===============")
print(temps[-3])


# 문제 3
print("\n=============== 문제 3 ===============")
print(temps[:3])
print(temps[-4:])
print(temps[2:5])


# 문제 4
print("\n=============== 문제 4 ===============")
fixed = np.array(
    [78.5, 84.0, 91.2, 87.6, 80.1, 95.4, 83.3, 89.9]
)  # temps와 같은 값의 별도 배열
fixed[2] = 85.0
print(fixed)


# 문제 5
print("\n=============== 문제 5 ===============")
print(temps - 1.2)


# 문제 6
print("\n=============== 문제 6 ===============")
celsius = np.array([0.0, 37.0, 100.0])
print(celsius * 1.8 + 32)


# 문제 7
print("\n=============== 문제 7 ===============")
am = np.array([80.0, 88.5, 79.8])
pm = np.array([83.0, 87.0, 82.0])
print(pm - am)

# 문제 8
print("\n=============== 문제 8 ===============")
print(temps > 88)

# 문제 9
print("\n=============== 문제 9 ===============")
print(temps[temps > 88])
print(temps[temps < 80])

# 문제 10
print("\n=============== 문제 10 ===============")
print(np.sum(temps > 88))

# 문제 11
print("\n=============== 문제 11 ===============")
print(np.sqrt(np.array([16.0, 36.0, 81.0])))
print(np.round(temps, 0))

# 문제 12
print("\n=============== 문제 12 ===============")
print(np.round((temps - temps.min()) / (temps.max() - temps.min()), 2))

# 문제 13
print("\n=============== 문제 13 ===============")
try:
    p = np.array([1.0, 2.0, 3.0, 4.0])
    q = np.array([1.0, 2.0])
    print(p + q)
except ValueError as e:
    print(e)
"""
배열의 길이가 달라서 불가능
(4,)이랑 (2,)는 계산이 안 됨
"""


# 문제 14
print("\n=============== 문제 14 ===============")
vib = np.array([3.6, 3.9, 4.0, 4.3, 3.7, 4.1])
fix = vib * 1.05
print(np.round(fix[fix > 4.0], 2))
print(np.sum(fix > 4.0))
print(np.round(fix[fix > 4.0].mean(), 2))
