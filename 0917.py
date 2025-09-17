# break
for i in range(3):
    if i == 2:
        break
    print(i)


for i in range(10):
    break
    print(i)
print(i)

for i in range(10):
    print(i)
    break
print("for문 종료")

print()

for i in range(10):
    if i % 2:  # 짝수가 나오면 프린트 하고
        continue  # 홀수를 값이 내려오면 다시 무시하고 실행
    print(i)

for i in range(10):
    print(i)
    pass

print()

for i in range(10):
    print(i)
    if i == 3:
        continue
else:
    print("루프 정상 종료")

colors = ["red", "blue"]
fruits = ["apple", "banana"]

for color in colors:
    for fruits in fruits:
        print(f"{color}, {fruits}")

new_list = [(c, f) for c in colors for f in fruits]
print(new_list)

# while문

i = 1

while i <= 5:
    print("반복문 실행")
    i += 1
print("반복문 종료")

# for문 vs while문
# for문 : 몇 번 반복할지 정해져 있을때
# while문 : 조건이 만족하는 동안 계속 반복

# while 조건식
#   반복할 코드
#   (조건을 변경하는 코드)

# 카운트 다운
count = 5

while count > 0:
    print(f"count {count}")
    count -= 1

print("while문 종료")

# 누적 합계 구하기
total = 0
num = 1

while num <= 100:
    total += num
    num += 1

print(f"1부터 100까지의 합 {total}")

# while문으로 입력 검증하기
# 올바른 입력을 받을 때까지 반복
age = -1  # 초기값

while age < 0 or age > 150:
    age = int(input("나이를 입력하세요(0 - 150): "))

    if age < 0 or age > 150:
        print("올바른 나이를 입력해주세요!")

print(f"입력된 나이: {age}세")

# 비밀번호 확인
correct_password = "python123"
attempt = 0
max_attempt = 3

while attempt < max_attempt:
    password = input("비밀번호를 입력하세요: ")
    attempt += 1

    if password == correct_password:
        print("로그인 성공")
        break
    else:
        remaining = max_attempt - attempt
        if remaining > 0:
            print(f"틀렸습니다. {remaining}번 남았습니다.")
        else:
            print(f"로그인 실패! 계정이 잠겼습니다")

# 무한 루프와 break
while True:
    user_input = input("명령을 입력하세요(종료: q")

    if user_input == "q":
        print("프로그램을 종료합니다.")
        break

    print(f"입력한 명령: {user_input}")
    # 명령 처리
    pass

# 계산기
while True:
    num1 = float(input("첫 번째 숫자: "))

    if num1 == 0:
        break

    num2 = float(input("두 번째 숫자: "))
    operator = input("연산자 (+, -, *, /)")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("0으로 나눌수 없습니다.")
            continue
    else:
        print("잘못된 연산자 입니다")
        continue
    print(f"결과 : {result}")

# while else
i = 10

while i < 15:
    print(i)
    i += 1
else:
    print("정상 종료 되었습니다.")
print()
