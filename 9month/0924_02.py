# 예외
'''
    예외는 프로그램 실행 중에 발생하는 예상치 못한 상황
    예외가 발생하면 프로그램이 즉시 엄추지만, 예외 처리를 하면 프로그램을 계속 실행할수 있습니다.
'''

# 오류 vs 예외의 차이
# 구문 오류(Syntax Error): 코드를 잘못 작성한 경우
# 프로그램이 시작조차 못함
# 코드를 수정해야만 해결

'''
    ____print("hello"
'''

'''
    예외: 문법은 맞지만 실행 중 발생하는 문제
    프로그램 실행 중 발생
    try-except로 처리 가능
'''
# result = 10 / 0

# 예외 처리가 필요한 이유
# age = int(input("나이를 입력해주세요: "))


# while True:
#     try:
#         age = int(input("나이를 입력해주세요: "))
#         break
#     except:
#         print("숫자로 입력해주세요")

# # try 블록은 최소한으로
# name = input("이름")
# try:
#     age = int(input("나이"))
# except:
#     print("오류!")

# print(f"안녕하세요 {name}님")


def get_age_group():
    """나이를 입력받아 연령대 반환"""
    while True:
        try:
            age = int(input("나이를 입력해라: "))
            if 0 <= age < 150:
                print(f"나는 {age}살")
            else:
                print("오류 메세지")

        except ValueError:
            print("다시 입력해주세요")
        else:
            if age < 20:
                print('미성년자')
            elif 20 <= age < 40:
                print("청년")
            elif 40 <= age < 60:
                print("중년")
            elif 60 < age:
                print("노년")

            break


get_age_group()
