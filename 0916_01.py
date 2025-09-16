# 실습 1. 딕셔너리 종합 연습 문제(1)
user = {"username": "skywalker", "email": "sky@example.com", "level": "5"}
print(user["email"])
user["level"] = "6"
print(user)

# 실습 2.
print(user.get("phone", "미입력"))
user.update({
    "nickname": "sky"
})
print(user)
del user["email"]
print(user)
print(user.get("signup_date"))
user.setdefault("signup_date", "2025-07-10")
print(user)

# 실습 3. 빈 딕셔너리를 안만듬 3문제다...ㅋㅋ
students = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 95
}
students.update({
    "David": 80
})
students["Alice"] = 88
del students["Bob"]
print(students)
