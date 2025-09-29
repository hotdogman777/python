# 추상 클래스
'''
    직접 객체를 만들 수 없고,
    반드시 상속 받아서 완성해야 사용할수 있는 미완성 설계도

    동물 실제로 "동물"만 있는건 없고, 개 , 고양이, 새, 등 구체적인 동물이 있음
    악기 추상적 개념, 피아노, 기타, 드럼, 등이 있어야 연주 가능
'''


# 추상 클래스 사용

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


class Dog(Animal):
    def make_sound(self):
        pass

    def eat(self):
        print("강아지가 밥을 먹습니다.")


# 문제 발생
dog = Dog()


class 추상클래스이름(ABC):
    @abstractmethod
    def 추상메소스일름(self):
        pass


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, redius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


circle = Circle(5)
print(circle.area())


class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name}이(가) 잠을 잡니다.")

    def eat(self):
        print(f"{self.name}이(가) 먹이를 먹습니다.")

# 추상 메서드 - 각 동물마다 다르게 구현해야 함


@abstractmethod
def make_sound(self):
    pass


@abstractmethod
def move(self):
    pass


class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} 짹짹!")

    def move(self):
        print(f"{self.name}이(가) 날아갑니다.")


dog = Dog("바둑이", 3)
bird = Bird("새대갈", 5)
print()
print()
