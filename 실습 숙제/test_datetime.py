import datetime
import calendar
# 사용자로부터 생일(월-일 예 07-25)을 입력 받으세요.
# 오늘 날짜를 기준으로 올해 또는 내년의 생일까지 남은 날짜(일 수)를 계산해서 출력하세요
#   올해 생일이 지났으면 내년까지 남은 일수로, 아직 안 지났으면 올해 생일까지 남은 일수로 계산


birth = input("생일을 입력해주세요(예시 07-25): ")
month, day = map(int, birth.split("-"))
today = datetime.date.today()
birthday = datetime.date(today.year, month, day)
if birthday < today:
    birthday = datetime.date(today.year + 1, month, day)

d_day = (birthday - today).days

print(f"생일까지 {d_day}일 남았습니다.")
