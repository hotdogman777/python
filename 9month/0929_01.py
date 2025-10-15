import numpy as np

array1 = np.full((3, 4), 5)
print("문제1: \n", array1)

# arr0 = np.zeros((3, 4)) + 5
# print("문제1: \n", array1)

arr1 = np.arange(0, 21, 2)
print("문제2: \n", arr1)

print("문제3: \n", np.random.rand(2, 3))

mean, std = 100, 20
scores = mean + std * np.random.randn(6)
print("문제4: \n", scores)

# reshape 재배치
arr5 = np.arange(1, 21).reshape(4, 5)
print(arr5)

arr6 = np.linspace(0, 1, 12).reshape(3, 4)
print(arr6)

arr7 = np.random.randint(0, 100, (10, 10))
arr7 = arr7 + np.eye(10)
print(arr7)

arr8 = np.random.randint(0, 10, (2, 3, 4))
print(arr8)
