# set
# 중복되지 않는 요소들의 순서가 없는 집합
# 수학의 집합 개념을 구현한 자료 구조
# 해시 테이블 기반으로 빠른 멤버쉽 테스트 가능

# 왜 Set이 필요한가?
# 중복 제거가 필요한 경우
visitors = ["철수", "영희", "철수", "민수", "영희", "철수"]

# 리스트로 중복 제거(비효율적) o(n) 검색
unique_visitors_list = []
for visitor in visitors:
    if visitor not in unique_visitors_list:
        unique_visitors_list.append(visitors)
print(unique_visitors_list)

# Set으로 중복 제거 (효율적) o(1) 검색
unique_visitors_list = set(visitors)
print(unique_visitors_list)

# 특징
# 1. 순서 없음 : 요소들의 순서가 보장 되지 않음
# 2. 중복 불가 : 같은 값은 하나만 저장
# 3. 변경 가능 : 요소 추가 /삭제 가능
# 4. 인덱싱 불가 : 순서가 없어 인덱스로 접근 불가능
# 5. 빠른 검색 : o(1)시간 복잡도로 요소 확인

# Set 생성 방법
# 1. 빈 set 생성
# empty_set = [] # 이것은 딕셔너리!!!!
empty_set = set()

# 2. 값이 있는 set 생성
numbers = {1, 2, 3, 4, 5, 4, 3, 2, 1}
fruits = {"사과", "바나나", "오렌지"}

# 3. 리스트/튜플에서 set 생성
list_numbers = [1, 2, 3, 4, 5, 4, 3, 2, 1, 4]
set_numbers = set(list_numbers)
print(set_numbers)

# 4. 문자열에서 set 생성
chars = set("hello")
print(chars)

# Comprehension
for i in range(10):
    print(i)
com_set = {i for i in range(10)}
print(com_set)

com_set1 = {i * 2 for i in range(10)}
print(com_set1)

com_set2 = {(i ** 2 + 1)for i in range(10)}
print(com_set2)

com_set3 = {(i * 3 + 2 - 1)for i in range(10)}
print(com_set3)

com_set4 = set()
for i in range(10):
    com_set4.add((i * 3 + 2 - 1))
print(com_set4)

com_list = [i for i in range(2, 10, 2)]  # for 문을 한줄로 쓰는 방법
print(com_list)
