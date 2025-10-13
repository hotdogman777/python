import numpy as np
from collections import deque


# Deque
# 덱 Deque, Double_Ended Queue
# 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료 구조
# 스택과 큐의 특성을 모두 가지고 있어, 매우 유연한 자료구조
# "deck"으로 발음

# 특징
# 1. 양방향 연상 (Double_ended)
#     앞쪽(front) 뒤쪽(rear) 모두에서 요소의 추가 제거가 가능 하다.
# 2. 0(1) 시간 복잡도
#     양쪽 끝에서의 모든 연산이 상수 시간에 수행된다.
# 3. 동적 크기
#     필요에 따라 크기가 자동으로 조절
# 4. 스택과 큐 동시 구현
#     하나의 자료구조로 스택과 큐를 몯 구현할 수 있다.
# 5. 회전 연산 지원
#     요소들을 좌우로 회전시킬 수 있다.

# 주요 연산:
#     append(x) 오른쪽 끝에 요소 추가
#     appendleft(x) 왼쪽 끝에 요소 추가

#     pop()   # 오른쪽 끝 요소 제거 및 반환
#     popleft()   # 왼쪽 끝 요소 제거 및 반환

#     extend(iterable)    # 오른쪽 여러 요소 추가
#     extendleft(iterable) # 왼쪽 여러 요소 추가

#     rotate(n)   # n만큼 회전
#     clear()    # 모든 요소 제거


# 회문(palindrome) 검사
# level ->

def is_palindrome(s):
    # 덱을 이용한 회문 검사
    dq = deque(s)

    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False


is_palindrome("level")
is_palindrome("tomato")

# ===================================================
# 차원수 추가와 제거
# newaxis 와 expand_dims
# 새로운 차원을 추가ㅏ여 브로드 캐스팅이나 연산을 가능하게 한다.


arr = np.array([1, 2, 3, 4, 5])
print("원본: \n", arr)
print("모양", arr.shape)

# newaxis
row_vec = arr[np.newaxis, :]
print("행 벡터: \n", row_vec)
print("행 벡터: \n", row_vec.shape)
print()

col_vec = arr[:, np.newaxis]
print("열 벡터 \n", col_vec)
print("열 벡터 \n", col_vec.shape)
print()

arr_expanded0 = np.expand_dims(arr, axis=0)
arr_expanded1 = np.expand_dims(arr, axis=1)

print("axis=0\n", arr_expanded0)
print("axis=1\n", arr_expanded1)

# squeeze
arr = np.array([[[1, 2, 3]]])
print("원본 \n", arr)
print("모양 \n", arr.shape)
print()

squeeze = np.squeeze(arr)
print("squeeze \n", squeeze)
print("squeeze 모양 \n", squeeze.shape)
print()

squeeze0 = np.squeeze(arr, axis=0)
print("squeeze0 \n", squeeze0)
print("squeeze0 모양 \n", squeeze0.shape)
print()

# 배열 평탄화 Flattening

# flatten: 항상 복사본 반환 (안전하지만 메모리 사용)
# ravel: 가능 하면 뷰 반환 ()

flattened = arr.flatten()
print("flattened 결과: ", flattened)
flattened[0] = 999

print("2차원 배열")
print(arr)
print("flattened 결과: ", flattened)

raveled = arr.ravel()
print("raveled 결과: ", raveled)
raveled[0] = 999
print()

print("2차원 배열")
print(arr)
print("raveled 결과: ", raveled)
print()

raveled_copy = arr.ravel().copy()
raveled_copy[1] = 999

print("2차원 배열")
print(arr)
print("raveled_copy 결과: ", raveled_copy)
print()

arr = np.array([1, 2, 3, 2, 2, 1, 3, 1, 5, 6, 3, 3])
uniq, idx, inv, cnt = np.unique(arr,
                                return_index=True,
                                return_inverse=True,
                                return_counts=True)
print("고유값", uniq)
print("첫 등장 인덱스", idx)
print("원본 -> 고유값 인덱스", inv)
print("등장 횟수", cnt)
print()
print()
print()
print()
print()
# 배열 결합 (Concatenation)
# 배열 이어 붙이기
# 같은 차원의 배열들을 특정 축을 따라 연결
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([7, 8, 9])

concat_id = np.concatenate([a, b, c])
print("결합 결과", concat_id)

# 2차원 배열
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# axis = 0
concat_v = np.concatenate([A, B], axis=0)
print("axis = 0 (수직결합):")
print(concat_v)
print(concat_v.shape)
print()
# axis = 1
concat_h = np.concatenate([A, B], axis=1)
print("axis = 1 (수평결합):")
print(concat_h)
print(concat_h.shape)
print()

# vstack, hstack
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

vstacked = np.vstack([a, b])
print("v stack: ", vstacked)
print()

hstacked = np.hstack([a, b])
print("h stack: (수평)", hstacked)
print()

# 배열 분할
# split

# 하나의 배열을 여러개의 작은 배열로 나누는 작업
# 데이터를 배치로 나누거나 훈련/검증 세트로 분리할때 사용
arr = np.arange(12)
print(arr)
print()

splits_equal = np.split(arr, 3)  # 3개로 균등 분할
print(splits_equal)
for i, sub in enumerate(splits_equal):
    print(i+1, sub)
print()

splits_idx = np.split(arr, [2, 10])  # 엔덱스 3, 7에서 분할 (해당 하는 인덱스에서 분할)
for i, sub in enumerate(splits_idx):
    print(i+1, sub)
print()

arr = np.arange(24).reshape(4, 6)
# [[ 0  1  2  3  4  5]
#  [ 6  7  8  9 10 11]
#  [12 13 14 15 16 17]
#  [18 19 20 21 22 23]]
print(arr)

row_splits = np.split(arr, 2, axis=0)
for i, sub in enumerate(row_splits):
    print(i+1, sub)
print()

col_splits = np.split(arr, 2, axis=1)
for i, sub in enumerate(col_splits):
    print(i+1, sub)
print()

arr = np.array([3, 1, 3, 2, 5])
sorted_copy = np.sort(arr)
print(sorted_copy)

arr.sort()
print(arr)
print()
arr2 = np.array([
    [2, 1, 5],
    [3, 2, 1]
])

sorted_axis0 = np.sort(arr2, axis=0)  # 열 방향 정렬
print(sorted_axis0)
print()

sorted_axis1 = np.sort(arr2, axis=1)  # 행 방향 정렬
print(sorted_axis1)
print()


sorted_None = np.sort(arr2, axis=None)  # 평탄화 하고 정렬
print(sorted_None)
print()
# argsort
names = np.array(["김철수", "이영희", "박민수", "정수진", "최동욱"])
scores = np.array([85, 92, 78, 95, 88])

for name, score in zip(names, scores):
    print(f"{name} {score}")

# 점수 순으로 정렬
sorted_idx = np.argsort(scores)[::-1]

for i, idx in enumerate(sorted_idx, 1):
    print(f"{i}위 {names[idx]} {scores[idx]}")
