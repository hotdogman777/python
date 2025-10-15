import numpy as np
# numpy(numberiacl Python) 파이썬에서 과학계산을 위한 핵심 라이브러리
# 데이터과학, 머신러닝, 과학 연구 분야에서 가장 중요한 도구 중 하나이다.

# 파이썬은 인터프리터 언어로 실행속도가 느립니다.
# 속도 문제 해결
# numpy는 c언어로 구현되어 있어 대용량 데이터 연산을 매우 빠르게 처리

# 메모리 효율성
# 파이썬 리스트: 각 요소가 객체로 저장되어 메모리 오버헤드가 큼
# numpy 배열: 연속된 메모리 공간에 같은 타입의 데이터를 저장

# 백터와 연산
# 반복문 없이 전체 배열에 대한 연산을 한번에 수행

print("Numpy 버전: ", np.__version__)
print("Numpy 설치 경로: ", np.__file__)

# ndarray(N-dimensional array) Numpy의 핵심 자료 구조
# 같은 타입의 요소들을 담는 다차원 컨테이너

arr = np.array([1, 2, 3, 4, 5])


print("1. 객체타입:", type(arr))
print("2. 데이터타입:", arr.dtype)
print("3. 배열모양:", arr.shape)
print("4. 차원 수:", arr.ndim)
print("5. 전체 요소 수:", arr.size)

python_list = [1, 2.5, "3.", True]
numpy_array = np.array([1, 2.5, "3.", True])
print(python_list)
print(numpy_array)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print("리스트 더하기: ", list1 + list2)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Numpy 배열 더하기: ", arr1 + arr2)


int_array = np.array([1, 2, 3, 4, 5])
print("정수 배열: ", int_array)
print("데이터 타입: ", int_array.dtype)

float_array = np.array([1.1, 2.2, 3.3, 4.4, 5.5])
print("실수 배열: ", float_array)
print("데이터 타입: ", float_array.dtype)

specified_array = np.array([1.1, 2.2, 3.3, 4.4, 5], dtype=np.float32)
print("명시적 배열: ", specified_array)
print("데이터 타입: ", specified_array.dtype)

string_array = np.array(["apple", "banana", "cherry"])
print("명시적 배열: ", string_array)
print("데이터 타입: ", string_array.dtype)

# 2차원 배열
matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])
print("2차원 배열: ", matrix)
print("모양: ", matrix.shape)
print("차원: ", matrix.ndim)
print("크기: ", matrix.size)

# for i in range(3):
#     for j in range(3):
#         print()

rows = []
for i in range(3):
    row = [i * 3 + j for j in range(4)]
    rows.append(row)

martix2 = np.array(rows)
print()
print("동적 생성 행렬: ", martix2)

# 3차원 배열 (2 x 3 x 4)
# 2개의 3 x 4 행렬로 구성
tensor = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ],
])

print()
print("3차원 배열 모양: ", tensor.shape)
print("차원: ", tensor.ndim)

# numpy 내장 함수로 배열 생성
# 0부터 9까지
arr1 = np.arange(10)
print("0부터 9까지", arr1)

arr2 = np.arange(1, 11)
print("1부터 10까지", arr2)

arr3 = np.arange(1, 21, 2)
print("1부터 20까지 홀수만", arr3)

arr4 = np.arange(1, 11, 0.5)
print("1부터 10까지", arr4)

# 균등 간격 배열 linspace
# 시작, 끝 사이를 균등하게 나눈 숫자들
arr1 = np.linspace(0, 10, 5)
print("시작과 끝 사이를 균등하게 나눈 숫자들\n", arr1)

arr2 = np.linspace(0, 10, 5, endpoint=False)
print("끝 값을 제외\n", arr2)

# 로그 간격 배열 logspace
# logspace(start, end, num)

# zeros: 0으로 채운 배열
zeros_1d = np.zeros(5)
print("1차원 zeros: ", zeros_1d)

zeros_2d = np.zeros((3, 4))
print("2차원 zeros: ", zeros_2d)

ones_1d = np.ones(5)
print("1차원 ones: ", ones_1d)

# full 특정 값으로 채운 배열
full_array = np.full((3, 4), 7)
print("2차원 배열: ", full_array)

matrix = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [4, 5, 6]
])

full_like = np.full_like(matrix, 999)
print("2차원 배열: ", full_like)

empty_array = np.empty((2, 3))
print("2차원 배열(주의: 쓰레기값)", empty_array)

# 3x3 항등 행렬
identity = np.eye(3)
print("3x3 항등 행렬: \n", identity)


# 4x5 행렬에서 대각선이 1
matrix = np.eye(4, 5)
print("4x5 대각 1:\n", matrix)


# 대각선 위치 조정
matrix = np.eye(4, k=1)
print("위쪽 대각선:\n", matrix)

# 0과 1사이에 균일 분포
random_uniform = np.random.rand(3, 3)
print("0부터 1균일 분포: \n", random_uniform)
rounded = np.round(random_uniform, 2)
print(rounded)

# 특정 범위의 균일 분포
low, high = 10, 20
random_range = low + (high - low) * np.random.rand(3, 3)
print(f"{low} 부터 {high} 균일 분포\n", random_range)

uniform = np.random.uniform(low=0, high=100, size=(2, 3))
print(f"0부터 100 균일 분포\n", uniform)

# 정규 분포 난수
# 표준 정규 분포 (평균 0 표준편차 1)
random_normal1 = np.random.randn(3, 3)
print("표준 정규 분포\n", random_normal1)

# 평균 100, 표준편차 15인 평균 분포
mean, std = 100, 15
scores = mean + std * np.random.randn(3)
scores = mean + std * np.random.randn(1000)
print("표준 정규 분포\n", scores[:10])
print("표준 정규 분포\n", scores.mean())
print("표준 정규 분포\n", scores.std())

# 정수 난수
# 0 - 9 사이에 정수 난수
random_int = np.random.randint(0, 10, size=(3, 4))
print("0~9 정수 난수\n", random_int)

# 주사위 시뮬레이션(1~6)
dice = np.random.randint(1, 7, size=10)
print("주사위 10번 굴리기\n", dice)

# 시드 설정(재현 가능한 난수)
np.random.seed(42)
random1 = np.random.rand(5)
print("첫 번째 난수: ", random1)

np.random.seed(42)
random2 = np.random.rand(5)
print("첫 번째 난수: ", random2)
print("같은가?", np.array_equal(random1, random2))

rng = np.random.default_rng(seed=42)
random3 = rng.random((2, 3))
print("새로운 방식 난수: \n", random3)
