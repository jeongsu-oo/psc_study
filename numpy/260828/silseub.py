설비명 = "M-101"
담당자 = "김정비"
센서ID = "TEMP-M101-A-0007"
온도 = [71.2, 68.5, 75.9, 80.1, 66.3, 72.4, 69.8, 95.6, 70.0, 73.1, 68.9, 71.5]
측정값문자 = ["71.2", "68.5", "75.9", "80.1"]
점검메모 = "  정상가동 / 진동 약간 있음  "

print("\n == 문제 1 == ")
print(f"설비 {설비명} / 담당 {담당자} / 측정 {len(온도)}회")
print(type(설비명).__name__, type(len(온도)).__name__, type(온도[0]).__name__)

print("\n == 문제 2 == ")
print(" ".join(센서ID.split("-")))
print(센서ID[:4], 센서ID[-4:])

print("\n == 문제 3 == ")
print(점검메모.strip())
print(점검메모.strip().replace("/", "·"))
print(센서ID.lower(), 센서ID.startswith("TEMP"), 센서ID.index("M101"))

print("\n == 문제 4 == ")
lst = []
for i in 측정값문자:
    lst.append(float(i))
print(lst)
print(round(sum(lst) / len(lst), 2))

print("\n == 문제 5 == ")
print(len(온도) // 5, len(온도) % 5, 2**5)
print(온도[0] > 70 and 온도[0] < 75)
print(온도[7] >= 90 or 온도[4] <= 60)

print("\n == 문제 6 == ")
if 온도[7] >= 90:
    print(온도[7], "이상")
elif 온도[7] >= 75:
    print(온도[7], "주의")
else:
    print(온도[7], "정상")

print("\n == 문제 7 == ")
cnt1 = 0
cnt2 = 0
cnt3 = 0
for i in 온도:
    if i >= 90:
        cnt1 += 1
    elif i >= 75:
        cnt2 += 1
    else:
        cnt3 += 1
print(cnt3, cnt2, cnt1)

print("\n == 문제 8 == ")
sm = 0
mx = 온도[0]
mn = 온도[0]
for i in 온도:
    sm += i
    if i > mx:
        mx = i
    if i < mn:
        mn = i
avg = round(sm / len(온도), 2)
print(sm, "\n", avg, "\n", mx, mn)

print("\n == 문제 9 == ")
for i in range(len(온도)):
    while 온도[i] >= 90:
        print(i, 온도[i])
        break

print("\n == 문제 10 == ")
cnt = 0
for i in 온도:
    if i >= 75:
        continue
    cnt += 1
print(cnt)
for i in range(0, len(온도), 4):
    print(i, 온도[i])

print("\n == 문제 11 == ")
print(sorted(온도)[:3])
print(sorted(온도, reverse=True)[:3])
print(온도[3:7], 온도[-3:])

print("\n == 문제 12 == ")
cp = 온도.copy()
cp.remove(95.6)
cp.append(70.5)
cp.insert(0, 69.0)
print(len(cp), cp[0], cp[-1])
print(온도.index(80.1), cp.index(71.2))

print("\n == 문제 13 == ")
dic = {"M-101": 71.2, "M-102": 78.4, "M-203": 85.0}
dic["M-305"] = 66.8
print(list(dic.keys()))
print(round(sum(dic.values()) / len(dic), 2))
print("없음" if "M-999" not in dic else dic)

print("\n == 문제 14 == ")
tier = ["정상", "주의", "정상", "이상", "정상", "주의"]
uni_tier = list(set(tier))
print(uni_tier, len(uni_tier))
a, b, c = ("M-101", "A라인", 2019)
print(f"{a}({b}) 사용 {2026 - c}년차")

print("\n == 문제 15 == ")
val_lst = []
idx_lst = []
for i in range(len(온도)):
    if 온도[i] > 75:
        val_lst.append(온도[i])
        idx_lst.append(i)
print(val_lst)
print(idx_lst)
print(round(len(val_lst) / len(온도) * 100, 2))
