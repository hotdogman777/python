# 배열 인덱싱, 슬라이싱

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("원본 배열 arr:/n", arr)

# 양수 인덱스 (0부터 시작)
print("1번째 요소 (인덱스 0)", arr[0])
print("2번째 요소 (인덱스 0)", arr[2])
print("8번째 요소 (인덱스 0)", arr[8])


arr[0] = 100

print("1번째 요소 (인덱스 0)", arr[-1])
print("2번째 요소 (인덱스 0)", arr[-2])
print("8번째 요소 (인덱스 0)", arr[-8])

arr[-3] = 400
print("수정 후 배열 arr:\n", arr)

# 배열 슬라이싱
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print("원본 배열 arr:/n", arr)

# 펜시 인덱싱 (Fancy indexing)
indices = [1, 4, 7]
print("indices = [1, 4, 7] 선택: \n", arr[indices])


print("2부터 5까지 요소 (인덱스 0)", arr[2:5])
print("첫번째 부터 4번째까지 (인덱스 0)", arr[:4])
print("3부터 마지막 (인덱스 0)", arr[3:])
print("짝수 인덱스만: ", arr[::2])
print("홀수 인덱스만: ", arr[1::2])

# 슬라이싱으로 값 수정
arr[2:5] = 100
print("수정 후 배열 arr: \n", arr)

# new_list = [1, 2, 3, 4, 5]
# new_list[2:4] = 40
# print(new_list)

original = np.array([1, 2, 3, 4, 5])
view = original[1:4]
print("original: ", original)
print("view: ", view)

view[1:] = 20
print("original: ", original)
print("view: ", view)

# 독립적인 복사본 필요한 경우
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()

copy[0] = 100
print("original: ", original)
print("view: ", copy)

# 2차원 배열
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("2차원 배열: \n", matrix)

print("0,0요소 : \n", matrix[0, 0])
print("2,2요소 : \n", matrix[2, 2])
print("1,2요소 : \n", matrix[1, 2])
# print("3,0요소 : \n", matrix[3, 0]) error

print("-1,-2요소: ", matrix[-1, -2])
print("-1,-2요소: ", matrix[-1][-2])
print("첫번째 행: ", matrix[1])
print("첫번째 행: ", matrix[1])

print("여러 행: \n", matrix[:2])

# 부분 행렬 추출
matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])
print("[:1][:1]: \n", matrix[:2, 1:])
print("[:1][:1]: \n", matrix[1:3, 1:4])
print("[:1][:1]: \n", matrix[::2, ::2])

# 특정 행글 선택
row_indices = [0, 2, 3]
print("[0, 2, 3]행 선택: \n", matrix[row_indices])

# 특정 요소들 선택 (행, 열 인덱스)
row_indices = [0, 2, 2]
col_indices = [3, 2, 3]
print("특정 요소들 선택: \n", matrix[row_indices, col_indices])


arr = np.array([1, 5, 4, 7, 2, 3])
print("4 이상 ", arr[arr >= 4])

print("2 미만, 4 이상 ", arr[(arr >= 4) | (arr < 2)])
print("2 미만, 4 이상 ", arr[(2 <= arr) & (arr <= 4)])


matrix = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]
])
print("원본 행렬\n", matrix)
print("9보다 큰 요소들 \n", matrix[matrix > 9])

print("첫번째 열이 4 이상인 행들 \n", matrix[matrix[:, 0] >= 4])

matrix[matrix > 9] = 10
print("원본 행렬\n", matrix)
