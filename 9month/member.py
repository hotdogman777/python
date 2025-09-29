# member = input("회원이름을 입력하세요: ")

# with open("member.txt", "w", encoding="utf-8") as f:
#     for i in range(3):
#         user_id = input("이름을 입력 하세요: ")
#         user_pw = input("비밀번호를 입력 하세요: ")
#         f.write(f"{user_id} {user_pw}\n")

# with open("member.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line.split()[0])
#     contant = f.read()
#     print(contant)

# # 사용자에게 이름을 입력하세요라는 메세지를 출력한 뒤 이름 입력 받기
# # 사용자에게 비밀번호를 입력하세요라는 메세지를 출력한 뒤 비번 입력 받기
# # member.txt에서 한줄씩 이름과 비번을 검사하여 로그인 성공 시 로그인 성공 실패시 로그인 실패 출력
# with open("member.txt", "r", encoding="utf-8") as f:
#     input_id = input("이름을 입력하세요: ")
#     input_pw = input("비밀번호를 입력하세요: ")
#     for line in f:
#         user_id, user_pw = line.split()
#         if user_id == input_id and user_pw == input_pw:
#             print("로그인 성공")
#             input_phone = input("전화번호를 입력하세요: ")

#             members = {}

#             with open("member.tel.txt", "a", encoding="utf-8") as f2:
#                 for line in f2:
#                     saved_name, saved_phone = line.strip().split()
#                     members[saved_name] = saved_phone

#             members[input_id] = input_phone

#             with open("member.tel.txt", "a", encoding="utf-8") as f2:
#                 for name, phone in members.items():
#                     f2.write(f"{name} {phone}")
#                     break
#         else:
#             print("로그인 실패")


with open("what.png", "rb") as f1:
    img = f1.read()

with open("./whats.png", "wb") as f2:
    f2.write(img)
