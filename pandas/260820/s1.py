# 터미널 >> pip3 install pandas numpy openpyxl
import pandas as pd
import numpy as np
import openpyxl as wb
from pathlib import Path

print(pd.__version__)
print(np.__version__)
print(wb.__version__)
# 터미널 >> pip3 list
# 가상환경 만들면 python3만 쓰는 독립적인 방이라 3 안 붙여도 됨


#
# pandas - 데이터 읽고 살펴보기
#


BASE = Path(__file__).parent
DATA = BASE / "data"
DATA.mkdir(exist_ok=True)
rows = [
    "주문일,지점,사원,분류,상품,수량,단가",
    "2026-03-02,강남,김철수,가전,노트북,3,1200000",
    "2026-03-02,강남,김철수,주변기기,마우스,10,25000",
    "2026-03-03,홍대,이영희,가전,모니터,4,350000",
    "2026-03-03,부산,박민수,주변기기,키보드,8,45000",
    "2026-03-04,강남,김철수,가전,노트북,2,1200000",
    "2026-03-04,홍대,이영희,주변기기,마우스,15,25000",
    "2026-03-05,부산,박민수,가전,모니터,3,350000",
    "2026-03-05,강남,최지은,주변기기,키보드,12,45000",
    "2026-03-06,홍대,이영희,가전,노트북,1,1200000",
    "2026-03-06,부산,박민수,주변기기,마우스,20,25000",
    "2026-03-07,강남,최지은,가전,모니터,5,350000",
    "2026-03-07,홍대,정하늘,주변기기,키보드,6,45000",
]

sales_file = DATA / "sales_file.csv"
# with open(sales_file, "w", encoding="utf-8") as f:
#     for i in rows:
#         f.write(i + "\n")
print("실습데이터 준비 완료 : ", sales_file.name)


#
# DataFrame
#

# pandas의 핵심, 줄여서 df
# 엑셀 시트와 거의 비슷, 표

# 가로가 row 행
# 세로가 column 열
# 리스트와 인덱스와 같은 개념


# [지금까지 뭐가 다른가]
# 한 줄씩 읽어서 딕셔너리 만들고 for문으로 하나씩 처리
# >> 행 단위 사고 방식

# pandas
# 표 전체로 통째로 올려놓고, 열 단위로 한꺼번에 계산
# >> 열 단위 사고 방식

# 딕셔너리로 DataFrame을 만들 수 있다
# 키가 열, 값이 데이터

data = {
    "이름": ["김철수", "이영희", "박민수"],
    "부서": ["영업", "개발", "개발"],
    "연봉": [4500, 5200, 4800],
}
df_test = pd.DataFrame(data)
print(df_test)
print(type(df_test).__name__)

# DataFrame >> 클래스, df_test >> 객체
# df_test.head()처럼 점을 찍는 거 >> 매서드


#
# 열 하나는 series
#
# DataFrame에서 열 하나만 선택하면 series라는 다른 자료형이 됨

salary = df_test["연봉"]
print(salary)
print(salary.sum())
print(salary.mean().round(2))
print(salary.max())


#
# 데이터 읽기
#

df = pd.read_csv(sales_file)
print(df)
print(df[:1])

# read_csv에서 자주 쓰는 옵션

# pd.read_csv(경로)
# 기본 utf-8

# 근데 깨지면 cp949로 인코딩
# pd.read_csv(경로, encoding = 'cp949')
# 그래도 안 되면
# pd.read_csv(경로, encoding = 'utf-8-sig')

# pd.read_csv(경로, header = None)
# 첫 줄이 헤더가 아니라 데이터일 때

# pd.read_csv(경로, usecols=['지점','수량'])
# 필요한 열만 읽기. 파일이 클 떄 유용


#
# 자료형을 알아서 판단해 준다
#

# csv 모듈로 읽으면 모든 값이 문자열이다
# '4500' + '5200' >> '45005200'

