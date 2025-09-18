# 실습
def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b != 0:
            return float(a) / b
        else:
            return "0으로 나눌 수 없습니다."

    else:
        return "지원하지 않는 연산입니다."


print(calculate(10, 5, "+"))   # 15
print(calculate(10, 5, "-"))   # 5
print(calculate(10, 5, "*"))   # 50
print(calculate(10, 5, "/"))   # 2.0
print(calculate(10, 0, "/"))   # 0으로 나눌 수 없습니다
print(calculate(10, 5, "%"))   # 지원하지 않는 연산입니다


def greet(name, message="안녕"):
    print(f"{name} {message}")


greet("hotdog")
greet("김철수", "안녕하세요")


def add(a=4, b=3, c=2, d=1):
    pass


add(1, 2, 11)


def add_all(*new_tuple):
    return sum(new_tuple)


result = add_all(1, 2, 3, 4, 5)
print(result)


def print_info(**new_dic):
    for key, value in new_dic.items():
        print(f"{key} {value}")


print_info(name="홍길동", age=25, city="서울")


def average(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(average(1, 2, 3, 4, 5))


def long_lenth(*args):
    if max(args) == 0:
        return None
    return max(args, key=len)


print(long_lenth("aaaaaaaaaaaaa", "bbbbbbbbbbbbb", "ccccccccccccccc"))


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# use1 = input("이름을 입력하세요: ")
# use2 = input("나이를 입력하세요: ")
# use3 = input("이메일을 입력하세요: ")
# print_info(name=use1, age=use2, email=use3)

print_info(name="거북도사", age="99", city="무릉도원")


def cal(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} {value}")
