# 상속
'''
    기존 클래스의 속성과 매서드를 물려받아 새로운 클래스를 만드는 것

    동물: 포유류 -> 개, 고양이(공통 특징: 자기, 먹기)
    자동차: 차량 -> 승용차, 트럭
    가족: 부모 -> 자식
'''

# 상속 없이 - 코드가 중복이 심각!


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}이 잠을 잡니다.")

    def sleep(self):
        print(f"{self.name}이(가) 잠을 잡니다.")

    def meow(self):
        print(f"{self.name}이(가) 울부 짓습니다.")

# 기본 문법과 용어


# class 부모 클래스:
#     pass


# calss 자식클래스(부모클래스):  # 괄호 안에 부모 클래스
#     pass

# 자식은 부모의 모든 것을 물려 받습니다.
# 부모의 모든 속성과 매서드를 자동으로 사용 가능
# 추가된 자신만의 속성과 매서드 정의 가능


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"안녕하세요, {self.name}입니다.")


class Student(Person):
    def study(self):
        print(f"{self.name}이(가) 공부합니다.")


class Teacher(Person):
    def teach(self):
        print(f"{self.name}이(가) 수업합니다.")


student = Student("김학생", 20)
teacher = Teacher("박선생", 30)

student.greet()
teacher.greet()

student.study()
teacher.teach()

# super()와 생성자 상속
# super()는 자식 자식 클래스에서 부모 클래스에 접근할때

# super() 없이 문제 발생!


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person 생성: {name} {age}살")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        print(f"student 생성: 학번 {student_id}")


student = Student("김철수", 20, "20250001")
print(student.name)