# pandas는 열마다 자료형을 알아서 판단

print(df.dtypes)
"""
object 문자열 (파이썬의 str)
int64 정수
float64 실수
bool True/False
"""

print(df["수량"].sum(), "개")


#
# 처음 받는 데이터 파악하기
#

# 1) df.shape >> 크기
print(df.shape)  # 괄호 없네 - 속성
# 2) df.head() >> 위에 5개
print(df.head())  # 괄호 있네 - 매서드
# 3) df.info() >> 정보
df.info()
# 4) df.describe() >> 숫자열 요약 정보
# pd.set_option('display.float_format', lambda x: f'{x:,.1f}')
pd.options.display.float_format = "{:.2f}".format
print(df.describe())

# df.tail >> 뒤에 5개
print(df.tail())

"""
info() 읽는법
Non-Null Count >> 값이 들어가는 갯수, 전체 행보다 적으면 빈칸이 있다.
Dtype >> 자료형
memory uage >> 메모리 사용량
"""
# 빈칸 세기
print(df.isnull().sum())


# 문자열 열까지 보고 싶으면
# include='all'을 쓰면 모든 열을 다 보여준다
print(df.describe(include="all"))
"""
문자열 읽는 법
count >> 개수
unique >> 서로 다른 값이 몇 종류인지
top >> 가장 많이 나온 값
freq >> top이 얼마나 나왔는지

NaN이 보이는 칸은 '이 열은 해당 없음'
문자열 열엔 평균이 없다.
"""


#
# 어떤 값이 들어오나 - unique, value_counts
#

print("지점 종류 : ", df["지점"].unique())
print("지점 종류 : ", df["지점"].nunique(), "곳")

print("\n[지점별 등장 횟수]")
print(df["지점"].value_counts())

print("\n[분류별 등장 횟수]")
print(df["분류"].value_counts())

# value_counts()는 개수를 세서 많은 순으로 정렬


#
# 열 꺼내기
#
# 열 하나 >> Series(1차원)
print(df["상품"].head(3))
print("자료형 : ", type(df["상품"]).__name__)

# 열 여러 개 >> DataFrame(2차원)
# 대괄호가 두 겹인 거 주의
print(df[["상품", "수량"]].head(3))
print("자료형 : ", type(df[["상품", "수량"]]).__name__)

"""
대괄호 개수 주의
df['상품'] >> Series(열 하나)
df[['상품','수량']] >> Series(열 여러개)

안쪽 대괄호는 리스트
"""

#
# 새 열 만들기 - 계산해서 추가
#

df["매출액"] = df["수량"] * df["단가"]  # 벡터 연산
df["부가세"] = df["매출액"] * 0.1
df["총액"] = df["매출액"] + df["부가세"]
print(df[["상품", "수량", "단가", "매출액"]].head(3))


# 조건으로 새 열 만들기
df["대형거래"] = df["매출액"] >= 1000000
print(df[["상품", "매출액", "대형거래"]].head(3))


# 이름 바꾸기 - 딕셔너리 {옛 이름 : 새 이름}
df2 = df.rename(columns={"사원": "담당자"})
print("바꾼 뒤 열 목록", list(df2.columns))

# 열 지우기
df3 = df.drop(columns=["부가세", "총액"])
print("\n 지운 뒤 열 목록 : ", list(df3.columns))

print("\n 원본 : ", list(df.columns))
"""
원본은 변하지 않는다.

sorted()와 .sort()의 차이
pandas의 대부분 매서드는 sorted()처럼 동작
원본은 건드리지 않고 새 것만 만들어 돌려준다.

그래서 결과를 쓰려면 반드시 변수에 담아야 함

df.drop(columns = ['부가세']) << 아무 일도 안 일어남
df = df.drop(columns = ['부가세']) << 이래야 원본에 반영
"""

# df[조건]
location = df["지점"] == "강남"
print(location)

print("\n[강남 지점만]")
gn = df[df["지점"] == "강남"]
print(gn.head())

