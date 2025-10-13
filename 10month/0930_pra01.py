import numpy as np

arr1 = np.array([1, 2, 3, 4])
print(arr1 * 3)

arr2 = np.array([[
    [5, 10],
    [15, 20]
]])

new_arr = arr2 * -1
print(new_arr)

arr3_a = np.array([2, 4, 6])
arr3_b = np.array([1, 2, 3])

mul_result = arr3_a * arr3_b

div_result = arr3_a / arr3_b
print("요소별 곱셈 결과: ", mul_result)
print("요소별 나눗셈 결과: ", div_result)

arr4 = np.array([[95, 97], [80, 85]])

max_val = arr4.max()
diff = 100 - max_val
new_arr = arr4 + diff

print("원래 배열:\n", arr4)
print("현재 최대값:\n", arr4)
print("더해야 할 것:\n", arr4)
print("새로운 배열:\n", arr4)

arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

factors = np.array([
    [10],
    [100]
])

new_arr = arr5 * factors

print("원래 배열: \n", arr5)
print("곱할 값(factors): \n", arr5)
print("새로운 배열: \n", arr5)

arr6 = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

add_values = np.array([
    [100],
    [200],
    [300]
])

new_arr = arr6 + add_values

print("원래 배열:\n", arr6)
print("더할 값:\n", arr6)
print("새로운 배열:\n", arr6)
