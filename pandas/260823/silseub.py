import pandas as pd
from pathlib import Path
import random
import csv

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

# random.seed(42)  # 항상 같은 데이터가 나오게 고정

# products = [
#     ("노트북", "가전", 1200000),
#     ("모니터", "가전", 350000),
#     ("키보드", "주변기기", 45000),
#     ("마우스", "주변기기", 25000),
#     ("이어폰", "주변기기", 89000),
#     ("가습기", "생활", 65000),
#     ("텀블러", "생활", 28000),
# ]
# channels = ["웹", "앱", "전화"]
# regions = ["서울", "경기", "부산", "대구", "광주"]
# members = ["일반", "실버", "골드", "VIP"]

orders_file = DATA / "orders.csv"

# lines = ["주문번호,주문일,고객등급,채널,지역,상품,분류,수량,단가"]

# order_no = 1000
# for month in [1, 2, 3]:
#     for day in range(1, 29):
#         # 하루에 0~4건
#         for _ in range(random.randint(0, 4)):
#             order_no += 1
#             name, cat, price = random.choice(products)
#             qty = random.randint(1, 5)
#             grade = random.choice(members)
#             ch = random.choice(channels)
#             rg = random.choice(regions)

#             # 일부러 이상한 값을 섞습니다
#             r = random.random()
#             if r < 0.03:
#                 qty_text = ""  # 빈 값
#             elif r < 0.05:
#                 qty_text = "세개"  # 숫자가 아님
#             else:
#                 qty_text = str(qty)

#             if random.random() < 0.04:
#                 grade = ""  # 등급 누락

#             lines.append(
#                 f"ORD{order_no},2026-{month:02d}-{day:02d},{grade},{ch},{rg},"
#                 f"{name},{cat},{qty_text},{price}"
#             )

# with open(orders_file, "w", encoding="utf-8") as f:
#     for line in lines:
#         f.write(line + "\n")

# print(f"orders.csv 준비 완료 ({len(lines) - 1}건)\n")

# 1단계
print("\n---------1단계 출력---------")
orders = pd.read_csv(orders_file)
print("크기")
print(orders.shape)
print("앞 5줄")
print(orders.head())
print("열별 자료형")
orders.info()
print("열별 빈 값 개수")
print(orders.isnull().sum())
print("숫자 열 요약")
print(orders.describe().round(2))
"""
수량 열이 int64가 아닌 이유?
>> 만들 때 결측치를 NaN이라 하지 않고 빈 문자열과 세개라는 문자열 값이 있기 때문
"""


# 2단계
print("\n---------2단계 출력---------")
orders["수량"] = pd.to_numeric(orders["수량"], errors="coerce")
print(orders["수량"].isnull().sum())
orders = orders.dropna(subset="수량")
orders["고객등급"] = orders["고객등급"].fillna("일반")
orders["수량"] = orders["수량"].astype(int)
print("  크기 : ")
print(orders.shape)
print("  빈 값 개수 : ")
print(orders.isnull().sum())


# 3단계
orders["매출액"] = orders["수량"] * orders["단가"]
orders["주문일"] = pd.to_datetime(orders["주문일"])
orders["월"] = orders["주문일"].dt.month
week_kr = {
    "Monday": "월",
    "Tuesday": "화",
    "Wednesday": "수",
    "Thursday": "목",
    "Friday": "금",
    "Saturday": "토",
    "Sunday": "일",
}
orders["요일"] = orders["주문일"].dt.day_name().map(week_kr)
orders["대형주문"] = orders["매출액"] >= 500000
print("\n---------3단계 출력---------")
print(orders[["주문일", "월", "요일", "상품", "수량", "매출액", "대형주문"]].head())

# 4단계
print("\n---------4단계 출력---------")
print(f"전체 주문 : {len(orders)}건")
print(f"전체 매출 : {orders['매출액'].sum():,}원")
print(f"평균 주문 : {int(orders['매출액'].mean()):,}원")
maxi = orders["매출액"].max()
print(f"최대 주문 : {maxi:,}원 ({orders[orders['매출액'] == maxi]['상품'].iloc[0]})")
rate = orders["대형주문"].sum() / len(orders) * 100
print(f"대형주문 비율 : {rate:.1f}%")


# 5단계
print("\n---------5단계 출력---------")
groupby_cate = orders.groupby("분류")["매출액"].agg("sum").sort_values(ascending=False)
print("분류별")
print(groupby_cate)
groupby_local = orders.groupby("지역").agg(
    주문건수=("매출액", "count"),
    매출합계=("매출액", "sum"),
)
print("\n지역별")
print(groupby_local)
groupby_cn = orders.groupby("채널")["매출액"].sum()
print("\n채널별")
print(groupby_cn)
groupby_tier = orders.groupby("고객등급").agg(
    주문건수=("매출액", "count"),
    총매출=("매출액", "sum"),
    평균주문액=("매출액", lambda x: int(x.mean().round(0))),
)
print("\n고객등급별")
print(groupby_tier)


