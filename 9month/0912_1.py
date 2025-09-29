#  실습3 문제1

train = ["철수", "영희"]
train1 = ["민수", "지훈"]
del train[1]
train.insert(0, "수진")
del train1[0]
train2 = train + train1
print(train2[::-1])

# 실습3 문제2

card = [5, 3, 7]
card.extend([4, 9])
max_num = max(card)
min_num = min(card)
print(max_num)
print(min_num)
print(sum(card))
card.pop()
print(card)
