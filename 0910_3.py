# a = 10
# a += 5
# print(a)

# a -= 4
# print(a)

# a *= 3
# print(a)

# a /= 11
# print(a)

# a //= 2
# print(a)

# a **= 200
# print(a)

# a = 10
# a %= 3
# print(a)


# 30만원

# money = 300000
# money -= 80000
# money -= 9000 * 5
# money += 120000
# money += money * 0.2
# money -= money / 3
# print(money)


# name = input("이름을 입력하세요: ")
# print(name)

# score = int(input("점수를 입력하세요 : "))
# print(f"점수는 : {score + 10}")

# split() : 공백을 구분자로 나누겠다.
# fruit = "사과 참외 수박".split()
# print(fruit)

# fruit1, fruit2, fruit3 = input().split()
# print(fruit1, fruit2, fruit3, sep=',')

# intro = "둠칫"
# drop = "두둠칫"

# intro += drop * 3
# print(intro)

# name = "hotdog"
# age = 26
# your = input(f"안녕하세요. 저는 {name}이고, {age}살입니다.")


# 가로와 세로 입력받기

# width = int(input("가로 입력: "))
# height = int(input("세로 입력: "))

# # 넓이와 둘레 계산
# area = width * height
# perimeter = 2 * (width + height)

# # 출력
# print("넓이:", area)
# print("둘레:", perimeter)


# digits = input("네 자리 정수를 띄어쓰기로 입력하세요: ").split()
# # 예: 2 1 4 5 입력

# print("천의 자리:", digits[0])
# print("백의 자리:", digits[1])
# print("십의 자리:", digits[2])
# print("일의 자리:", digits[3])


# name1, name2, name3 = input("발표자 이름을 3명을 입력하세요: ").split()
# ppt1, ppt2, ppt3 = input("발표 주제 3개를 입력하세요: ").split()
# print("1조 발표자:", name1, "- 주제: ", ppt1)
# print("2조 발표자:", name2, "- 주제: ", ppt2)
# print("3조 발표자:", name3, "- 주제: ", ppt3)

year, month, day = input("년, 월, 일을 입력해주세요: ").split("-")

hour, minute, second = input("시, 분, 초를 입력해주세요: ").split(":")

print(f"RE3의 개강일은 {year}년 {month}월 {day}일")
print(f"시작 시간은 {hour}시 {minute}분 {second}초입니다.")
