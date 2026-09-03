import pandas as pd
import numpy as np
from pathlib import Path

BASE = Path(__file__).parent


df_1 = pd.DataFrame(
    [
        # 측정ID, 온도, 진동, 회전수, 압력
        [1, 72.0, 3.1, 1420, 5.2],
        [2, 75.0, 4.0, 1435, 5.0],
        [3, 71.0, 2.9, 1410, np.nan],  # 압력 결측
        [4, np.nan, 5.1, 1450, 5.3],  # 온도 결측
        [5, 120.0, 4.4, 1440, 5.1],  # 온도 이상값(튐)
        [6, 74.0, 12.0, 1425, 5.4],  # 진동 이상값(상한 초과)
        [7, 73.0, 3.3, 1415, 5.2],
        [8, 76.0, 4.1, 1430, 5.0],
        [8, 76.0, 4.1, 1430, 5.0],  # 중복(측정ID 8 반복)
        [9, 70.0, 3.0, -50, 5.1],  # 회전수 음수(물리적 불가)
        [10, np.nan, 3.8, 1445, 5.3],  # 온도 결측
        [11, 77.0, 4.5, 1438, 5.2],
        [12, 72.0, 3.2, 1418, 5.0],
        [13, 78.0, 4.7, 1442, 5.4],
        [14, 71.0, 2.8, 1408, 5.1],
        [15, 75.0, 4.0, 1428, 5.2],
    ],
    columns=["측정ID", "온도", "진동", "회전수", "압력"],
)
print("[df_1 데이터]")
print(" 행 수:", len(df_1))  # → 행 수: 16
print(" 빈 칸 총합:", int(df_1.isna().sum().sum()))  # → 빈 칸 총합: 3
print(" 회전수 최소:", df_1["회전수"].min())  # → 회전수 최소: -50
print(" 온도 최대:", df_1["온도"].max())  # → 온도 최대: 120.0


def fill_na(df):
    df = df.drop_duplicates()
    for i in ["온도", "압력"]:
        df[i] = df[i].fillna(df[i].median())
    return df


def outlier(df):
    df = df[df["회전수"] > 0].copy()
    df.loc[df["온도"] > 100, "온도"] = 100
    df.loc[df["진동"] > 10, "진동"] = 10
    return df


def seperate(df, rate=0.7):
    np.random.seed(42)
    mix = np.random.permutation(len(df))  # 복사본 반환
    range = int(len(df) * rate)
    return df.iloc[mix[:range]], df.iloc[mix[range:]]


def scaling(df, base=None):
    cols = ["온도", "진동", "회전수", "압력"]
    df = df.copy()
    if base is None:
        base = {c: {"min": float(df[c].min()), "max": float(df[c].max())} for c in cols}
    for i in cols:
        low = base[i]["min"]
        high = base[i]["max"]
        df[i] = ((df[i] - low) / (high - low)).round(3)
    return df, base


def pp_pipe(df):
    df = fill_na(df.copy())
    df = outlier(df)
    df, base = scaling(df)
    train, test = seperate(df)
    return train, test, base


train, test, base = pp_pipe(df_1)
print("\n[파이프라인 통과 결과]")
print(" 학습 행 수:", len(train))
print(" 테스트 행 수:", len(test))
print("  온도 기준 min/max : ", base["온도"]["min"], "/", base["온도"]["max"])


train.to_csv(BASE / "clean_train.csv", index=False, encoding="utf-8-sig")
test.to_csv(BASE / "clean_test.csv", index=False, encoding="utf-8-sig")

base_df = pd.DataFrame(base).T
base_df.to_csv(BASE / "scaling_base.csv", encoding="utf-8-sig")

print("\n[기준표 로딩]")
base_load = pd.read_csv(BASE / "scaling_base.csv", index_col=0, encoding="utf-8-sig")
print(base_load)

read_base = {
    col: {"min": row["min"], "max": row["max"]} for col, row in base_load.iterrows()
}
print(read_base)
