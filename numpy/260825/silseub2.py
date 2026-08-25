import numpy as np

temp = np.array(
    [
        [71.2, 68.5, 75.9, 80.1, 66.3],
        [69.8, 72.4, 78.2, 85.6, 70.0],
        [74.1, 70.9, 69.5, 77.3, 81.8],
    ]
)

print("===== 문제 1 =====")
print(temp[::-1, ::2])

print("\n===== 문제 2 =====")
print((temp > 72).sum(axis=1))

print("\n===== 문제 3 =====")
avg = temp.mean(axis=1).reshape(3, 1)
avgs = np.hstack((avg, avg, avg, avg, avg))
print(temp - avgs)

print("\n===== 문제 4 =====")
norm = (temp - temp.mean()) / temp.std()
print(norm.round(2))

print("\n===== 문제 5 =====")
t6 = np.array([[70.5], [74.2], [79.6]])
new = np.concatenate([temp, t6], axis=1)
print(new.shape)
print(new[:, 4:].mean(axis=1))

print("\n===== 문제 6 =====")
base = np.linspace(70, 78, 5)
print((temp > base).sum(axis=0))

print("\n===== 문제 7 =====")
temp_ran = temp[(temp < 70) | (temp > 80)]
print(temp_ran)
print(temp_ran.std().round(3))

print("\n===== 문제 8 =====")
a = np.arange(1, 13).reshape(3, 4)
b = np.arange(1, 13).reshape(4, 3)
print(a.sum(axis=0))
print(b.sum(axis=0))
"""
열별 합 >> 행들의 합 >> axis = 0 >> 열 개수 차이
값들이 같아도 행렬 구조가 다르면 다르다
"""

print("\n===== 문제 9 =====")
temp_cp = temp.copy()
temp_cp[temp_cp < 70] = 70
temp_cp[temp_cp > 85] = 85
print(temp_cp.std(axis=1).round(2))

print("\n===== 문제 10 =====")
idx = np.arange(3)
bl = (temp.mean(axis=1) >= 73) & (temp.std(axis=1) >= 4)
print(idx[bl])

print("\n문제3번 추가 코드")
avg = temp.mean(axis=1).reshape(3, 1)
print(temp - avg)
