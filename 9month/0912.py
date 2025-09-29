list1 = list()

list2 = list("Hello")

# H  e  l  l  o
# 0  1  2  3  4
# 0 -4 -3 -2 -1

print(list1)
print(list2)

print(list2[0])

list2[4] = "a"
print("list2", list2)

# text = "python"
# text[1] = "a"
# print("text", text)


list3 = list("Python")
text3 = "Hello"
print("list3[:]", list3[:])
print("text3[:3]", text3[:3])
print("text3[-3:-1]", text3[-3:-1])

print("text3[::-1]", text3[::-1])
print("text3[::-2]", text3[::-2])
print("text3[:-4:-2]", text3[:-4:-2])

numbers = [10, 20, 30, 40]

print("numbers[1:3]", numbers[1:3])
print("numbers[:3:2]", numbers[:3:2])
print("numbers 뒤집기", numbers[::-1])

# 실습 1번
nums = [10, 20, 30, 40, 50]
print("nums[::4]", nums[::4])

# 실습 2번
nums = [100, 200, 300, 400, 500, 600, 700]
print("nums[2:5]", nums[2:5])

# 실습 3번
nums = [1, 2, 3, 4, 5]
for i in range(5):
    nums[i] *= 2
print("리스트의 원소 두배 하기 : ", nums)

# 실습 4번
items = ["a", "b", "c", "d", "e"]
print("리스트 역순으로 뒤집기", items[::-1])

# 실습 5번
data = ["zero", "one", "two", "three", "four", "five"]
print("짝수 인덱스 호출 : ", data[::2])

# 실습 6번
movies = ["인셉션", "인터스텔라", "어벤져스", "라라랜드", "기생충"]
movies[2:4] = "매트릭스", "타이타닉"
print("슬라이싱 변경 : ", movies)

# 실습 7번
subjects = ["국어", "수학", "영어", "물리", "화학", "생물", "역사", "지구과학", "윤리"]
print(subjects[3::2])

# 실습 8번
data = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
datas = data[:3]
datass = data[3:6]
datasss = data[6:]
print(datas[::-1], datass[::-1], datasss[::-1])

# 실습2 문제1번
fruits = ["apple", "banana", "cherry", "grape", "watermelon", "strawberry"]
del fruits[1:4]
a = fruits
b = fruits + a
print(fruits)

# 실습 문제2번
letters = ["A", "B"]
a = letters * 3
del a[2]
print(a)

#  실습3 문제1

train = ["철수", "영희"]
train1 = ["민수", "지훈"]
del train[1]
train.insert(0, "수진")
del train1[0:-1]
train

# 3인덱스 요소를 삭제
list1 = [10, 20, 30, 40, 50]

del list1[3]
print(list1)

del list1[1:3]
print(list1)

# del list1
# print(list1)

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3, 4, 5]

result = list1 + list2
print(result)

result = list1 * 3
print(result)

print(1 not in list1)

# 요소 추가 매소드
number = ["10", "25", "32", "55"]

numbers.append(20)
print(numbers)

numbers.append(12)
print(numbers)

numbers.extend([19])
print(numbers)

numbers.extend([5, 29])
print(numbers)

numbers.insert(2, 30)
print(numbers)

fruits = ["사과", "바나나", "오렌지", "바나나", "포도"]
fruits.remove("바나나")
print(fruits)

removed = fruits.pop(1)
print(removed)
print(fruits)

fruits.clear()
print(fruits)

numbers = [1, 2, 3, 9, 4, 5, 3, 2, 5]
idx = numbers.index(9)
print("idx: ", idx)

count = numbers.count(2)
print("count: ", count)

numbers.sort()
print("numbers: ", numbers)


numbers.sort(reverse=True)
print("numbers: ", numbers)

original = [3, 2, 5, 7, 1]
sorted_list = sorted(original)
sorted_r_list = sorted(original, reverse=True)

print("original: ", original)
print("sorted_list: ", sorted_list)


numbers = [5, 2, 7, 3, 11, 22, 22, 35, 45, 99]
max_num = max(numbers)
min_num = min(numbers)

print(max_num)
print(min_num)
