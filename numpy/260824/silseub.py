import numpy as np

# 문제 1
pressure_list = [101.3, 102.7, 99.8]
ps_arr = np.array(pressure_list)
print("=============== 문제 1 ===============")
print(ps_arr)


# 문제 2
arr_a = np.array([1.5, 2.5, 3.5])
arr_b = np.array([10, 20, 30])
print("\n=============== 문제 2 ===============")
print(arr_a.dtype)
print(arr_b.dtype)


# 문제 3
a = [4, 5, 6]
print("\n=============== 문제 3 ===============")
print(np.array(a, dtype=float))


# 문제 4
print("\n=============== 문제 4 ===============")
print(np.zeros(5))
print(np.ones(4))


# 문제 5
print("\n=============== 문제 5 ===============")
print(np.arange(1, 10, 2))


# 문제 6
print("\n=============== 문제 6 ===============")
print(np.linspace(0, 1, 5))


# 문제 7
print("\n=============== 문제 7 ===============")
vib = np.array([3.2, 3.8, 4.1, 3.5])
print(vib.shape)
print(vib.size)
print(vib.ndim)


# 문제 8
print("\n=============== 문제 8 ===============")
wrong = np.array([70, 75, 80])
print(wrong)


# 문제 9
print("\n=============== 문제 9 ===============")
value = np.array([12.5, 13.1, 11.9, 12.8])
print(value)
print(value.dtype)
print(value.shape)
