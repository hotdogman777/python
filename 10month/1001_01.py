import random
import numpy as np
arr = np.array([5, 12, 18, 7, 30, 25])
print(arr)
print(arr[(10 < arr) & (arr < 20)])

arr = np.array([10, 15, 20, 25, 30, 35])
print(arr)
print(arr[(15 >= arr) | (arr >= 30)])

arr = np.array([5, 12, 18, 7, 30, 25])
arr[arr >= 10] = 0
print(arr)

arr = np.array([7, 14, 21, 28, 35])
for i in arr:
    if i >= 20:
        print("High")
    else:
        print("Low")

result = np.where(arr >= 20, "High", "Low")

# == == == == == == == == == == == == == == == == == 실습 1번

arr = np.arange(10)
result = np.where(arr % 2 == 0, arr, arr * 10)
print(result)
print()
arr = np.array([
    [10, 25, 30],
    [40, 5, 15],
    [20, 35, 50]
])

result = arr[(arr >= 20) & (arr <= 40)]
print(result)
print(arr[arr >= 20] & [arr <= 40])
print(arr[arr <= 40])

print()
arr = np.array([1, 2, 3, 4, 5, 6])
print(arr[~(arr % 3 == 0)])
# == == == == == == == == == == == == == == == == == == == == == 실습 2번


arr = np.random.randint(0, 101, 10)
result = np.where(arr >= 50, arr, 50)
print(result)

arr9 = np.array([
    [5, 50, 95],
    [20, 75, 10],
    [60, 30, 85]
])

result = np.where(arr9 >= 70, "A",
                  np.where(arr9 >= 30, "B", "C"))
print(result)
