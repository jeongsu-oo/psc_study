import numpy as np


table = np.array([[80, 90, 70], [60, 50, 40]])
print("===문제1===")
print(table)

print("\n===문제2===")
print(table.shape)

print("\n===문제3===")
print(table[0, 1])

print("\n===문제4===")
print(table[1,])

print("\n===문제5===")
print(table.sum())

print("\n===문제6===")
print(table.sum(axis=0))

print("\n===문제7===")
print(table.sum(axis=1))

print("\n===문제8===")
print(table.mean(axis=1))

print("\n===문제9===")
print(table.max(axis=0))

print("\n===문제10===")
print(table.max(axis=1))
"""
설비별 최댓값 >> 행별 최댓값 >> 열 값들 중 최댓값 >> axis = 1(열)
"""
