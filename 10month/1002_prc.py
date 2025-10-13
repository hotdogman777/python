import pandas as pd
# 1. 파이썬 리스트 [5, 10, 15, 20]을 이용해 Series를 생성하세요.
temp = pd.Series([5, 10, 15, 20])
print(temp)
print()
# 2. 값 [90, 80, 85, 70]에 대해 인덱스를 각각 '국어', '영어', '수학', '과학'으로 지정한 Series를 만드세요.
d = pd.Series([90, 80, 85, 70], index=["국어", "영어", "수학", "과학"])
print(d)
print()
# 3. {'서울': 950, '부산': 340, '인천": 520} 딕셔너리를 이용해 Series를 만들고, 인천의
h = {"서울": 950, "부산": 200, "대구": 300, "인천": 520}
is3 = pd.Series(h)
print(is3["인천"])
print()

# 4. Series [1, 2, 3, 4]를 만들고, 데이터 타입(dtype)을 출력하세요.
s = pd.Series([1, 2, 3, 4])
print("dtype: ", s.dtype)
print()

# 5. 아래 두 Series의 합을 구하세요.

s1 = pd.Series([3, 5, 7], index=['a', 'b', 'c'])
s2 = pd.Series([10, 20, 30], index=['b', 'c', 'd'])
result = s1 + s2
print(result)
print()

# 6. Series [1, 2, 3, 4, 5]의 각 값에 10을 더한 Series를 만드세요.
s = pd.Series([1, 2, 3, 4, 5])
print(s + 10)
print()


# 1. 다음 데이터로 DataFrame을 생성하고, 컬럼명을 '이름', '나이', '도시'로 지정하세요.
# • [['홍길동', 28, '서울'], ['김철수', 33,'부산'], ['이영희', 25, '대구']]

data = pd.DataFrame(
    [["홍길동", 28, "서울"], ["김철수", 33, "부산"], ["이영희", 25, "대구"]]
)
print(data)
print()
# 2. 아래와 같은 딕셔너리로 DataFrame을 생성하세요.
# {'A': [1, 2, 3], 'B': [4, 5, 6]}
data = pd.DataFrame({
    'A': [1, 2, 3], 'B': [4, 5, 6]
})
print(data)
print()
# 3. 아래 데이터를 사용해 DataFrame을 만드세요.
# • ['과목':'수학', '점수': 90}, {'과목': '영어', '점수': 85}, {'과목': '과학', '점수': 95}]
data = pd.DataFrame({
    "과목": ["수학", "영어", "과학"],
    "점수": [90, 85, 95]
})
print(data)
print()
# 4. 아래 데이터를 사용해 DataFrame을 생성하되, 인덱스를 ['학생1', '학생2', '학생3']으로 지정
# 하세요.
stu1 = pd.Series([80, 92, 77], index=["학생1", "학생2", "학생3"])
stu2 = pd.Series(["민수", "영희", "철수"], index=["학생1", "학생2", "학생3"])
data = pd.DataFrame({"이름": stu2, "점수": stu1})

print(data)
print()
# • {'이름': ['민수' '영희', '철수'], '점수': [80, 92, 77]}

# 5. 아래 Series 객체 2개를 이용해 DataFrame을 만드세요.
kor = pd.Series([90, 85, 80], index=['a', 'b', 'c'])
eng = pd.Series([95, 88, 82], index=['a', 'b', 'c'])
data = pd.Series({"kor": kor, "eng": eng})

print(data)
print()

# 6. 아래 딕셔너리로 DataFrame을 만들고, 컬럼 순서를 ['B', 'A']로 지정해 출력하세요.
data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})

print(data[["B", "A"]])
print()
# 7. 데이터를 DataFrame으로 만들고, 컬럼명을 ['product', 'price', 'stock']으로 변경하세요.
data = pd.DataFrame([['펜', 1000, 50], ['노트', 2000, 30]],
                    columns=["product", "price", "stock"])
print(data)
print()

# 8. 아래 DataFrame을 생성한 뒤, '국가' 컬럼만 추출하세요.
data = pd.DataFrame({'국가': ['한국', '일본', '미국'], '수도': ['서울', '도쿄', '워싱턴']})

print(data["국가"])
print()
