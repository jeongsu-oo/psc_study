import math
import random
import numpy as np

temp = [71.2, 68.5, 75.9, 80.1, 66.3, 72.4, 69.8, 95.6, 70.0, 73.1, 68.9, 71.5]
temp_str = ["71.2", "68.5", "이상", "80.1", "N/A"]

print("\n === 문제 1 ===")


def mk_avg(lst):
    sm = 0
    for i in lst:
        sm += i
    return round(sm / len(lst), 2)


print(mk_avg(temp))
print(mk_avg([70.0, 72.0, 74.0]))

print("\n === 문제 2 ===")


def mk_tier(v, c=75, d=90):
    if v >= d:
        return "이상"
    if v >= c:
        return "주의"
    return "정상"


print(mk_tier(temp[7]), mk_tier(temp[2]), mk_tier(temp[0]))
print(mk_tier(temp[2], 80, 100), mk_tier(temp[2]))


print("\n === 문제 3 ===")


def summary(lst):
    sm = 0
    mx = lst[0]
    mn = lst[0]
    for i in lst:
        sm += i
        if mx < i:
            mx = i
        if mn > i:
            mn = i
    avg = round(sm / len(lst), 2)
    return [sm, avg, mx, mn]


print(*summary(temp))  # 언패킹..!


print("\n === 문제 4 ===")
base = 75


def cnt_base_over(lst):
    cnt = 0
    for i in lst:
        if i > base:
            cnt += 1
    return cnt


print(cnt_base_over(temp), base)

print("\n === 문제 5 ===")
print(math.sqrt(16), round(math.pi, 4), math.ceil(73.61), math.floor(73.61))
random.seed(42)
print(random.randint(0, 11), random.randint(0, 11), random.randint(0, 11))
random.seed(42)
print(random.randint(0, 11), random.randint(0, 11), random.randint(0, 11))

print("\n === 문제 6 ===")
lst = []
err = []
for i in temp_str:
    try:
        lst.append(float(i))
    except ValueError:
        err.append(i)
print(lst, "\n", err, "\n", len(lst), len(err))

print("\n === 문제 7 ===")
from pathlib import Path
import csv

BASE = Path(__file__).parent
file = BASE / "설비온도기록.csv"
with open(file, "r", encoding="utf-8-sig", newline="") as f:
    rd = csv.reader(f)
    hd = next(rd)
    LST = list(rd)
print(f"""{hd}
{len(LST)}
{LST[0]} {float(LST[0][1])}""")


print("\n === 문제 8 ===")
tp_lst = []
for i in LST:
    tp_lst.append(float(i[1]))
a = f"측정 {len(tp_lst)}회 / 평균 {mk_avg(tp_lst)} / 최고 {summary(tp_lst)[2]}"
file2 = BASE / "점검보고서.txt"
with open(file2, "w", encoding="utf-8-sig", newline="") as f:
    f.write(a)
with open(file2, "r", encoding="utf-8-sig", newline="") as f:
    print(f.read())


print("\n === 문제 9 ===")


class Sensor:
    def __init__(self, nm, lst):
        self.nm = nm
        self.lst = lst

    def avg(self):
        return mk_avg(self.lst)

    def introd(self):
        return f"{self.nm} 센서 / 측정 {len(self.lst)}회 / 평균 {mk_avg(self.lst)}"


s = Sensor("범용", temp)
print(s.nm, s.avg())
print(s.introd())


print("\n === 문제 10 ===")


class Temp_sensor(Sensor):
    def __init__(self, nm, lst, limit=90):
        super().__init__(nm, lst)
        self.limit = limit

    def cnt_lim_over(self):
        cnt = 0
        for i in self.lst:
            if i >= self.limit:
                cnt += 1
        return cnt

    def introd(self):
        return f"{self.nm} 센서 / 측정 {len(self.lst)}회 / 평균 {mk_avg(self.lst)}"


ts = Temp_sensor("온도", temp)
print(ts.introd())
print(ts.cnt_lim_over(), ts.limit)


print("\n === 문제 11 ===")


class Vib_sensor(Sensor):
    def __init__(self, nm, lst, limit=35):
        super().__init__(nm, lst)
        self.limit = limit

    def introd(self):
        return f"[{self.nm}] {self.nm} / 평균 {mk_avg(self.lst)} / 한계 {self.limit}"


v = [30.1, 31.4, 41.2, 29.8]
vs = Vib_sensor("진동", v)
print(vs.introd())
print(ts.introd())
print(isinstance(vs, Sensor), isinstance(vs, Temp_sensor))  #


print("\n === 문제 12 ===")
lst = [ts, vs]
for i in lst:
    print(i.introd())


print("\n === 문제 13 ===")
arr_t = np.array(temp)
print(arr_t.shape, arr_t.dtype)
print(arr_t.sum().round(1), arr_t.mean().round(2), arr_t.max(), arr_t.min())
print(arr_t + 3)


print("\n === 문제 14 ===")
print(arr_t[arr_t > 75])
print(np.where(arr_t > 75)[0])
print(((arr_t > 75).sum() / len(arr_t) * 100).round(1))


print("\n === 문제 15 ===")
arr_csv = np.array(LST)
arr_temp = np.array(tp_lst)
print(arr_csv.shape, len(arr_temp))


def a(arr, lim=3):
    avg = arr.mean().round(2)
    std = arr.std().round(2)
    z = (arr - avg) / std
    over = arr[abs(z) > lim]
    idx = np.where(abs(z) > lim)[0]
    return avg, std, over, idx


print(*a(arr_temp)[0:2])
print(*a(arr_temp)[2:], len(a(arr_temp)[2]))
print(*a(arr_temp, 2)[2:], len(a(arr_temp, 2)[2]))
print(round(len(a(arr_temp, 2)[2]) / len(arr_temp) * 100, 2))
