import numpy as np

arr1 = np.array([5, 10, 15, 20])

total = arr1.sum()
mean = arr1.mean()

print("전체 합계:", total)
print("전체 평균:", mean)
print()

arr2 = np.array([
    [3, 7, 1],
    [9, 2, 8]
])

min_val = arr2.min()
max_val = arr2.max()

print("최소값:", min_val)
print("최대값:", max_val)
print()

arr3 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

col_sum = arr3.sum(axis=0)
row_sum = arr3.sum(axis=1)

print("열 합계:", col_sum)
print("행 합계:", row_sum)
