import numpy as np

vib = np.array([30.2, 29.8, 30.5, 30.1, 58.0, 29.9, 30.4, 55.2, 30.0, 30.3])  # 진동
temp = np.array([70.1, 69.8, 88.5, 70.2, 91.0, 70.5, 69.9, 70.3, 70.0, 69.7])  # 온도
press = np.array([5.1, 5.0, 5.2, 4.9, 5.1, 5.0, 5.3, 9.8, 5.0, 5.1])  # 압력
t10 = np.array([[30.6], [70.4], [5.2]])

print("===== 문제 1 =====")
sen = np.array([vib, temp, press])
print(sen.shape)
print(sen.mean(axis=1).round(2))

print("\n===== 문제 2 =====")
print(sen[::-1, ::2])

print("\n===== 문제 3 =====")
print(sen.max(axis=1) - sen.min(axis=1).round(2))

print("\n===== 문제 4 =====")
print(sen.mean(axis=0).round(2))

print("\n===== 문제 5 =====")
q1 = np.percentile(sen, 25, axis=1)
q3 = np.percentile(sen, 75, axis=1)
iqr = q3 - q1
print(iqr)
print(q3 + 1.5 * iqr)
print(q1 - 1.5 * iqr)

print("\n===== 문제 6 =====")
high = q3 + 1.5 * iqr
low = q1 - 1.5 * iqr
mask = (high.reshape(3, 1) < sen) | (low.reshape(3, 1) > sen)
print(mask.sum(axis=1))

print("\n===== 문제 7 =====")
for i in np.argwhere(mask == True).T:
    print(i)
print(sen[mask])

print("\n===== 문제 8 =====")
both = mask[:2, :].all(axis=0)
least = mask[:2, :].any(axis=0)
print(np.where(both == True)[0])
print(np.where(least == True)[0])

print("\n===== 문제 9 =====")
fixed = np.where(mask, np.median(sen, axis=1).reshape(3, 1), sen)
print(fixed.mean(axis=1))

print("\n===== 문제 10 =====")
# add_t = np.concatenate((fixed, t10), axis=1)
add_t = np.hstack([fixed, t10])
print(add_t.shape)
print(add_t[:, -2:].mean(axis=1).round(2))
