from pathlib import Path
import csv


BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)
orders_file = DATA / "orders.csv"


with open(orders_file, "w", encoding="utf-8", newline="") as f:
    f.write("주문일,시간대,매장,메뉴,분류,수량,단가,포장\n")
    f.write("2026-03-02,오전,강남점,아메리카노,커피,3,4500,N\n")
    f.write("2026-03-02,오후,강남점,카페라떼,커피, 2 ,5000,Y\n")
    f.write("2026-03-02,오전,홍대점,녹차라떼,논커피,1,5500,N\n")
    f.write("2026-03-03,오후,강남점,치즈케이크,디저트,2,6500,Y\n")
    f.write("2026-03-03,오전,부산점,아메리카노,커피,5,4500,N\n")
    f.write("2026-03-03,오후,홍대점,아메리카노,커피,,4500,N\n")
    f.write("2026-03-04,오전,강남점,크로플,디저트,3,6000,Y\n")
    f.write("2026-03-04,오후,부산점,카페라떼,커피,4,5000,N\n")
    f.write("2026-03-05,오전,홍대점,아메리카노,커피,2,4500,Y\n")
    f.write("2026-03-05,오후,강남점,녹차라떼,논커피,3,사천,N\n")
    f.write("2026-03-06,오전,부산점,치즈케이크,디저트,1,6500,N\n")
    f.write("2026-03-06,오후,홍대점,카페라떼,커피,6,5000,Y\n")
print("orders.csv 준비 완료")
print("data 폴더에서 직접 열어보고, 이상한 값이 몇 개인지 세어 보세요.\n")


# 문제 1
print(f"{'-' * 20}\n{'문제 1 답변':>12}\n{'-' * 20}")
orders_lst = []
with open(orders_file, "r", encoding="utf-8", newline="") as f:
    for i in csv.DictReader(f):
        orders_lst.append(i)
        print(i)


# 문제 2
def clean_number(x):
    try:
        return int(str(x).strip())
    except ValueError:
        return


print(f"{'-' * 20}\n{'문제 2 답변':>12}\n{'-' * 20}")
print(f"clean_number('   3   ')     ->  {clean_number('   3   ')}")
print(f"clean_number('4500')     ->  {clean_number('4500')}")
print(f"clean_number('')     ->  {clean_number('')}")
print(f"clean_number('사천')     ->  {clean_number('사천')}")


# 문제 3
def load_orders(path):
    lst = []
    pb_lst = []
    cnt = 1
    with open(path, "r", encoding="utf-8", newline="") as f:
        for i in csv.DictReader(f):
            cnt += 1
            try:
                if not i["수량"] or not i["수량"].strip().isdigit():
                    raise ValueError(f"수량 이상 {i['수량']!r}")
                if not i["단가"] or not i["단가"].strip().isdigit():
                    raise ValueError(f"단가 이상 {i['단가']!r}")
                i["수량"] = clean_number(i["수량"])
                i["단가"] = clean_number(i["단가"])
            except ValueError as e:
                print(e)
                a = [cnt, i["메뉴"], e]
                pb_lst.append(a)
            else:
                i["금액"] = i["수량"] * i["단가"]
                lst.append(i)
        tot = 0
        for i in lst:
            tot += i["금액"]
    return lst, pb_lst, tot


good, bad, tot = load_orders(orders_file)
print(f"{'-' * 20}\n{'문제 3 답변':>12}\n{'-' * 20}")
print(f"정상 {len(good)}건 / 문제 {len(bad)}건")
for i in range(len(bad)):
    print(f"{bad[i][0]}번째 줄 {bad[i][1]} : {bad[i][2]}")
print(f"전체 매출 : {tot:,}원")


# 문제 4
def sum_by(rows, group_key, value_key):
    dic = {}
    for i in rows:
        group = i[group_key]
        value = i[value_key]
        dic[group] = dic.get(group, 0) + value
    return dic


def count_by(rows, group_key):
    dic = {}
    for i in rows:
        group = i[group_key]
        dic[group] = dic.get(group, 0) + 1
    return dic


print(f"{'-' * 20}\n{'문제 4 답변':>12}\n{'-' * 20}")
print(f'sum_by(good, "매장", "금액")    ->  {sum_by(good, "매장", "금액")}')
print(f"count_by(good, '매장')          ->   {count_by(good, '매장')}")


