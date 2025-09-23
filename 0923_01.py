# 실습 4

class Shape(self):
    def __init__(self, sides, base):
        self.sides = sides
        self.base = base

    def printInfo(self):
        print(f"변의 개수: {self.sides}")
        print(f"밑변의 길이: {self.base}")

    def area(self):
        print(f"넓이 계산이 정의되지 않았습니다.")


class Rectangle(Shape):
    def __init__(self, sides, base, height):
