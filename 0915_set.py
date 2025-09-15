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

new_list = [1, 2, 5, 1, 5]
com_set5 = {i for i in new_list}
print(com_set5)

# set에 저장 가능한 데이터 타입
# hashable 타입만 가능 (불변 타입)
valid_set = {1, "문자열", (1, 2), 3.14, True, }

# unhashable 타입 불가능 (가변타입)
# invalid_set = {[1, 2], {"key": "value"}, {1, 2}}

# 중첩 set을 만들려면 frozenset() 사용
nested_set = {frozenset([1, 2]), frozenset([3, 4])}
print(nested_set)

# set 메서드
colors = {"빨강", "노랑", "파랑"}
colors.add("초록")
print(colors)

colors.update(["보라", "주황"])
print(colors)

# colors.remove("검정")
# print(colors)

colors.discard("주황")
print(colors)

popped = colors.pop()
print(popped)
print(colors)

colors.clear()
print(colors)

# 교집합 연산
A = {1, 2, 3, 4, 5}
B = {1, 2, 6, 7, 8, }

intersection1 = A & B
intersection2 = A.intersection(B)

print(intersection1)
print(intersection2)

# 합집합 - 모든 요소
union1 = A | B
union2 = A.union(B)
print(union1)
print(union2)

# 차집합 (Difference) - 기준 집합에만 있는 요소
difference1 = A - B
difference2 = A.difference(B)

print(difference1)
print(difference2)

# 대칭 차집합(Symmertric Difference) - 공통 요소 제외
sym_diff1 = A ^ B
sym_diff2 = A.symmetric_difference(B)
print(sym_diff1)
print(sym_diff2)

A = {1, 2, 3}
B = {3, 4, 5}

A.intersection_update(B)  # 교집합으로 업데이트
A &= B
print(A)

A = {1, 2, 3}
A.difference_update(B)  # 차집합으로 업데이트
A -= B
print(A)

A = {1, 2, 3}
A.symmetric_difference_update(B)  # 대칭차집합으로 업데이트
A ^= B
print(A)

A = {1, 2, 3}
A.update(B)  # 합집합으로 업데이트
A |= B
print(A)

# 집합 관계 확인
# 부분 집합, 상위 집합

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}

# 부분 집합인지 확인
print(A.issubset(B))  # True
print(B.issubset(A))  # False
print(A <= B)

print(B.issubset(A))

# 상위 집합인지 확인
print(A.issuperset(B))
print(B.issuperset(A))
print(A >= B)

# 진부분집합 확인
print(B > A)
print(B < A)


# 서로수 집합
print(A.isdisjoint(C))

# frozenset() (불변집합)
fs1 = frozenset([1, 2, 3, 3, 4])
# 불변이므로 수정이 불가
# fs1.add(5)
# fs1.remove()
# fs1.discard()


submissions = ["kim", "lee", "kim", "park", "choi", "lee", "lee"]
submissions1 = set(submissions)
print(f"제출자 명단", submissions1)
a = len(submissions1)
print(f"제출한 학생 수: ", int(a))

user1 = {"SF", "Action", "Drama"}
user2 = {"Drama", "Romance", "Action"}

print(user1.intersection(user2))
print(user1.symmetric_difference(user2))
print(user1.union(user2))

my_certificates = {"SQL", "Python", "Linux"}
job_required = {"SQL", "Python"}

print(job_required.issubset(my_certificates))