# 문제 5
sales_by_store = sum_by(good, "매장", "금액")


print(f"{'-' * 20}\n{'문제 5 답변':>12}\n{'-' * 20}")
for i in sales_by_store:
    print(f"{i:<6}{sales_by_store[i]:,}원   {'■' * (sales_by_store[i] // 10000)}")


# 문제 6
cnt_by_ctg = count_by(good, "분류")
sum_by_ctg = sum_by(good, "분류", "금액")
mean_by_ctg = {}
for i in cnt_by_ctg:
    mean_by_ctg[i] = round(sum_by_ctg[i] / cnt_by_ctg[i], 1)

print(f"{'-' * 20}\n{'문제 6 답변':>12}\n{'-' * 20}")
print(f"{'분류':<6}{'건수':>6}{'합계':>8}{'평균':>10}")
print("-" * 45)
for i in cnt_by_ctg:
    print(f"{i:<4}{cnt_by_ctg[i]:>8}        {sum_by_ctg[i]:,}      {mean_by_ctg[i]:,}")


# 문제 7
takeout = []
for i in good:
    if i["포장"] == "Y":
        takeout.append(i)
am = []
pm = []
for i in good:
    if i["시간대"] == "오전":
        am.append(i)
    elif i["시간대"] == "오후":
        pm.append(i)

tot = 0
for i in takeout:
    tot += i["금액"]
am_tot = 0
for i in am:
    am_tot += i["금액"]
pm_tot = 0
for i in pm:
    pm_tot += i["금액"]

print(f"{'-' * 20}\n{'문제 7 답변':>12}\n{'-' * 20}")
print(f"포장 주문 : {len(takeout)}건, {tot:,}원")
print(f"오전 매출 : {am_tot:,}원")
print(f"오후 매출 : {pm_tot:,}원")


# 문제 8
cnt_by_mu = count_by(good, "메뉴")


def best_menu(rows):
    lst = []
    for i, j in rows.items():
        if j == max(rows.values()):
            lst.append((i))
    return lst


lst = best_menu(cnt_by_mu)
print(f"{'-' * 20}\n{'문제 8 답변':>12}\n{'-' * 20}")
print(f"메뉴별 판매 수량")
for i in cnt_by_mu:
    print(f"{i:<6}{cnt_by_mu[i]}개")

print(f"가장 많이 팔린 메뉴 : {', '.join(lst)} ({cnt_by_mu[lst[0]]}개)")


# 문제 9
sales_by_store = DATA / "매장별_매출.csv"
error_lst = DATA / "오류목록.csv"

sm = sum_by(good, "매장", "금액")
cn = count_by(good, "매장")
with open(sales_by_store, "w", encoding="utf-8", newline="") as f:
    f.write("매장,주문건수,매출합계\n")
    for i in sm:
        f.write(f"{i},{cn[i]},{sm[i]}\n")

with open(error_lst, "w", encoding="utf-8", newline="") as f:
    f.write("줄번호,메뉴,사유\n")
    for i in bad:
        f.write(f"{i[0]},{i[1]},{i[2]}\n")

print(f"{'-' * 20}\n{'문제 9 답변':>12}\n{'-' * 20}")
with open(sales_by_store, "r", encoding="utf-8", newline="") as f:
    print(f.read())

with open(error_lst, "r", encoding="utf-8", newline="") as f:
    print(f.read())


# 문제 10
report = DATA / "일일보고서.txt"

with open(report, "w", encoding="utf-8", newline="") as f:
    f.write(f"""{"=" * 40}
카페 매출 보고서
{"=" * 40}
총 주문 : {len(good)}건
총 매출 : {sum(sm.values()):,}원


[매장별]
""")
    for i in sm:
        f.write(f"{i}  {sm[i]:,}원\n")
    f.write("\n[분류별]\n")
    for i in sum_by_ctg:
        f.write(f"{i}  {sum_by_ctg[i]:,}원\n")
    f.write(f"\n가장 많이 팔린 메뉴 : {', '.join(lst)}\n")
    f.write("-" * 40 + "\n")
    f.write(f"처리 실패 : {len(bad)}건")

print(f"{'-' * 20}\n{'문제 10 답변':>12}\n{'-' * 20}")
with open(report, "r", encoding="utf-8", newline="") as f:
    print(f.read())
