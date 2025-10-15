# 배열 모양 변경 조작

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5, 6])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])


print(arr_1d.shape)
print(arr_1d.ndim)
print(arr_1d.size)
# arr_1d.reshape(2,)

print(arr_2d.shape)
print(arr_2d.ndim)
print(arr_2d.size)

# 기본 산술 연산
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])

print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a ** b)
print(a / b)
print(a // b)
print(a % b)

# 스칼라와의 연산
a - np.array([1, 2, 3, 4, 5])
scalar = 10

print(a + scalar)
print(a - scalar)
print(a * scalar)
print(a / scalar)
print("스칼라 / 배열", scalar / a)

a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

print(a)
print(b)

print("행렬 a + b\n", a + b)
print("행렬 a * b\n", a * b)
print("행렬 a / b\n", a / b)


a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [7, 8],
    [9, 10]
])

print(a @ b)


# 브로드 캐스팅(Broadcasting)

# 서로 다른 모양의 배열 간 연산을 가능하게 하는 Numpy 기능
arr = np.array([1, 2, 3, 4, 5])
scalar = 10

# 스칼라가 자동으로 배열 크기로 "브로드캐스트" 됨
# [1, 2, 3, 4, 5] + [10, 10, 10, 10, 10]

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

vector = np.array([10, 20, 30])

print(matrix + vector)


# 브로드캐스팅 규칙
# 규칙 1. 차원 수가 다르면 작은 쪽의 앞에 1을 추가
#
# 규칙 2. 각 차원에서 크기가 1이거나 같아야 함
# 호환 가능: (3, 1) & (1, 4) = (3, 4)

# 규칙 3.
# 규칙 4.


np.sum
np.mean
np.medium
np.std
np.max
np.min
np.var
np.ptp
