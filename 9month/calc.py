def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if a or b == 0:
        print("0으로는 나눌 수 없습니다.")
    else:
        return a / b
