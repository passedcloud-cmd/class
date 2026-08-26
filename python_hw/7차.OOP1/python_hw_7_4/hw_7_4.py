# 아래 클래스를 수정하시오.
# 사람의 이름과 나이를 입력받아 소개하는 Person 클래스
# introduce 인스턴스 메서드 포함
# 인스턴스가 생성될 때마다 증가하는 number_of_people 클래스 변수 작성

class Person:
    number_of_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count_people()

    def introduce(self):
        print(f'제 이름은 {self.name} 이고, 저는 {self.age}살 입니다.')

    @classmethod
    def count_people(cls):
        cls.number_of_people += 1

person1 = Person("Alice", 25)
person1.introduce()
print(Person.number_of_people)
