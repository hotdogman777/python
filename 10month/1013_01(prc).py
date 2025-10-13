# 다음 데이터를 CSV로 저장하고 다시 읽어오세요
import pandas as pd

practice_data = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['Seoul', 'Busan', 'Daegu']
})

practice_data.to_csv("practice_data.csv")
df = pd.read_csv("practice_data.csv")
print(df)
print()


# TODO:
# 1. 'practice.csv'로 저장 (인덱스 제외)
# 2. 저장한 파일 읽어오기
# 3. 읽어온 데이터 출력


# 한글 데이터를 UTF-8로 저장하고 읽어오세요

korean_data = pd.DataFrame({
    '이름': ['김철수', '이영희', '박민수'],
    '직급': ['사원', '대리', '과장']
})

korean_data.to_csv("korean_data.csv", index=False, encoding="utf-8-sig")
df = pd.read_csv("korean_data.csv", encoding="utf-8-sig")
print(df)
print()

# TODO:
# 1. UTF-8 인코딩으로 저장
# 2. 같은 인코딩으로 읽어오기
# 3. 한글이 깨지지 않았는지 확인

data = {
    "이름": ["홍길동", "이순신", "김유신", "강감찬", "장보고", "이방원"],
    "나이": [23, 35, 31, 40, 28, 34],
    "직업": ["학생", "군인", "장군", "장군", "상인", "왕자"]
}
df = pd.DataFrame(data)

# 인덱싱

print(["=== 인덱싱 ==="])
print(df["이름"])
print(df[["이름", "나이", "직업"]])
print()

# 슬라이싱
print(df[1:3])
print()
print(df[-2:])
print()

# DataFrame의 슬라이싱은 행(Row) 기준으로 동작한다.
# 열 단위 슬라이싱은 명시적으로 지정
print(df[-2:]["이름"])
print()

# iloc

print("=== iloc ===")
print(df)
print(df.iloc[0])  # 0번 행 전체
print()
print(df.iloc[:, 1])  # 모든 행의 1번(컬럼) 나이
print()
print(df.iloc[[0, 2, 4], [0, 2]])  # 모든 행의 1번(컬럼) 나이
print()

# loc
print("=== loc ===")
print(df.loc[0])
print()
print(df.loc[:, "나이"])
print()
print(df.loc[:, ["이름", "나이"]])
print()
print(df.loc[1:3, "나이"])
print()
