print(chr(90))

new_list = [1, 2, 3]

try:
    print(new_list.index(4))
except:
    print("에러가 발생했습니다.")


def add(a, b):
    a += 1
    return a + b


# print(a)


count = 10


def count_print():
    global count  # 함수 내부에서 count 는 전역 변수임을 명시 해준다.
    count = count + 1
    print(count)
    return count


count_print()
print(count)


def count_print(count):
    count += 1
    print("def count: ", count)
    return count


count_print(count)
print(count)


def outer():
    a = 10

    def inner():
        nonlocal a
        a += 5
        print(f"[inner] a: {a}")
    inner()
    print(f"[outer] a: {a}")


outer()

# 함수의 범위
'''
변수의 범위란?
변수가 살아 있는 (접근 가능한) 영역을 범위(Scope)라고 합니다
집 = 전역범위
방 = 지역범위
방 안의 물건은 그 방에서만 사용 가능
거실의 물건은 모든 방에서 사용 가능
'''

# 전역 변수(Global variable)
global_var = "전역 변수"


def my_fun():
    # 지역 변수(local variable)
    local_var = "지역 변수"

    print(global_var)
    print(local_var)


my_fun()
print(global_var)  # 전역 변수 접근 가능
# print(local_var) # 에러! 함수 밖에서 지역 변수 접근 불가

# Global 키워드
# 함수 안에서 전역 변수를 수정할려면 global 키워드를 사용합니다.

count = 0  # 전역 변수


def increment_wrong():
    count = count + 1  # 에러! 지역 변수로 취급됨


def increment_right():
    global count
    count = count + 1


# increment_wrong()

print("초기값:", count)  # 0
increment_right()
increment_right()
print("최종갑:", count)

score = 0

# def add_score(points):


# 전역 변수 사용 주의
# 전역 변수는 편리하지만 과도하게 사용하면 코드가 복잡해집니다.


# 불변 타입
# 함수, 실수, 문자열, 튜플

# 가변 타입
# 리스트, 딕셔너리, set


current_user = None


def login(name):
    global current_user
    if current_user is None:
        current_user = name
        print(f"{name}님 로그인 성공")
    else:
        print("이미 로그인되어 있습니다")


def logout():
    global current_user
    if current_user is not None:
        print("로그아웃되었습니다")
        current_user = None
    else:
        print("로그인된 사용자가 없습니다.")


# 재귀 함수 (Recursive Function)
'''
재귀 함수는 자기 자신을 호출하는 함수
'''

# 팩토리얼 계산 (n! = n x (n-1) x (n-2) x (n-3) ....1)


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


result = factorial(5)
print(result)

# 피보나치 수열 - 앞에 더한 값이 뒤에 나온다
# 0 1


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


fibonacci(2)

fibonacci(4)
fibonacci(2) + fibonacci(3)
fibonacci(0) + fibonacci(1) + fibonacci(3)

4
3 2
2 1


for i in range(10):
    print(fibonacci(i))
print()
