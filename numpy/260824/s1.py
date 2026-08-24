#
# Numpy 배열 기초 - 배열의 이해와 생성
#

"""
[배열이 왜 필요한가]
설비 한 대가 1초에 한 번 온도를 재면 무수한 데이터가 쏟아진다.
이걸 for문으로 하나씩 하기 힘들다.

오늘은 수치 계산을 통째로 대신해 주는 새 그릇,
배열(array)를 만든다.
"""

# 리스트로 온도 3을 더하려면
temp_list = [62.1, 63.5, 71.8]

result = []
for i in temp_list:
    result.append(i + 3)
print(result)
# >> 비효율


#
# Numpy - 수치 계산 라이브러리
#

"""
[Numpy는 무엇인가]
대량의 수치를 빠르고 간결하게 다루는 파이썬 라이브러리.
Numerical Python(수치 계산을 위한 파이썬)의 줄임말

데이터 분석 도구, 인공지능 모델 다루는 도구 등
대부분 Numpy 배열 위에서 돌아감

측정값, 이미지 픽셀, 모델의 숫자 등 표현 가능
"""

import numpy as np

#
# 배열 ndarray - 수치를 담는 그릇
#

# NumPy가 수치를 담는 그릇을 배열(array)이라고 부른다.

# 정식 이름 ndarray >> 'n차원 배열(n-dimensional array)'의 줄임말

# 1차원 배열 (오늘)             2차원 배열 (통계 시간에)
# [62.1, 63.5, 71.8]        [[1 2 3]
#                            [4 5 6]]

#
# np.array로 배열 만들기
#
# 배열 만들기의 가장 기본 >> 리스트를 배열로
# np.array에 '값들을 담은 리스트'를 넣어 부르면 배열

temps = np.array([62.1, 63.5, 71.8])
print(temps)
# 리스트는 ,로 구분 / 배열은 공백으로 구분

#
# 배열 vs 리스트
#
"""
차이점   리스트 / 배열
계산    for문 / 통째로
대량속도 느림 / 빠름
"""
print(temps + 3)


#
# 같은 자료형만 - dtype
#
# 배열은 모든 값을 '같은 자료형'으로 통일해서 담는다.
mix = np.array([1, 2, 3.0])
print(mix)
# 전체 다 실수가 됨

# 배열 전체가 공유하는 자료형 >> dtype
# data type(자료형)의 줄임말

# '통일'이 배열을 빠르게 만든다


#
# dtype 확인과 지정
#
# 배열이 어떤 지료형인지 궁금하면 변수명.dtype
# '정보를 꺼내 보는 것'이라 소괄호를 안 붙임
print(temps.dtype)
# float64

# 직접 지정도 가능
# np.array(value, dtype=float)

# 정수 데이터지만 앞으로 나눗셈같은 실수 계산을 할 예정일 때 미리 실수로

#
# 0으로, 1로 채운 배열 - zeros, ones
#
# 특정 값을 미리 채운 배열을 만드는 도구

# np.zeros
print(np.zeros(3))

# np.ones
print(np.ones(4))

# 0과 1이 0., 1.처럼 소수점이 붙어 '실수'로 나옴


#
# 연속 숫자 배열 - arange
#
# 0 1 2 3처럼 연속된 숫자로 채운 배열이 필요할 땐 np.arange를 사용

print(np.arange(5, dtype=float))
# >> [0 1 2 3 4]
print(np.arange(0, 10, 2, dtype=float))


#
# 균등 분할 - linspace
#
# linspace는 개수를 정해 만듦
# 시작 값과 끝 값 사이를 몇 등분할 지 정하면 균등하게 나눠 돌려줌
print(np.linspace(0, 100, 5))
# >> [0. 25. 50. 75. 100.]
# 시작 0 끝 100 개수 5 >> 0부터 100까지 5개로 균등 분할
# 똑같은 간격 25로 나뉜 5개의 값


# arange는 인덱스 개수
# linspace는 마지막 값

# 나눠 쓰는 기준
# 간격이 정해져 있으면 >> arange
# 개수가 정해져 있으면 >> linspace


#
# 배열의 모양 - shape
#
# 정보를 꺼내 보는 것이라 소괄호는 안 붙임
print(temps.shape)
# >> (3,)
# 값이 3개 들어있는 1차원 배열

#
# 크기 size와 차원 ndim
#
# shape 말고 생김새를 알려주는 정보가 2개 더 있음
# size는 배열이 담은 '전체 값의 개수'
print(temps.size)  # 3
# ndim은 배열의 차원 값
print(temps.ndim)  # 1

"""
shape   모양(행,열)
size    전체 개수
ndim    차원
"""

# 센서 측정 값을 배열로
# 현장에서 센서가 뱉는 온도, 진동, 압력, 생산량 등 전부 배열

# 흔한 실수
# np.array(1,2,3) >> 대괄호 빼먹음


#
# 배열 만들기 절차
#
# 어떤 배열이든 네 단계로 만들고 확인
# 1) 담을 값 정하기 >> 무엇을, 몇 개?
# 2) 도구 고르기 >> 가진 값 있으면 arrya / 특정 값 채우면 zeros, ones
#                연속 숙자면 arange / 균등 분할이면 linspace
# 3) 배열 만들기 >> array는 값들을 대괄호로 감싸기
# 4) 구조 파악 >> shape, dtype, size, ndim

# [배열 생성 도구 정리]
# 상황          도구            예시 결과
# 가진 값 담기   np.array       [62.1 63.5]
# 0으로 채우기   np.zeros       [0. 0. 0.]
# 1로 채우기    np.ones         [1. 1. .1]
# 연속 숫자     np.arange       [0 2 4 6]
# 균등 분할     np.linspace     [0. 25. 50. 75. 100.]
