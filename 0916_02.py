# 반복문

# 실습 1.
numbers = [3, 6, 1, 8, 4]
for i in numbers:
    print(i * 2, end=" ")

words = ["apple", "banana", "kiwi", "grape"]
print(f"\n리스트의 길이: {len(words)}")

x_valuse, y_values = [], []
coordinates = [(1, 2), (3, 4), (5, 6), (7, 8)]  # 저장하고
for x, y in coordinates:  # 언패킹하고
    x_valuse.append(x)
    y_values.append(y)
print(f"x_values: {x_valuse}, y_values: {y_values}")

# 실습2. for문과 range
# ★문제1. 입력 받은 수의 합 구하기
# ■ for 문과 range()를 사용하여 1부터 사용자가 입력한 수까지의 합을 구해보세요.
total_num = []
input_name = int(input("점수를 입력해주세요: "))
for i in range(1, input_name+1):
    print(i)
    total_num.append(i)
    sum_total = sum(total_num)
    print("\nsum_total : ", sum_total)
    # ★ 문제2. 구구단 만들기(1)
    # ■ 사용자로부터 정수 하나를 입력 받아, 해당 숫자의 구구단을 아래와 같이 출력하는 프로그램을 작성하세요.
