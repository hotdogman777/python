# 파일 입출력
'''
    파일 입출력(File I/0)은 프로그램이 파일을 익고(Input) 쓰는(Output) 작업입니다.
    프로그램이 종료 되어도 데이터를 보관할 수 있는 유일한 방법
    프로그램의 데이터는 메모리에 저장되는데 프로그램이 종료되면 메모리의 데이터는 시작 파일로 저장하면 하드디스크에 영구 저장
'''

'''
    1. 설정 파일 저장: 게임 설정, 프로그램 옵션
    2. 데이터 백업: 중요한 정보 보관
    3. 로그 기록: 프로그램 실행 기록, 에러 추적
    4. 데이터 교화 : 엑셀, csv 파일로 다른 프로그램과 데이터
    5. 대용량 처리: 메모리에 다 못 담는 빅데이터 처리


'''
# 위험한 방법 - 파일을 안 닫을 수 있기 때문에
file = open("hello.txt", "r", encoding="utf8")

content = file.read()
print(content)

file.close()

# 안전한 방법 2 - with문
with open("hello.txt", "r", encoding="utf8") as f:
    content = f.read()
    print(content)
# with 사용하면 자동으로 close() 됨

# 새 파일 생성 또는 덮어쓰기
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("파이썬 파일 입출력\n")

with open("output.txt", "a", encoding="utf-8") as f:  # a = 추가 하고 싶으면 생성한 파일 밑에 w는 덮어쓰기
    f.write("추가된 내용!\n")

# 1. read() - 파일 전체를 하나의 문자열로
with open("hello.txt", "r", encoding="utf-8") as f:
    contant = f.read()
    print(content)


# 2, read(크기) - 저장한 크기만큼만
with open("hello.txt", "r", encoding="utf-8") as f:
    content = f.read(3)
    print(content)

# 2. readline() - 한줄씩 읽기
print("2. readline() - 한 줄씩 읽기")
