#
# 배열 기초 - 배열 통계와 형태
#
import numpy as np

#
# 통계 함수 - 반복 없이 한 줄로
#
temps = np.array([82, 91, 75, 88, 79, 95])
# tot = 0
# for i in temps:
#     tot += i
# avg = tot / len(temps)
print(temps.sum())
print(temps.mean())
print(temps.max())
print(temps.min())


#
# 표준편차와 분산 - std, var
#
"""
값들의 분산 정도
표준편차(std)^2 = 분산(var)
"""
print(temps.std())
print(temps.var())


#
# axis - 축, 방향
#

temps1 = np.array([[82, 91, 75], [88, 79, 95]])
print(temps1)

print(temps1.sum(axis=0))
print(temps1.sum(axis=1))


# axis는 shape의 자리 번호
# (행, 열) >> 행 : 0, 열 : 1
print(temps1.shape)


"""
2차원은 0이 행, 1이 열
3차원은 0이 페이지, 1이 행, 2가 열

바깥부터 0 1
2차원 구조 >> [[1,2,3],[4,5,6]]
바깥부터 0 1 2
3차원 구조 >> [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
"""


#
# axis는 모든 통계 함수에 똑같이 적용
#
# sum뿐 아니라 mean, max, min, std

print(temps1.std(axis=1))


#
# 센서 배열 통계 분석
#
sens = np.array([82, 91, 75, 88, 79, 95])  # (임의) 설비 M-101 온도
print(sens.sum())
print(sens.mean())


#
# 배치 변경 - reshape, concatenate
#

# reshape - 값은 그대로, 행 열 배치만 바꾸기
# 값은 그대로, 배치만 변경
a = np.arange(6)
b = a.copy().reshape(2, 3)
print(a)
print(b)

# concatenate - 배열 이어 붙이기
x = np.array([82, 91])
y = np.array([75, 88])
z = np.concatenate([x, y])
print(z)
z = np.concatenate([[x], [y]])
print(z)
print(z.mean())
print(z.mean(axis=1))

# [2차원을 이어 붙일 때는 axis로 방향]
# axis = 0 >> 행이 늘어남
# axis = 1 >> 열이 늘어남


#
# 조건 통계 - 경고값만 골라 평균
#
# 전체가 아니라 조건에 맞는 값만 요약하고 싶을 때 많음


#
# 실습 재료
#
# 여러 설비의 시간대별 측정값을 2차원 배열로 만들고,
# axis를 바꿔가며 열별 행별 요약을 각각 뽑은 뒤,
# 조건 통계로 기준을 넘는 값만의 요약까지 구한다.
data = np.array([[82, 91, 75], [88, 79, 95]])  # 설비 2개 시간대 3개
print(data.shape)
print("시간대별 평균 : ", data.mean(axis=0))
print((data > 85).sum())
print(data[data > 85].mean().round(2))
