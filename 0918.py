def greet(name):
    # 출력하는 함수
    print(f"hello, {name}!")


greet("hotdog")

# 함수(function)

# 함수는 특정 작업을 수행하는 묶음입니다.
# 한번 정의하면 필요할 때마다 호출하여 재사용이 용이

# 함수를 사용하는 이유
'''
코드 재사용성: 같은 코드를 반복 작성할 필요 없음
모듈화 : 프로그램을 작은 단위로 나누어 관리
가독성 향상 : 코드의 의도를 명확히 표현
유지보수 용이 : 수정이 필요할 때 함수만 변경
추상화 : 복잡한 로직을 단순한 인터페이스로 제공
'''

print("=" * 20)
print("첫 번째 섹션")
print("=" * 20)

print("=" * 20)
print("두 번째 섹션")
print("=" * 20)

# 함수 사용 - 코드 재사용


def print_section(title):
    print("=" * 20)
    print(f"{title} 섹션")
    print("=" * 20)


print_section("첫번째")
print_section("두번째")

# 함수 정의와 호출
# 함수 정의(Defintion)


# def 함수이름(매개변수):
#     # 실행할 코드
#     return 반환값


# # 함수 호출 (call)
# 결과 = 함수이름(인자)


def say_hello():
    print("안녕하세요!")


say_hello()


def greet(name):
    print(f"안녕하세요 {name}님!")


greet("안철수")
greet("배철수")


def add(a, b):
    result = a + b
    return result


sum_result = add(3, 5)
print("sum_result", sum_result)
print("add(10, 5)", add(10, 5))

# 사각형 넓이


def calculate_area(width, height):
    '''
    직사각형 넓이를 계산합니다

    parameters:
        width (float): 직사각형의 너비
        height (float): 직사각형의 높이

    Return:
        float: 직사각형의 넓이
    '''
    return width * height


# Docstring 확인
print(calculate_area.__doc__)
print(calculate_area(10, 20))
help(calculate_area)


# 매개변수와 인자
'''
매개변수(parameter): 함수 정의 시 사용하는 변수
인자(Argument): 함수 호출시 전달하는 실제 값
'''


def multiply(x, y):
    return x * y


result = multiply(3, 5)

# 위치 인자


def introduce(name, age, city):
    print(f"{name} {age} {city}")


introduce("김철수", 25, "서울")


# 키워드 인자
def introduce(name, age, city):
    print(f"{name} {age} {city}")


introduce(city="서울", age=25, name="김철수")

# 위치 인자, 키워드 혼용

introduce("김철수", city="서울", age=15)
#  주의: 위치 인자는 키워드 인자보다 앞에 와야 한다

# introduce(25, city="부산", name="이영희")

# 반환값(return)
# 단일 값 반환


def square(n):
    return n ** 2


result = square(5)
print(result)

# 여러 값 반환


def calculate_stats(numbers):
    total = sum(numbers)
    avg = total / len(numbers)
    maxnum = max(numbers)
    minnum = min(numbers)

    return total, avg, maxnum, minnum


numbers = [100, 140, 230, 200]
a, b, c, d = calculate_stats(numbers)

print(a)
print(b)
print(c)
print(d)

stats = calculate_stats(numbers)
print(stats)

# return의 특징


def check_positive(number):
    if number > 0:
        return "양수"
    elif number < 0:
        return "음수"
    else:
        return "0"
    print("코드가 실행이 될까요?")


check_positive(4)
check_positive(-1)
check_positive(0)

# 조기 반환


def divide(a, b):
    if b == 0:
        return

    return a / b


print(divide(10, 2))
print(divide(10, 0))

# 기본값 매개변수


def greet(name, greeting="안녕하세요"):
    print(f"{greeting}, {name}님")


greet("김철수")
greet("이영희", "반갑습니다.")

# 여러 기본값


def create_profile(name, age=25, city="서울", job="개발자"):
    return {"name": name,
            "age": 25,
            "city": city,
            "job": job
            }


print(create_profile("박민수"))
print(create_profile("김철수", 30))
print(create_profile("이영희", job="모델"))

# 가변 위치 인자(*args)


def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_all(1, 2, 3))

# 가변 키워드 인자(**kwargs)


def print_info(**user):
    # 키워드 인자를 딕셔너리로 받습니다.
    print(f"user", user)
    for key, value in user.items():
        print(f"{key}: {value}")


print_info(name="김철수", age=20, city="서울")


def create_student(**info):
    '''
    학생 정보를 입력하세요
    '''
    student = {
        "name": info.get("name", "이름 없음"),
        "age": info.get("age", 20),
        "grade": info.get("grade", 1),
        "subjects": info.get("subjects", []),
    }
    return student


student1 = create_student(name="김철수", subjects=["python"])
print(student1)
