import pandas as pd

# DataFrame vs Series

# Series
# 1차원

# DataFrame
# 2차원 (Series들의 묶음)
# 데이터 (values) - 2차원 배열
# 행 인덱스(index) - 각 행의 레이블
# 열 이름 (columns) - 각 열의 레이블

df_default = pd.DataFrame({
    "name": ["Kim", "Lee", "Park"],
    "age": [25, 26, 27]
})


print(f"인덱스: {df_default}")
print(f"인덱스: {df_default.index}")
print(f"인덱스: {df_default.columns.tolist()}")