print("\n[매출액 100만원 이상]")
big = df[df["매출액"] >= 1000000]
print(big)


#
# 조건 여러 개 걸기
#
# and >> & (앰퍼샌드)
# or >> | (파이프)
# not >> ~ (물결)

print(
    "강남과 매출 100 이상 : \n", df[(df["지점"] == "강남") & (df["매출액"] >= 1000000)]
)
print("\n강남 아님 홍대 : \n", df[(df["지점"] == "강남") | (df["지점"] == "홍대")])
# print("\n강남이 아닌 곳 : \n", df[~df["지점"] == "강남"])


# 목록에 포함되는지 확인 - isin
# or 여러 번 대신 이게 편함
print("[isin - 목록에 포함되는 것]")
result = df[df["지점"].isin(["강남", "부산"])]
print(len(result), "건")

# 문자열에 포함 확인 str.contains
print("\n[str.contains - 글자가 들어간 것]")
result = df[df["상품"].str.contains("노트")]
print(result[["상품", "매출액"]])


# 정렬하기

# 매출액 큰 순서로
print("매출액 높은 순 상위 5건")
top5 = df.sort_values("매출액", ascending=False).head(5)
print(top5[["지점", "상품", "수량", "매출액"]])

# 여러 기준 정렬
print("\n[지점 이름순, 그 안에서 매출 높은 순]")
sorted_df = df.sort_values(["지점", "매출액"], ascending=[True, False])
print(sorted_df[["지점", "상품", "매출액"]])


"""
sort_values 옵션
ascending 오름차순 여부
"""


#
# 특정 행 꺼내기 - loc와 iloc
#

# iloc 숫자 위치로 찾기
# loc 이름표(인덱스)로 찾기

print("[iloc - 숫자 위치]")
print("[첫번째 행]")
print(df.iloc[0])
print("\n[앞 3행, 앞 4열]")
print(df.iloc[0:3, 0:4])
print("\n[loc 이름으로]")
print("0번 인덱스의 상품 열", df.loc[0, "상품"])
print("\n0~2번 행의 지저모가 매출액")
print(df.loc[0:2, ["지점", "매출액"]])

"""
구분법
iloc[0] 맨 앞 행(위치 기준)
loc[0] 인덱스가 0인 행(이름 기준)

iloc[0:3] 0, 1, 2 행 (끝 번호 제외 - 리스트와 같음)
loc[0:3] 0, 1, 2, 3 행 (끝 번호 포함 - 이름 기준이라 그런 듯)
범위 지정할 때 끝 번호 포함 여부가 다르다.
헷갈리면 iloc을 쓰라.
"""


#
# 정리
#
"""
[처음 데이터 받으면 이 순서로]
df = pd.read_csv('파일.csv')
df.shape        크기
df.head()       앞 5개
df.info()       구성
df.describe()   숫자형 요약

[열 다루기]
df["열"]                  열 하나 (Series)
df[["열1", "열2"]]         열 여러 개 (DataFrame)
df["새열"] = df["A"] * df["B"]   계산해서 추가
df.rename(columns={...})   이름 바꾸기
df.drop(columns=[...])     열 지우기

[행 다루기]
df[df["열"] == 값]                조건 필터
df[(조건1) & (조건2)]              and
df[(조건1) | (조건2)]              or
df[df["열"].isin([...])]          목록에 포함
df[df["열"].str.contains("글자")]  문자 포함
df.sort_values("열", ascending=False)   정렬

[반드시 기억할 5가지]
1. import pandas as pd  (별칭은 pd 로 고정)
2. 속성은 괄호 없이(df.shape), 메서드는 괄호(df.head())
3. 대부분의 메서드는 원본을 안 바꾼다. 변수에 담아라
4. 조건 여러 개는 & | ~ 를 쓰고 각각 괄호로 감싼다
5. 열끼리 계산하면 for 문 없이 전체 행에 적용된다
"""
