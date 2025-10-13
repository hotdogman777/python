import pandas as pd
import numpy as np

missing_types = pd.DataFrame({
    'none_type': [1, 2, None, 4],           # Python None
    'nan_type': [1, 2, np.nan, 4],         # NumPy NaN
    'empty_string': ['A', 'B', '', 'D'],   # 빈 문자열
    'whitespace': ['A', 'B', ' ', 'D'],    # 공백
    'special_value': [1, 2, -999, 4]       # -999를 결측값으로 사용하는 경우
})

print(missing_types)

# 결측값 탐지
# isnull() / isna()
# 결측값이면 True

# notna() / notnull()
# 값이 있으면 True
print("=== isna ===")
print(missing_types.isna())
print(missing_types.isnull())

print("=== notna ===")
print(missing_types.notna())
print(missing_types.notnull())

# 결측값 통계 확인
print("=== 열별 결측값 개수 ===")
print(missing_types.isna().sum())

# 전체 결측값 개수
print(missing_types.isna().sum().sum())

# 결측값 처리 전략

'''
    삭제 - 결측값이 있는 행/열 제거
    대체 - 다른 값으로 채우기
    예측 - 앞뒤 값이나 패턴으로 추정
'''

# 결측값이 있는 샘플 데이터
sales_data = pd.DataFrame({
    'date': pd.date_range('2024-01-01', periods=7),
    'sales': [100, 120, np.nan, 150, np.nan, 180, 200],
    'customers': [20, 25, 22, np.nan, 30, 35, 40],
    'region': ['Seoul', 'Busan', np.nan, 'Daegu', 'Seoul', np.nan, 'Busan']
})
print("=== 원본 ===")
print(sales_data)
print()

# 삭제
# 1-1 결측값이 있는 행 전체 삭제
drop_rows = sales_data.dropna()
print("결측값이 있는 행 삭제:")
print(drop_rows)

# 1-2 결측값이 있는 열 전체 삭제
drop_cols = sales_data.dropna(axis=1)
print("결측값이 있는 열 삭제:")
print(drop_cols)
print()

# 1-3 특정 열 기준 삭제
drop_sales = sales_data.dropna(subset=["sales"])
print("sales 열 기준으로만 삭제:")
print(drop_sales)
print()

# 대체
# 2-1 평균값으로 대체
fill_mean = sales_data.copy()
fill_mean["sales"] = fill_mean["sales"].fillna(fill_mean["sales"].mean())
print(fill_mean)
print()

# 2-2 중앙값으로 대체
fill_median = sales_data.copy()
fill_median["sales"] = fill_median["sales"].fillna(fill_median["sales"].median())
print(fill_median)
print()

# 시계열 대체
# 시간 순서가 있는 데이터에서 앞뒤 값으로 결측값을 채운다.
# 3-1
fill_forward = sales_data.copy()
fill_forward["sales"] = fill_forward["sales"].ffill()
print(fill_forward)
print()

# 3-2 BackWord Fill (뒤의 값으로 채우기)
fill_backword = sales_data.copy()
fill_backword["sales"] = fill_backword["sales"].bfill()


data = {
    "도시": ["서울", "부산", "광주", "대구", np.nan, "춘천"],
    "미세먼지": [45, 51, np.nan, 38, 49, np.nan],
    "초미세먼지": [20, np.nan, 17, 18, 22, 19],
    "강수량": [0.0, 2.5, 1.0, np.nan, 3.1, 0.0]
}
df = pd.DataFrame(data)


# 실습4. 통계함수·결측값 처리 연습(2)
# 1. ‘미세먼지’ 컬럼의 평균과 중앙값을 구하세요.
mean1 = df["미세먼지"].mean
median1 = df["미세먼지"].median

print("미세먼지 평균:", mean1)
print("미세먼지 중앙값:", median1)
# 2. ‘초미세먼지’ 컬럼의 최댓값과 최솟값을 구하세요. min max
max1 = df["초미세먼지"].max()
min1 = df["초미세먼지"].min()

print("초미세먼지 최댓값:", max1)
print("초미세먼지 최솟값:", min1)

# 3. 각 컬럼별 결측값 개수를 구하세요.
print("=== 각 컬럼별 결측값 개수 ===")
print(df.isna().sum())
# 4. 결측값이 하나라도 있는 행을 모두 삭제한 뒤, 남은 데이터의 ‘초미세먼지’ 평균을 구하세요.
drop_rows = df.dropna()
mean2 = drop_rows["초미세먼지"].mean
print("초미세먼지 평균:", mean2)
print()
# 5. 결측값을 모두 0으로 채운 뒤,
# ‘미세먼지’와 ‘초미세먼지’의 합계를 각각 구하세요.
fill_mean = df.fillna(0)
sum_dust = fill_mean["미세먼지"].sum()
sum_micro = fill_mean["초미세먼지"].sum()
print(fill_mean)
print("미세먼지 합계:", sum_dust)
print("초미세먼지 합계:", sum_micro)
# 6. ‘미세먼지’ 컬럼의 결측값을 평균값으로 채운 뒤, 그 표준편차를 구하세요.
mean_value = df["미세먼지"].mean()
df["미세먼지"] = df["미세먼지"].fillna(mean_value)
std_value = df["미세먼지"].std()
print("미세먼지 평균:", mean_value)
print("미세먼지 표준편차:", std_value)
