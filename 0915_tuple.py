# # 튜플
# # 순서가 있는 불변 자료 시퀀스이다.
# # 한번 생성되면 수정할 수 없는 리스트와 유사한 구조
# # 여러 개의 값을 하나의 단위로 묶을 때 사용

# # 왜 Tuple을 사용하는가???
# # 변경되면 안되는 데이터 보호
# # 리스트 사용 시 -> 실수로 변경 가능...
# coordinates_list = [37.345, 126.432]  # 특정 좌표
# coordinates_list[0] = 0  # TypeError! 발생 변경 불가능


# # 특징
# # 불변성 생성 후 수정 불가능
# # 순서 보장 : 인덱스로 접근 가능
# # 종복 허용 : 같은 값 여러 번 가능
# # 해시 가능 : 딕셔너리 키로 사용 가능
# # 메모리 효율성 : 리스트보다 적은 메모리 사용


# # 1. 소괄호 사용
# empty_tuple = ()
# numbers = (1, 2, 3, 4, 5)
# mixed = (1, "hello", 3.14, True)
# print("mixed: ", mixed)

# # 2. 소괄호 없이
# numbers2 = 1, 2, 3, 4, 5
# print("type(numbers2): ", type(numbers2))

# # 3. tuple() 생성자 사용
# from_list = tuple([1, 2, 3, 4])
# print("type(from_list): ", type(from_list))
# # 4. 단일 요소 튜플(, 필수 !!!)
# from_str = tuple("hello")
# print("type(from_str): ", type(from_str))
# not_tuple = (10)
# print("type(not_tuple): ", type(not_tuple))

# # 5. range로 튜플 생성
# range_tuple = tuple(range(1, 10))
# print("type(range_tuple): ", type(range_tuple))

# print("range_tuple: ", range_tuple)

# # tuple_range = range(tuple(1, 10))
# # print(tuple_range)

# # 튜플 접근과 슬라이싱
# fruits = ("사과", "바나나", "수박", "오렌지")
# print(fruits[1])
# print(fruits[-1])

# print(fruits[1:3])
# print(fruits[:2])
# print(fruits[::-1])

# # 슬라이싱으로 새튜플 생성
# first_three = fruits[0:3]
# last_two = fruits[2:]
# print("last_two", last_two)

# # 처음 3개랑, 마지막 두개
# combined = first_three + last_two
# print(combined)

# # 불변성 확인
# numbers = (1, 2, 3, 4, 5, 6)

# # 수정 시도 - 모두 에러 발생
# # numbers[0] = 10 # TypeError
# # numbers.append(6)
# # del numbers[1] 튜플은 삭제가 가능하지만 단일 삭제는 안된다.

# # 하지만 새 튜플 생서은 가능
# new_numbers = numbers = (1, 2)

# tuple_with_list = ([1, 2], [3, 4])
# tuple_with_list[0].append(3)
# print(tuple_with_list)
# # tuple_with_list[0] - [2, 3]

# # 언패킹(unpacking)
# coordinates = (3, 5)
# x, y = coordinates
# print(f"x : {x}, y: {y}")

# # 직접 언패킹
# x, y = (10, 20)
# print(f"x : {x}, y : {y}")
# x = 20
# print(f"x : {x}, y : {y}")

# x, *y, = (10, 20, 30)
# print(f"x : {x}, y : {y}")

# first, *middle, last = numbers
# print("first", first)
# print("middle", middle)
# print("last", last)

# # 빈 리스트 생성
# first, *rest = (1,)
# print("first", first)
# print("rest", rest)

# # 튜플 메서드 특정 값의 개수
# numbers = (1, 1, 3, 3, 2, 2, 5, 4, 3)
# count_2 = numbers.count(2)
# print("count_2", count_2)

# # index() - 특정 값에 인덱스
# # 없는 값 검색 시 에러...
# index_4 = numbers.index(4)

# # 안전한 검색
# value = 10
# if value in numbers:
#     print(f"{value}의 인덱스: {numbers.index(value)}")
# else:
#     print(f"{value}는 튜플에 없습니다.")

# # 연산
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# print(tuple + tuple2)

# # 곱셈
# print("tuple * 3", tuple * 3)

# # 비교 연산 (사전식 비교)
# print(tuple1 < tuple2)
# print(tuple1 == tuple2)

# # 길이
# numbers = (1, 2, 3, 4)
# print(len(numbers))
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))

# 실습1
user = ("minji", 25, "Seoul")
users = ("minji", "eunji", "soojin", "minji", "minji")
user1 = ("eunji", 25, "Seoul")
restored_user = user1
name, age, city = (restored_user)
print(f"{name}, {age}, {city}")
if city == "Seoul":
    print("서울 지역 보안 정책 적용 대상입니다.")
else:
    print("일반 지역 보안 정책 적용 대상입니다.")

count = users.count("minji")
print("minji 이름 중복: ", count)

found_soojin = users.index("soojin")
print("soojin 위치 인덱스: ", found_soojin)
sorted_users = sorted(users)
print(f"가나다 순: ", sorted_users)

# 튜플을 변경하려면 새로운 튜플을 생성하는 방법 말고는 없다.
