import pandas as pd
from pathlib import Path

BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)

sales_file = DATA / "sales2.csv"

rows = [
    "주문일,지점,사원,분류,상품,수량,단가",
    "2026-03-02,강남,김철수,가전,노트북,3,1200000",
    "2026-03-02,강남,김철수,주변기기,마우스,10,25000",
    "2026-03-03,홍대,이영희,가전,모니터,4,350000",
    "2026-03-03,부산,박민수,주변기기,키보드,8,45000",
    "2026-03-04,강남,김철수,가전,노트북,2,1200000",
    "2026-03-04,홍대,,주변기기,마우스,15,25000",
    "2026-03-05,부산,박민수,가전,모니터,,350000",
    "2026-03-05,강남,최지은,주변기기,키보드,12,45000",
    "2026-03-06,홍대,이영희,가전,노트북,1,1200000",
    "2026-03-06,부산,박민수,주변기기,마우스,20,25000",
    "2026-03-09,강남,최지은,가전,모니터,5,350000",
    "2026-03-09,홍대,정하늘,주변기기,키보드,6,",
    "2026-03-10,부산,박민수,가전,노트북,2,1200000",
    "2026-03-10,강남,김철수,주변기기,마우스,7,25000",
]

# with open(sales_file, "w", encoding="utf-8") as f:
#     for row in rows:
#         f.write(row + "\n")

df = pd.read_csv(sales_file)
print("데이터 준비 완료:", df.shape[0], "건")

# groupby
df["매출액"] = df["수량"] * df["단가"]
df.groupby("지점")["매출액"].mean()

# [groupby의 3단계]
# 1) 쪼갠다 >> 지점별로 데이터를 나눔
# 2) 계산한다 >> 각 덩어리마다 합계나 평균을 낸다
# 3) 합친다 >> 결과를 하나의 표로 모은다

# pd.options.display.float_format = "{:.2f}".format
print("[지점별 매출 합계]")
print(df.groupby("지점")["매출액"].sum())
print("\n[지점별 매출 평균]")
print(df.groupby("지점")["매출액"].mean().round(2))
print("\n[지점별 주문 건수]")
print(df.groupby("지점").size())


#
# 자주 쓰는 계산 함수 - sum(), mean(), count(), max(), min()
#
g = df.groupby("지점")["매출액"]
print(dict(g.sum()))
"""
count()     개수(빈 값 제외)
size()      개수(빈 값 포함)
median()    중앙값
std()       표준편차
nunique()   서로 다른 값의 개수
"""


#
# 한 번에 여러 계산하기 - agg
#
# 합계도 보고 평균도 보고 건수도 보고~
result = df.groupby("지점")["매출액"].agg(["sum", "mean", "count", "max"])
print(result)
"""
agg에 리스트로 넘기면 여러 계산을 한 번에 한다
숫자가 1.452500e_06처럼 나오는 건 >> 지수 표기
1.4524 * 10^6이란 뜻
보기 불편하면 round()로 제거
"""

# 열 이름도 바꾸고 싶으면 이렇게

# 열 이름 지정하는 방법
result2 = df.groupby("지점").agg(
    총매출=("매출액", "sum"),
    평균매출=("매출액", "mean"),
    건수=("매출액", "count"),
    총수량=("수량", "sum"),
    #  새로운 열 / 열 / 계산 함수
)
print(result2.round(2))


#
# 두 개 이상 묶기
#
print("[지점 + 분류별 매출]")
result = df.groupby(["지점", "분류"])["매출액"].sum()
print(result)


# 결과를 다시 DataFrame으로 만들기
print("[표 형태로 보기] reset_index()")
r = df.groupby(["지점", "분류"])["매출액"].sum().reset_index()
print(r)


#
# 실전 - 정렬해서 순위 보기
#
print("\n[매출 1위 사원부터]")
top = df.groupby("사원")["매출액"].sum().sort_values(ascending=False)
print(top)

# 상위 3명
print(top.head(3))

# 가장 잘 팔린 상품
best = df.groupby("상품")["수량"].sum().sort_values(ascending=False)
print(best)
print("\n1등 : ", best.index[0], ">>", int(best.iloc[0]), "개")


#
# 빠진 값 찾기
#
# pandas는 빈 값을 NaN으로 표시
# Not a Number >> NaN

print(df.isnull().sum())

print(df[df.isnull().any(axis=1)])  # axis=0 >>
"""
axis = 0 >> 열 방향
axis = 1 >> 행 방향
"""

#
# 빠진 값 채우기 >> fillna
#
# 어떻게 채울지, 데이터의 성격에 따라 다름
# 정답이 없으니 상황에 맞게 판단

# 방법 1) 0으로 채우기 - 수량이나 금액일 경우
df_fill = df.copy()  # 원본을 지키려고 복사본
df_fill["수량"] = df_fill["수량"].fillna(0)
# 수량 0으로
print(df_fill[["상품", "수량"]].head(8))

