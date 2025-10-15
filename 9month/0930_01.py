import numpy as np

arr = np.arange(10, 30, 2)
indices = [1, 3, 5]
print("문제 1: ", arr[indices])

arr = np.arange(1, 10).reshape(3, 3)
row_indices = [0, 1, 2]
col_indices = [0, 1, 2]
print("문제 2: ", arr[row_indices, col_indices])

arr = np.arange(1, 13).reshape(3, 4)
arr[:, 3:] = -1
print("문제 3: \n", arr)
print()
arr = np.arange(1, 17).reshape(4, 4)
print(arr[::-1, :])
print(arr[:, ::-1])
print()

arr = np.arange(1, 21).reshape(4, 5)
print(arr)
sub = arr[1:3, 1:4].copy()
print(sub)

arr = np.array([1, 2, 3, 4])
print(arr + 3)

# arr = np.array([5, 10], [15, 20])
# print(arr * -1)