# 6단계
def mon_tot(mon):
    return orders[orders["월"] == mon]["매출액"].sum()


def mon_cnt(mon):
    return orders[orders["월"] == mon]["매출액"].count()


def chg_rate(mon1, mon2):
    tot_mon1 = orders[orders["월"] == mon1]["매출액"].sum()
    tot_mon2 = orders[orders["월"] == mon2]["매출액"].sum()
    rate = (tot_mon2 - tot_mon1) / tot_mon1 * 100
    return rate.round(1)


def mk_bar(amount):
    bar = "*" * (amount // 1000000)
    return bar


print("\n---------6단계 출력---------")
for i in range(3):
    if i == 0:
        print(f"{i + 1}월   {mon_tot(i + 1):,}원  {mk_bar(mon_tot(i + 1))}")
    else:
        print(
            f"{i + 1}월   {mon_tot(i + 1):,}원  {mk_bar(mon_tot(i + 1)):<45} ({chg_rate(i, i + 1)}%)"
        )


# 7단계

print("\n---------7단계 출력---------")
print(
    orders[orders["고객등급"] == "VIP"]
    .groupby("고객등급")
    .agg(
        주문건수=("매출액", "count"),
        총매출=("매출액", "sum"),
    )
)
# sudo = orders[(orders["지역"] == "서울") | (orders["지역"] == "경기")]
# print("\n수도권 비중 : ", round(len(sudo) / len(orders) * 100, 1), "%")
sudo = orders[orders["지역"].isin(["서울", "경기"])]
print("\n수도권 비중 : ", round(len(sudo) / len(orders) * 100, 1), "%")
print(
    "\n앱+50만원이상 주문 건수 : ",
    len(orders[(orders["채널"] == "앱") & (orders["매출액"] >= 500000)]),
)
# print("가전X 매출 합계 : ", orders[~(orders["분류"] == "가전")]["매출액"].sum())
print(f"가전X 매출 합계 : {orders[orders['분류'] != '가전']['매출액'].sum():,}원")
print(
    f"폰이 들어간 상품명 판매 수량 : {orders[orders['상품'].str.contains('폰')]['수량'].sum()}"
)


# 8단계
print("\n---------8단계 출력---------")
pv1 = orders.pivot_table(
    index="지역",
    columns="분류",
    values="매출액",
    aggfunc="sum",
    fill_value=0,
    margins=True,
    margins_name="합계",
)
print(pv1)
pv2 = orders.pivot_table(
    index="고객등급",
    columns="채널",
    values="매출액",
    aggfunc="count",
    fill_value=0,
)
print(pv2)
"""
매출이 가장 큰 지역 (지역, 분류)은?
>> 광주, 가전
"""

# 9단계
print("\n---------9단계 출력---------")
print(
    orders[["주문번호", "주문일", "상품", "수량", "매출액"]]
    .sort_values("매출액", ascending=False)
    .head()
)
rk_sales = orders.groupby("상품")["수량"].sum().sort_values(ascending=False)
print("\n판매 수량 top3 : ", ", ".join(rk_sales.head(3).index))
tot_sales = groupby_local["매출합계"].sort_values(ascending=False)
most_rate = round(tot_sales.max() / tot_sales.sum() * 100, 2)
print(f"\n가장 매출이 많은 지역 {tot_sales.idxmax()} / 비중 {most_rate}%")
print("\n요일별 매출 : ")
week_order = ["월", "화", "수", "목", "금", "토", "일"]
groupby_day = orders.groupby("요일")["매출액"].sum()
print(groupby_day.reindex(week_order))

# 10단계
path1 = DATA / "주문내역_정리.csv"
orders.to_csv(path1, encoding="utf-8-sig", index=False)

path2 = DATA / "지역별_매출.csv"
groupby_local.to_csv(path2, encoding="utf-8-sig")

path3 = DATA / "월별_매출.csv"
groupby_mon = orders.groupby("월")["매출액"].sum()
groupby_mon.to_csv(path3, encoding="utf-8-sig")

path4 = DATA / "매출리포트.xlsx"
with pd.ExcelWriter(path4) as writer:
    orders.to_excel(writer, sheet_name="전체내역", index=False)
    groupby_local.to_excel(writer, sheet_name="지역별")
    groupby_mon.to_excel(writer, sheet_name="월별")

print("\n---------10단계 출력---------")
result1 = pd.read_csv(path1)
print(result1.shape)
result2 = pd.read_csv(path2)
print(result2.shape)
result3 = pd.read_csv(path3)
print(result3.shape)
result4_1 = pd.read_excel(path4, sheet_name="전체내역")
print(result4_1.shape)
result4_2 = pd.read_excel(path4, sheet_name="지역별")
print(result4_2.shape)
result4_3 = pd.read_excel(path4, sheet_name="월별")
print(result4_3.shape)
