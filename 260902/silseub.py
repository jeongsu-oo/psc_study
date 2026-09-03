import numpy as np
import pandas as pd
import statistics as st

rep = [1500, 1520, 1490, 1510, 1505, 1495, 1600, 1480, 1510, 1490]

# print("[평균, 중앙값, 최빈값]", np.mean(rep), np.median(rep), st.multimode(rep))
# print("[분산, 표준편차]", np.var(rep), np.std(rep).round(2))
# print("[최소, 최대, 범위]", min(rep), max(rep), max(rep) - min(rep))
# print(
#     "[q1, q3, iqr]",
#     np.percentile(rep, 25),
#     np.percentile(rep, 75),
#     np.percentile(rep, 75) - np.percentile(rep, 25),
# )


def avg(lst):
    return sum(lst) / len(lst)


def med(lst):
    s = sorted(lst)
    if len(s) % 2 == 1:
        return s[len(s) // 2]
    else:
        return (s[(len(s) // 2) - 1] + s[len(s) // 2]) / 2


def mod(lst):
    cnt = {}
    for i in lst:
        cnt[i] = cnt.get(i, 0) + 1
    m = max(cnt.values())
    return [i for i, j in cnt.items() if j == m]


def va(lst):
    a = [(x - avg(lst)) ** 2 for x in lst]
    return sum(a) / len(lst)


def stdd(lst):
    return np.sqrt(va(lst))


print("[평균, 중앙값, 최빈값]", avg(rep), med(rep), mod(rep))
print("[분산, 표준편차]", va(rep), stdd(rep).round(2))
print("[최소, 최대, 범위]", min(rep), max(rep), max(rep) - min(rep))
print(
    "[q1, q3, iqr]",
    np.percentile(rep, 25),
    np.percentile(rep, 75),
    np.percentile(rep, 75) - np.percentile(rep, 25),
)
