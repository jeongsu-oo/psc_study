import numpy as np
import pandas as pd

path = "/Users/jones/Documents/GitHub/psc_study/numpy/260827/"
df = pd.read_csv("설비로그.csv", parse_dates=["시각"], encoding="utf-8-sig")
COLS = ["진동", "온도", "압력", "유량"]
# print(df)


print("===== 문제 1 =====")
print(df[COLS].isnull().sum())

a = df[COLS].isnull().sum().to_frame(name="결측").T  #
print(a)

b = df[["설비", "시각", "센서", "메운값"]].interpolate(method="time")
print(b)
