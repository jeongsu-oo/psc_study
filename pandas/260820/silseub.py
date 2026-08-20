import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

cafe_file = DATA / "cafe.csv"

# rows = [
#     "날짜,매장,메뉴,분류,수량,단가",
#     "2026-04-01,강남,아메리카노,커피,12,4500",
#     "2026-04-01,홍대,카페라떼,커피,8,5000",
#     "2026-04-02,강남,치즈케이크,디저트,5,6500",
#     "2026-04-02,부산,아메리카노,커피,15,4500",
#     "2026-04-03,홍대,녹차라떼,논커피,6,5500",
#     "2026-04-03,강남,카페라떼,커피,10,5000",
#     "2026-04-04,부산,크로플,디저트,7,6000",
#     "2026-04-04,홍대,아메리카노,커피,20,4500",
#     "2026-04-05,강남,녹차라떼,논커피,4,5500",
#     "2026-04-05,부산,카페라떼,커피,9,5000",
#     "2026-04-06,홍대,치즈케이크,디저트,3,6500",
#     "2026-04-06,강남,아메리카노,커피,18,4500",
# ]

# with open(cafe_file, "w", encoding="utf-8") as f:
#     for row in rows:
#         f.write(row + "\n")

# print("cafe.csv 준비 완료\n")


# 문제 1
df = pd.read_csv(cafe_file)
print(df)
df["매출액"] = df["수량"] * df["단가"]

print("\n--- 문제 1 ---")
print("크기 : ", df.shape)
print(df[["매장", "메뉴", "수량", "매출액"]].head(5))
print(f"전체 매출 :  {df['매출액'].sum():,}원")


# 문제 2
result = df.groupby("매장").agg(
    판매건수=("날짜", "count"),
    총수량=("수량", "sum"),
    총매출=("매출액", "sum"),
)

print("\n--- 문제 2 ---")
print(result)


# 문제 3
print("\n--- 문제 3 ---")
print(f"[커피 10개 이상] {len(df[(df['분류'] == '커피') & (df['수량'] >= 10)])} 건")
print(df[(df["분류"] == "커피") & (df["수량"] >= 10)])
print("[분류별 매출]")
print(df.groupby("분류")["매출액"].sum())

path = DATA / "분류별_매출.csv"
out = df.groupby("분류")["매출액"].sum()
out.to_csv(path, encoding="utf-8")
print("저장 완료 : ", path.name)