# 방법 2) 평균으로 채우기 - 단가처럼 대표값이 있을 때
avg_price = df["단가"].mean()
df_fill["단가"] = df_fill["단가"].fillna(avg_price)
print(f"\n단가를 평균 {avg_price:,.0f}원으로 채움")

# 방법 3) 글자로 채우기 - 이름같은 문자열
df_fill["사원"] = df_fill["사원"].fillna("미지정")
print(df_fill[df_fill["사원"] == "미지정"][["주문일", "지점", "사원"]])


"""
어떻게 채울지 정하는 기준
수량, 건수 >> 0
금액, 점수 >> 평균, 중앙값
이름, 분류 >> ex 미지정
시계열 데이터 >> 앞의 값으로 (ffill)
"""

#
# 빠진 값이 있는 행 지우기 - dropna()
#

print("원본 : ", len(df), "건")

"""
dropna() 옵션

df.dropna()     하나라도 비어 있으면 행 삭제
df.dropna(subset=['수량'])   수량이 빈 행만 삭ㅈ
df.dropna(how = 'all')      모든 칸이 비어 있을 때만 삭제
df.dropna(axis=1)           빈 값이 있는 열 삭제

판단 기준
빈 값이 전체 5% 미만        삭제해도 큰 영향 x
빈 값이 많음 (30% 이상)     채우거나, 그 열을 아예 빼기
핵심 열(매출액 등)이 비었음   그 행은 쓸 수 없으니 삭제
"""


#
# 중복 처리
#

print("중복된 행 개수 : ", df.duplicated().sum())
print("사원 이름 중복 개수 : ", df.duplicated(subset="사원").sum())

# 중복 제거
df_unique = df.drop_duplicates(subset=["사원"])
print("사원별 첫 주문만 남기면 : ", len(df_unique), "건")
print(df_unique[["사원", "지점"]])

"""
drop_duplicates 옵션

keep = 'first'        첫번째만 남김 (default)
keep = 'last'         마지막만 남김
keep = False          중복된 거 모두 삭제
"""


#
# 날짜로 변환
#
# csv에서 읽은 날짜는 그냥 문자열
# 날짜로 바꿔야 월별 집계나 요일 분석 가능

print("변환 전 자료형 : ", df["주문일"].dtype)
df["주문일"] = pd.to_datetime(df["주문일"])
print("변환 후 자료형 : ", df["주문일"].dtype)
print(df["주문일"].head(3))

# 날짜 정보 꺼내기 - .dt를 붙인다.
df["월"] = df["주문일"].dt.month
df["일"] = df["주문일"].dt.day
df["요일"] = df["주문일"].dt.day_name()

# 날짜에서 꺼낸 정보
print(df[["주문일", "월", "일", "요일"]].head(5))

"""
.dt로 꺼낼 수 있는 것들

.dt.year        년
.dt.month       월
.dt.day         일
.dt.dayofweek   요일 (0 = 월요일 ~ 6 = 일요일)
.dt.day_name()  요일이름 (영어)
.dt.hour        시
.dt.minute      분
.dt.second      초
.dt.time        시:분:초
.dt.quarter     분기
"""

#
# 요일 한글로 바꾸기
#
# 딕셔너리 만들어서 map으로 바꾼다
week_kr = {
    "Monday": "월",
    "Tuesday": "화",
    "Wednesday": "수",
    "Thursday": "목",
    "Friday": "금",
    "Saturday": "토",
    "Sunday": "일",
}

df["요일한글"] = df["요일"].map(week_kr)
print(df[["주문일", "요일", "요일한글"]].head())


#
# 날짜로 집계하고 필터링
#

# 요일별 매출
print(df.groupby("요일한글")["매출액"].sum())
# 날짜별 매출
daily = df.groupby("주문일")["매출액"].sum()
print(daily)
# 특정 날짜 이후
recent = df[df["주문일"] >= "2026-03-06"]
print(recent[["주문일", "지점", "매출액"]])

"""
날짜로 바꿔두면 부등호 비교가 됨
문자열도 되긴 한데 날짜로 바꾸면 기능이 많으니 추천
"""


#
# 엑셀 피벗 테이블
#
# groupby로 두 개를 묶으면 결과가 계단처럼 나옴
# 이걸 가로 세로 표로 만들어 주는 게 pivot_table

# 엑셀 피벗 테이블을 써 보셨다면 같은 개념

# groupby
print(df.groupby(["지점", "분류"])["매출액"].sum())

# pivot_table
pivot = df.pivot_table(
    index="지점",
    columns="분류",
    values="매출액",
    aggfunc="sum",
)
print(pivot)

# 합계 행과 열 추가
pivot2 = df.pivot_table(
    index="지점",
    columns="분류",
    values="매출액",
    aggfunc="sum",
    margins=True,  # 합계 추가
    margins_name="합계",
)
print(pivot2)

