import pandas as pd

# CSV
# CSV(comma-Separated Valuse) 가장 널리 사용되는 데이터 파일 형식

'''
    특징
    쉼표(,)로 값을 구분
    텍스트 파일이라 어디서나 열람 가능
    가볍고 빠름
    Excel, Google sheets 등과 호환
'''

# CSV 파일 예시 내용
'''
    name, age, city, salary
    john, 25, Seoul, 50000
    john, 25, Seoul, 50000
    john, 25, Seoul, 50000
'''


sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 70000]
})

# CP949로 저장 (Windows 한글)
# sample_data.to_csv("sample_data.csv", index=False, encoding="cp949")

sample_data.to_csv("sample_data.csv", index=False,
                   encoding="utf-8-sig")

df = pd.read_csv("sample_data.csv", encoding="utf-8-sig")

print("=== csv 파일 읽기 ===")
print(f"데이터 타입\n {df.dtypes}")
print(f"데이터 크기\n {df.shape}")

sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 70000]
})

# seq - 구분자 설정
sample_data.to_csv("tab_separated.txt", sep="\t", index=False)

df_tab = pd.read_csv("tab_separated.txt", sep="\t")

print("==== CSV sep=탭 파일 읽기 ====")
print(df_tab)
print(df.head)
print(df.tail)
print()

# Excel
# 엑셀은 마이크로소프트의 스프레드시트 프로그램입니다.
'''
    특징
    여러 시트(Sheet) 지원
    서식, 수식 포함 가능
    비즈니스에서 가장 많이 사용
    확장자 (.xlsx)최신 (.xls)구버전
    pip install openpyxl
'''

sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 70000]
})

sample_data.to_excel("sample_data.xlsx", index=False, sheet_name="Default")
print("샘플 엑셀 파일 생성 완료")

df_excel = pd.read_excel("sample_data.xlsx")
print("=== Excel 파일 읽기 ===")
print(df_excel)

sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 70000]
})

# 여러 시트 다루기
with pd.ExcelWriter("multi_sheet.xlsx") as writer:
    sample_data.to_excel(writer, sheet_name="Default1", index=False)
    sample_data["name"].to_excel(writer, sheet_name="name", index=False)

print("시트 2개가 생긴지 확인")

# JSON
# JSON(JavaScript Object Notation)
# 웹에서 많이 사용하는 데이터 형식
sample_data = pd.DataFrame({
    "name": ["John", "Jane", "Park"],
    "age": [25, 30, 35],
    "city": ["서울", "부산", "대구"],
    "salary": [50000, 60000, 70000]
})

sample_data.to_json("sample_data.json", orient="records", indent=2)
print("JSON 파일 저장")
print()

df_json = pd.read_json("sample_data.json")
print("=== JSON 파일 읽기 ===")
print(df_json)
print()
