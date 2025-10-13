import numpy as np

# 실습 1번
arr1 = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
r = arr1.ravel()
print(r)
r[0] = 999
print(r)
print()

f = arr1.flatten()
print(f)
f[0] = 999
print(f)
print()

# 실습 2번
img = np.random.rand(32, 32)

arr = np.expand_dims(img, axis=0)
print(arr.shape)
print()

img = np.random.randint(0, 255, (1, 28, 28, 1))

arr = np.squeeze(img, axis=None)
print(arr.shape)
print()

arr = np.array([
    [3, 1, 2, 2],
    [1, 2, 3, 1],
    [2, 2, 1, 4]
])

a = np.sort(np.unique(arr))
print(a)
print()

# 실습2 1번
a = np.array([
    [1, 2],
    [3, 4]
])
b = np.array([
    [5, 6]
])
axis = 0
result1 = np.concatenate((a, b), axis=0)
print(result1)
print()

# 실습 2 2번
a = np.arange(12)
splits_equal = np.split(a, 3)
print(splits_equal)

# 실습2 3번
a = np.array([1, 2])
b = np.array([3, 4])
c = np.array([5, 6])

arr = np.stack((a, b, c), axis=0)
print(arr)

# 실습2 4번
a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
b = np.array([
    [7, 8, 9],
    [10, 11, 12]
])

arr = np.stack((a, b), axis=0)

print("배열:\n", arr)
print("shape:", arr.shape)

# 실습2 5번
arr = np.arange(8)

splits = np.split(arr, [2, 5])

for i, sub in enumerate(splits, start=1):
    print(f"부분 {i}", sub)
print()

# 실습2 6번
a = np.ones((2, 3))
b = np.zeros((2, 3))

arr0 = np.stack((a, b), axis=0)
print(arr0.shape)
print()

# 실습3 1번
arr = np.array([7, 2, 9, 4, 5])

asc = np.sort(arr)

desc = np.sort(arr)[::-1]

print("원본:", arr)
print("오름차순:", asc)
print("내림차순:", desc)

# 실습3 2번
arr2 = np.array([
    [9, 2, 5],
    [3, 8, 1]
])
sorted_rows = np.sort(arr2, axis=1)

print("원본:\n", arr2)
print("행 별 정렬:\n", sorted_rows)

# 실습3 3번
arr = np.array([10, 3, 7, 1, 9])

idx = np.argsort(arr)

sorted_arr = arr[idx]

print("원본:", arr)
print("정렬 인덱스:", idx)
print("정렬 결과:", sorted_arr)

# 실습3 4번
arr = np.array([
    [4, 7, 2],
    [9, 1, 5],
    [6, 8, 3]
])

sorted_col = np.sort(arr, axis=0)

print("원본:\n", arr)
print("열 기준 정렬:\n", sorted_col)
