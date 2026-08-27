import numpy as np
import pandas as pd

path = "/Users/jones/Documents/GitHub/psc_study/numpy/260826/"
df = pd.read_csv(path + "설비_측정값.csv")
print(df)

# 문제 1
print("===== 문제 1 =====")
pv = df.pivot(index="설비", columns="시점", values="측정값")
arr = np.array(pv)
print(arr)

# 문제 2
print("\n===== 문제 2 =====")
print("평균", arr.mean(axis=1))
print("중앙값", np.median(arr, axis=1))
print("평균 - 중앙값", arr.mean(axis=1) - np.median(arr, axis=1))

# 문제 3
print("\n===== 문제 3 =====")
mn = arr.min(axis=1)
mx = arr.max(axis=1)
q1 = np.percentile(arr, 25, axis=1)
q3 = np.percentile(arr, 75, axis=1)
std = arr.std(axis=1)
print(mx - mn.round(2))
print(q1.round(3))
print(q3.round(3))
print((q3 - q1).round(2))
print(std.round(2))


# 문제 4
print("\n===== 문제 4 =====")
avg = arr.mean(axis=1).reshape(2, 1)
std = std.reshape(2, 1)
k = np.arange(1, 4)
low = avg - std * k
high = avg + std * k
print(low)
print(high)
cnt = []
for i in range(3):
    l = low[:, i].reshape(2, 1)
    h = high[:, i].reshape(2, 1)
    is_ran = (arr > l) & (arr < h)
    cnt.append(is_ran.sum(axis=1))
result = np.column_stack(cnt)
print(result)
print()
print((result / len(arr[1]) * 100).round(1))


# avg_k = avg * k
# std_k = std * k
# print((avg_k - std_k).round(2))
# print((avg_k + std_k).round(2))
# ran = (avg_k + std_k) - (avg_k - std_k)
# print(arr < ran)

# std2 = 2 * std
# std3 = 3 * std
# re1 = (avg - std).reshape(2, 1).round(2)
# re2 = (avg - std2).reshape(2, 1).round(2)
# re3 = (avg - std3).reshape(2, 1).round(2)
# print(np.hstack([re1, re2, re3]))


# 문제 5
print("\n===== 문제 5 =====")
z = (arr - avg.reshape(2, 1)) / std.reshape(2, 1)
print(z.round(2))
loc = tuple(np.argwhere(abs(z) > 2).T)
print(arr[loc].round(2), z[loc].round(2))
print(np.argwhere(abs(z) > 2))