pivot3 = df.pivot_table(
    index="사원",
    columns="분류",
    values="수량",
    aggfunc="sum",
    fill_value=0,
)
print(pivot3)


#
# csv 저장
#
out1 = DATA / "지점별_매출.csv"
summary = (
    df.groupby("지점")
    .agg(
        총매출=("매출액", "sum"),
        평균매출=("매출액", "mean"),
        건수=("매출액", "count"),
    )
    .round(0)
)
summary.to_csv(out1, encoding="utf-8-sig")
print(f"저장 완료 : {out1.name}")
print(summary)
"""
to_csv 옵션
df.to_csv('파일.csv', encoding = 'utf-8-sig')
    엑셀에서 한글이 안 깨짐

df.to_csv('파일.csv', index = False)
    맨 왼쪽 인덱스 번호를 빼고 저장
    groupby 결과가 아닌 일반 데이터는 보통 이걸 사용

df.to_csv('파일.csv', columns = ['지점','매출액'])
    원하는 열만 저장
"""

# 일반 데이터를 저장할 때 index = False
out2 = DATA / "정리된_주문내역.csv"
df.to_csv(out2, encoding="utf-8-sig", index=False)
print(f"저장 완료 : {out2.name}")

# 저장한 파일 다시 읽어서 확인
check = pd.read_csv(out2)
print("다시 읽어보기 : ", check.shape)  # (행 개수, 열 개수)


# 엑셀로 저장

try:
    out3 = DATA / "매출보고서.xlsx"

    # 여러 시트 나눠 저장
    with pd.ExcelWriter(out3) as writer:
        df.to_excel(writer, sheet_name="전체내역", index=False)
        summary.to_excel(writer, sheet_name="지점별요약")
        pivot.to_excel(writer, sheet_name="피벗")

    print(f"저장 완료 : {out3.name}")
except ImportError:
    print("openpyxl이 설치되지 않았습니다.")

"""
엑셀 저장의 장점
  - 여러 시트로 나눌 수 있습니다
  - 받는 사람이 바로 열어봅니다
  - 서식이 유지됩니다

CSV의 장점
  - 가볍고 빠릅니다
  - 어떤 프로그램에서든 열립니다

보고용이면 엑셀, 데이터 주고받기용이면 CSV를 쓰세요.
"""

#
# 실전 - 보고서를 만드는 전체 흐름
#

# 1) 읽기
report = pd.read_csv(sales_file)

# 2) 정리 - 빠진 값 정리
report["수량"] = report["수량"].fillna(0)
report["단가"] = report["단가"].fillna(report["단가"].mean())
report["사원"] = report["사원"].fillna("미지정")

# 3) 계산 - 새 열 만들기
report["매출액"] = report["수량"] * report["단가"]
report["주문일"] = pd.to_datetime(report["주문일"])

# 4) 집계
by_branch = (
    report.groupby("지점")
    .agg(
        건수=("매출액", "count"),
        총매출=("매출액", "sum"),
        평균=("매출액", "mean"),
    )
    .round(0)
    .sort_values("총매출", ascending=False)
)

# 5) 출력
print("[지점별 실적]")
print(by_branch)

# 6) 저장
final = DATA / "최종보고서.csv"
by_branch.to_csv(final, encoding="utf-8-sig")
print(f"\n저장 완료 : {final.name}")

"""
[groupby]

df.groupby("열")["값열"].sum()          묶어서 합계
df.groupby(["열1","열2"])["값"].mean()   두 기준으로
df.groupby("열").agg(
    이름=("값열", "sum"),
)                                      여러 계산 한 번에
.reset_index()                          결과를 표로 되돌리기


[빠진 값]

df.isnull().sum()            열별 빈 값 개수
df["열"].fillna(0)            0으로 채우기
df["열"].fillna(df["열"].mean())   평균으로 채우기
df.dropna()                  빈 값 있는 행 삭제
df.dropna(subset=["열"])      특정 열만 확인해서 삭제
df.drop_duplicates()         중복 제거


[날짜]

pd.to_datetime(df["열"])     문자열을 날짜로
df["열"].dt.month            월 꺼내기
df["열"].dt.day_name()       요일 이름
df["열"].map({...})          값 바꾸기


[피벗]

df.pivot_table(
    index="세로", columns="가로",
    values="값", aggfunc="sum",
    margins=True, fill_value=0,
)


[저장]

df.to_csv("파일.csv", encoding="utf-8-sig", index=False)
df.to_excel("파일.xlsx", index=False)


[반드시 기억할 5가지]
1. groupby 는 "무엇으로 묶어서, 어느 열을, 어떻게 계산할지"
2. 빈 값은 채울지 지울지 데이터 성격을 보고 판단한다
3. 날짜는 to_datetime 으로 바꿔야 .dt 기능을 쓸 수 있다
4. 저장할 때 encoding="utf-8-sig" 를 잊지 말자
5. 실무 흐름은 읽기-정리-계산-집계-출력-저장
"""
