import random

# 1~45까지의 수 중에서 랜덤으로 6개의 숫자를 뽑는다.
# sample 사용
# 6개의 숫자 중 중복되는 숫자가 없도록 한다.

# 오름차순으로 정렬한 결과를 출력한다.
numbers = range(1, 46)
lotto = random.sample(numbers, 6)
lotto.sort()
num_list = lotto
print(num_list)

user_choice = input("가위, 바위, 보 중에 하나만 입력하세요: ")
print(f"당신의 선택은 {user_choice} 입니다.")

choices = ["가위", "바위", "보"]
cpu_choice = random.choice(choices)
print(f"컴퓨터의 선택은 {cpu_choice}")

if user_choice == cpu_choice:
    print("비겼습니다")
elif (user_choice == "가위" and cpu_choice == "보") or (user_choice == "바위" and cpu_choice == "가위") or (user_choice == "보" and cpu_choice == "바위"):
    print("당신이 이겼습니다.")
else:
    print("당신이 졌습니다 coputer: 내가 이겼다! 내가 이겼다!")
