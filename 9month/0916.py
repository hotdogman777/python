# Dictionary(딕셔너리)
# Key-value 쌍으로 데이터를 저장하는 자료구조
# Hash 테이블 기반으로 빠른 검색 속도
# 파이썬의 가장 강력하고 유용한 자료구조 중 하나

import copy
students_ids = ["20230001", "20230002", "20230003"]
students_names = ["김철수", "이영희", "박민수"]

# 특정 학번의 이름을 찾으려면?
target_id = "20230002"
if target_id in students_ids:
    index = students_ids.index(target_id)
    name = students_names[index]
    print(name)

# 딕셔너리를 사용하는 경우 - 직관적이고 빠름
students = {
    "20230001" "김철수",
    "20230002" "이영희",
    "20230003" "박민수"
}

# print(students["2023002"])

# 특징
# Key-Value 쌍 : 각 값에 고유한 키로 접근
# 빠른 검색: o(1) 시간 복잡도
# 변경 가능 (Mutable): 요소 추가, 수정, 삭제 가능
# Key는 유일 : 중복 키 불가(값은 중복 가능)
# 순서 보장 : Python3.7+ 부터 삽입 순서 유지
# 3.1.1 첫번째: 큰 패치 두번째:  세번째:

# Dictionary 생성
empty_dict = {}
empty_set = set()
print(type(empty_dict))
print(type(empty_set))

# 2. 값이 있는 딕셔너리 생성
person = {
    "name" "김철수",
    "age" "25",
    "city" "seoul"
}
print(person)

# 3. dict() 생성자 사용
person2 = dict(name="이영희", age=25, city="부산")
print(person2)

# 4. 리스트/튜플로부터 생성
# pairs = [("a", 1), ("b, 2")]
# dict_form_pairs = dict(pairs)

# 5. zip()를 이용한 생성
keys = ["name", "age", "city"]
values = ["박민수", "25", "대전"]

person3 = dict(zip(keys, values))
print(person3)

# 6. dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares)

# 7. fromkeys() 메서드
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)
print(default_dict)

# key로 사용 가능한 타입
# Hashable 타입만 key로 사용 가능
valid_dict = {
    1: "정수",
    3.14: "실수",
    "문자열": "string",
    (1, 2): "튜플",
    True: "불리언",
    frozenset([1, 2]): "frozenset"
}

# UnHashable 타입은 key로 사용 불가
# invalid_dict = {
#     [1, 2]: "리스트",
#     {1, 2}: "set",
#     {"a": 1}: "딕셔너리"
# }


#  접근과 수정
student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학",
    "gpa": "3,7"
}

# 1. 대괄호 표기법 (KeyError 위험)
name = student["name"]
print(name)
# grade = student["grade"]
# print("grade", grade)

# get() 메서드(안전한 접근)
major = student.get("major")
print("major", major)

grade1 = student.get("grade")
print("grade", grade1)

grade2 = student.get("grade", "N/A")
print("grade2", grade2)

# keys(), values(), item()
print(student.keys)
print(student.values)
print(student.items)

student = {
    "name": "김철수",
    "age": 20,
    "major": "컴퓨터공학",
    "gpa": "3,7"
}

# 값 수정, 추가
student["age"] = 30
print(student)

student["grade"] = 3
print(student)

# update() 메서드로 여러 값을 한번에 추가
student.update({
    "gpa": 4.0,
    "city": "seoul",
    "email": "hotdog@gmail.com"
})
print(student)

info_dict = {"age": 22, "grade": 1, "phone": "010-1122-1122"}
student.update(info_dict)
print(student)

# 값 삭제
# del 키워드
del student["grade"]
print(student)

# pop() 메서드 값을 반환하면서 삭제
popped = student.pop("phone")
print(popped)
print(student)

# popitem() - 마지막 항목 제거
last_item = student.popitem()
print(last_item)

student.clear()
print(student)

# 중요 메서드들
scores = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78
}

# setdefaults() - 키가 없으면 추가, 있으면 기존 값 반환
scores.setdefault("정수진", 88)  # 새로 추가
scores.setdefault("김철수", 100)
print(scores)


# copy() - 얕은 복사
scores_copy = scores.copy()
scores_copy["최동훈"] = 95
print("scores", scores)
print("\nscores_copy", scores_copy)


# deepcopy() - 깊은 복사
nested_dict = {
    "team1": {'leaders': '김철수', 'members': ['이영희', '박민수'],
              "team2": {'leaders': '정수진', 'members': ['최동훈', '강미나']
                        }
              }
}

shallow = nested_dict.copy()
deep = copy.deepcopy(nested_dict)

nested_dict["team1"]["members"].append("신입")
print("shallow: ", shallow["team1"]["members"])  # 영향 없고
print("deep: ", deep["team1"]["members"])  # 영향 있다

#  키만 순회 (기본)
for key in scores:
    print(f"{key}: {scores[key]}")

for key in scores.keys():
    print(f"{key}: {scores[key]}")


for value in scores.values():
    print(f"{value}")

# 평균 값 개산
average = sum(scores.values()) / len(scores)
print("average", average)

# 키 - 값 쌍 순회
for key, value in scores.items():
    print(f"{key}: {value}")

for idx, (key, value) in enumerate(scores.items()):  # 몇개 있는지 개수를
    print(f"{idx}번째 {key} : {value}점")
