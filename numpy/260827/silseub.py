import numpy as np

vib = np.array(
    [
        [30.1, 31.4, 29.8, 30.6, 31.0, 68.2, 30.3, 29.9],
        [32.5, 31.8, 33.0, 32.1, 31.5, 32.8, 31.9, 33.4],
        [30.9, 31.2, 8.4, 30.5, 31.7, 30.2, 31.1, 30.8],
    ]
)

print("===== 문제 1 =====")
print(vib[:, ::-2])

print("===== 문제 2 =====")
m = vib > 31
print(m.sum(axis=1))

print("===== 문제 3 =====")
avg = vib.mean(axis=1).reshape(3, 1)
std = vib.std(axis=1).reshape(3, 1)
print(((vib - avg) / std).round(2))

print("===== 문제 4 =====")
z = (vib - avg) / std
print(vib[abs(z) > 2])
for i in np.argwhere(abs(z) > 2).T:
    print(i)

print("===== 문제 5 =====")
n_vib = vib.copy()
bl = abs(z) > 2
n_vib = np.where(bl, avg.round(2), n_vib)
print(n_vib)
print(n_vib.mean(axis=1).round(2))
