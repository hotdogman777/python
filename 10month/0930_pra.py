import numpy as np

arr1 = np.arange(25).reshape(5, 5)
print(arr1)
print("문제1.\n 가운데 행:", arr1[2, :])
print("가운데 열", arr1[:, 2])
print()

arr2 = np.arange(100).reshape(10, 10)
print(arr2[::2])
print()

arr3 = np.arange(50).reshape(5, 10)
print(arr3[1:4, 2:7])
print()
print("실습 Numpy 종합 연습===================================================Numpy 종합 연습")
print()
print("Numpy 종합 연습2")

arr4 = np.random.randint(0, 10, (4, 4))
print("배열:\n", arr4)
print()

main_diag = []
for i in range(4):
    main_diag.append(arr4[i, i])
print()

sub_diag = []
for i in range(4):
    sub_diag.append(arr4[i, 3 - i])
print()

print("주대각선: ", main_diag)
print("부대각선: ", sub_diag)
print()

arr5 = np.random.randint(0, 10, (3, 4, 5))
print(arr5)
value = arr5[1, 0, -1]
print("두 번째 층의 첫 행 마지막 열 값:", value)
print("실습 Numpy 종합 연습===================================================Numpy 종합 연습")
print()

print("Numpy 종합 연습3")
arr6 = np.arange(35, 75).reshape(10, 4)
print("문제 6:\n", arr6)
print()

print("문제 7:\n", arr6[::-1])
print()

print("문제 8:\n", arr6[1:-1, 2:])
print()

print("실습 Numpy 종합 연습===================================================Numpy 종합 연습")

print("Numpy 종합 연습4")
arr9 = np.random.randint(1, 51, (5, 6))
print("문제 9 배열:\n", arr9)

evens = arr9[arr9 % 2 == 0]
print("문제 9 짝수만:", evens)
print()

arr10 = np.arange(100).reshape(10, 10)
print("문제 10 배열:\n", arr10)

selected = arr10[[1, 3, 5], :][:, [2, 4, 6]]
print("문제 10 선택된 원소들:\n", selected)
print()

arr11 = np.random.randint(0, 10, 15)
print("문제 11 배열:", arr11)

even_index_vals = arr11[::2]
print("짝수 인덱스 값들:", even_index_vals)

over5 = even_index_vals[even_index_vals >= 5]
print("짝수 인덱스 중 5 이상:", over5)
