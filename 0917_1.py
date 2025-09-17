# 실습

# 구구단 만들기
# num = 4
# print("4단")
# for i in range(1, 10):
#     print(f"{num} * {i} = {num * i}")


# # 구구단 전체
# for num in range(1, 10):
#     print(f"{num} 단")
#     for i in range(1, 10):
#         print(f"{num} * {i} = {num * i}")
#     print()

import random
for num in range(2, 6):
    print(f"{num} 단")
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")
for num in range(8, 10):
    print(f"{num} 단")
    for i in range(1, 10):
        print(f"{num} * {i} = {num * i}")


# 중첩 for문 사용
# 별 패턴 1: 직각삼각형

# *
# **
# ***
# ****
# *****
# ******
# *******

# for i in range(1, 6):
#     for j in range(i):
#         print('*', end='')
#     print()

n = int(input("정수를 입력하세요: "))
for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()

print()

for i in range(n):
    for j in range(n-i):
        print(" ", end="")
    for j in range(2*(i+1)-1):
        print("*", end="")
    print()

print()

for i in range(n):  # i는 0부터 n-1까지 반복 (줄 번호)
    # 왼쪽에 찍을 공백(" ") 출력
    # 첫 줄은 n-1개, 그 다음 줄은 n-2개 ... 마지막 줄은 0개
    for j in range(n-i):
        print(" ", end="")
    # 별(*) 출력
    # 첫 줄은 1개, 그 다음 줄은 2개 ... 마지막 줄은 n개
    for j in range(i+1):
        print("*", end="")
    print()

# 실습 리스트 컴프리헨션

num = [x ** 2 for x in range(1, 10 + 1)]
print(num)

num_list = [x for x in range(3, 50, 3)]
print(num_list)

fruits = ["apple", "fig", "banana", "plum", "cherry", "pear", "orange"]
five_len = [word for word in fruits if len(word) >= 5]
print(five_len)

# while 문 연습문제

secret_code = "codingonre3"
while True:
    code = input("비밀코드를 입력하세요: ")

    if code == secret_code:
        print("입장 완료 : 환영합니다.")
        break
    else:
        print("비밀번호가 틀렸습니다. 다시 시도하세요.")


attempt = 0
max_attempt = 5
remaining = max_attempt - attempt
while True:
    code = input("비밀코드를 입력해라: ")
    attempt += 1

    if code == secret_code:
        print("입장 완료 : 환영합니다.")
        break
    elif remaining > 0:
        print(f"틀렸습니다. {remaining}번 남았습니다.")
    else:
        print(f"로그인 실패! 계정이 잠겼습니다.")
