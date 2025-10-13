import pandas as pd

print(pd.__version__)

# 데이터 분석
# 과정
# 데이터 수집 -> 데이터 정제
# 데이터 탐색 -> 데이터 분석 -> 시각화
# 인사이트 도출

'''
 1. 데이터 수집
        분석할 자료를 모으는 단계
 2. 데이터 정제
        분석 가능한 형태로 만드는 단계
 3. 데이터 탐색
        데이터의 특성을 파악하는 단계
 4. 데이터 분석
        가설을 검증하고 패턴을 찾는 단계
 5. 시각화
        결과를 이해하기 쉽게 표현하는 단계
 6. 인사이트 도출
        분석 결과를 의사결정에 활용하는 단계
'''

'''
    편의점 사장님의 고민
    문제: 어떤 제품을 더 많이 주문해야할까?
    데이터: 지난 3개월 판매 기록
    분석: 요일별, 시간대별 판매 패턴 파악
    인사이트: 금요일 저녁에 맥주가 가장 많이 팔린다.
    행동: 금요일 전에 맥주 제고 확충

    대형 마트? =>
    기저귀와 맥주
    
'''

# Excel, Pandas 비교

'''
    Excel 로 100만개 데이터를 처리한다면?
    2019 버젼 1000000행 까지만 제한 되었습니다.
    파일 열기만 해도 5분 이상 소요
    수식 계산 시 프로그램 멈춤
    반복 작업을 매번 수동으로 해야함
    Pandas 
'''

# Series
temp_list = [15.5, 17.2, 18.9, 19.1, 20.1]
temp = pd.Series(temp_list, name="4월_기온")
print(temp)
print()

date = pd.date_range("2025-04-01", periods=5)
print(date)
temp_date = pd.Series(temp_list, index=date, name="4월_기온")
print(temp_date)
print()

product = {
    "노트북": 15,
    "마우스": 40,
    "키보드": 20
}

product_series = pd.Series(product, name="현재재고")
print(product_series)
print()


scalar_series = pd.Series(0,
                          index=["월", "화", "수", "목", "금"],
                          name="판매량")
print(scalar_series)
print()

'''
    1. 1차원 배열: 데이터가 일렬로 나열되어 있다.
    2. 레이브(인덱스) 보유: 각 데이터에 이름표를 붙일 수 있다.
    3. 동일 타입: 하나의 series 안의 모든 데이터는 같은 타입

'''
simple_series = pd.Series([10, 20, 30, 40, 50])
print(simple_series)
print()

'''
    Series = Value(값) + Index(인덱스) + Name(이름)

    매개변수 설명
    data=None 실제 데이터(필수)
        - 리스트, 딕셔너리, 스칼라값, Numpy 배열
    Index=None 인덱스 레이블(선택)
    
'''

data_series = pd.Series(
    data=[10, 20, 30, 40, 50],
    index=["Alice", "Bob", "Charlie", "David", "Eve"],
    name="Test_Score"
)


'''
    각 구성요소의 역할:
    Value(값)
        실제 데이터가 저장되는 부분
        Numpy 배열로 저장됨
        빠른 수치 연산 가능
    Index(인덱스)
        각 값을 식별하는 레이블
        기본값: 0,1,2,.....(정수)
        사용자 정의 가능(문자열, 날짜 등)
    Name(이름)
        Series 전체를 설명하는 이름
        선택사항(없이도 됨)
        DataFrame 결합 시 컬럼명이 됨
'''

int_series = pd.Series([1, 2, 3, 4, 5])
print(f"Integer Series dtype: {int_series}")

float_series = pd.Series([1.1, 2.2, 3.3, 4.4, 5.5])
print(f"Float Series dtype: {float_series}")

str_series = pd.Series(["Apple", "Cherry", "Banana"])
print(f"String Series dtype: {str_series}")

bool_series = pd.Series([True, False, True])
print(f"boolean Series dtype: {bool_series}")

mixed_series = pd.Series([1, 2.5, 3])
print(f"mixed Series dtype: {mixed_series}")


test_scores = pd.Series(
    data=[85, 55, 63, 53, 33],
    index=["Alice", "Bob", "Charlie", "David", "Eve"],
    name="Exam"
)

print("=== Series 속성 전체 ===")
print("1. Valuse (값들)")
print(test_scores.values)
print()

print("2. index (인덱스)")
print(test_scores.index)
print()

print("3. name (인덱스)")
print(test_scores.name)
print()

print("4. dtype (타입)")
print(test_scores.dtype)
print()

print("5. shape (모양)")
print(test_scores.shape)
print()

print("6. size (크기)")
print(test_scores.size)
print()

print("7. ndim (차원)")
print(test_scores.ndim)
print()

# 인덱싱과 슬라이싱

# 인덱싱
# Series에서 특정 데이터를 선택하는 방법
# 위치 기반 0, 1, 2
# 레이블 기반: 인덱스 이름으로 접근

sales = pd.Series(
    [100, 200, 150, 300],
    index=["Mon", "Tue", "Wed", "Thu"],
    name="Daily_Sales"
)

wed_sales = sales["Wed"]
print("수요일 매출", wed_sales)
print()

wed_sales2 = sales[2]
print("수요일 매출", wed_sales2)

selected_days = sales[["Mon", "Wed", "Thu"]]
print(selected_days)
print()
