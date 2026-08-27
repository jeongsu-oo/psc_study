#
# numpy 통계와 센서 데이터
#

"""
중심 - 평균, 중앙값
흩어짐 - 범위, iqr, 표준편차
이상치 - z-점수
"""

import numpy as np

temps = np.array([82, 85, 84, 86, 83, 88])
print(np.median(temps))
print(temps.mean().round(2))

clean = np.array([82, 85, 84, 86, 83, 88])

"""
percentile - 분위수
"""
scores = np.array([70, 74, 78, 80, 82, 86, 90, 96])
print("\n", np.percentile(scores, 50))
print("\n", np.percentile(scores, 90))

"""
표준편차 >> 평균에서 데이터가 평균적으로 떨어지는 정도
sigma^2 = sqrt( ∑(x-평균)^2 / n )
"""

print("\n진동")
vib_raw = np.array([30, 32, 31, 33, 30, 55, 32, 31])
print(np.percentile(vib_raw, 25))
print(np.percentile(vib_raw, 75))
print(np.argmax(vib_raw))
print(vib_raw[np.argmax(vib_raw)])


def detect_zscore(arr, thr=3):
    z = (arr - arr.mean()) / arr.std()  # ① 표준화
    m = np.abs(z) > thr  # ② 임계값
    return {  # ③ 골라내기 + ④ 세기
        "값": arr[m],
        "위치": np.where(m)[0],
        "개수": int(m.sum()),
        "비율": m.sum() / arr.size,
    }


v = np.array(
    [30, 32, 31, 29, 33, 30, 31, 32, 30, 29, 33, 31, 30, 32, 29, 33, 31, 65, 32, 70]
)
print(detect_zscore(v))


sen = np.array(
    [
        [84, 86, 85, 83, 86, 85, 84, 86, 85, 120],
        [30, 32, 31, 29, 33, 30, 31, 65, 30, 29],
        [55, 56, 54, 57, 55, 56, 54, 57, 55, 56],
    ]
)
q1 = np.percentile(sen, 25, axis=1)
q3 = np.percentile(sen, 75, axis=1)
print(q1)

high = q3 + 1.5 * (q3 - q1)
low = q3 - 1.5 * (q3 - q1)
print(high, low)

mask = (sen > high.reshape(3, 1)) | (sen < low.reshape(3, 1))
print(mask.sum(axis=1))

mu = sen.mean(axis=1).reshape(3, 1)
sd = sen.std(axis=1).reshape(3, 1)
z = (sen - mu) / sd
print(z.round(2))

w = np.array([0.5, 0.3, 0.2])
print(w)
score = w @ z
print(score.shape)
