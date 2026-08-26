# print('dasqwderf'.index('s'))
# print('wqeopdamfnj'.find('i'))
# print('Apple'.replace('A','B'))
# print('!!!sded!'.strip('!'))
# print('dsaed dwa/d dawef'.split())
# print(" ".join('das ead da./ !'))
# print('dawdstr'.capitalize())
# print('dawWDDWW'.swapcase())
# print('dasefa'.upper())
# print('dasWAD'.lower())


# a = [12,1,1,1,3,44,5,67,9,765,41]
# a.append(3)
# print(a)
# a.extend([5, 7])
# print(a)
# a.insert(1, 1111)
# print(a)
# a.remove(1)
# print(a)
# a.pop()
# print(a)
# a.pop(3)
# print(a)
# a.reverse()
# print(a)
# print(sorted(a)) 

# list0 = [1,2,3,4]
# print(list(map(lambda x: x *3, list0)))
# list1 = [x * 2 for x in [1,2,3,4,5]]
# print(list1)


# dict1 = {'a': 'apple', 'b': 'bad apple'}
# print(dict1.get('c', "없으면 None 반환"))
# print(list(dict1.values()))
# print(list(dict1.values()))
# print(list(dict1.items()))
# print(dict1.setdefault('a', "없으면 None 반환"))
# dict1.update(a ='pineapple')
# print(dict1)
# dict1.pop('a')
# print(dict1)
# dict1['a'] = 'apple'
# print(dict1)


print(5 != 0) #true

x = 0
print(x or 5) # 5가 출력됨 # 0은 False로 취급되기 때문에 다음으로 넘어감.
print(1 and x and 5) # 0이 출력됨

print(0o10) # 8



print('함수 호출' + '-----'*5)
def print_info1(*args): # *를 붙이지 않으면 2개 이상 시부터 오류
    print(args)

print_info1('name', 'age')


def print_info2(**kwargs): # **를 붙이지 않으면 키워드 인자 넣을 시 오류가 나옴
    print(kwargs)
    print(type(kwargs))

print_info2(name='eve', age=30)


def my_func(pos1, pos2, default_arg='default', *args, **kwargs):
    print(pos1, pos2, default_arg, args, kwargs)

my_func(1, 2, 3, 4, 5, 6, a='apple') # 1 2 3 (4, 5, 6) {'a': 'apple'}

my_func(1, 2) # 1 2 default () {}
# my_func(1)은 오류 나옴. 위치 인자는 반드시 적어야 해서.



print('재귀함수 팩토리얼' + '-----'*5)
# 재귀함수 팩토리얼
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) #120




print('global 키워드' + '-----'*5)
num = 0 # 전역 변수

def increment():
    global num # num를 전역 변수로 선언
    num += 1

print(num) # 0
increment()
print(num) # 1



print('언패킹' + '-----'*5)
packed_values = 1, 2, 3, 4, 5
a, b, c, d, e = packed_values
print(a, b, c, d, e)

# *을 활용
def my_fucntion(x, y, z):
    print(x, y, z)

"""def my_fucntion(*arges):
    print(arges)
    로 하면 결과가 튜플로 묶여서 나옴 ('a', 'j', 'p')
"""
names = ['a', 'j', 'p']
my_fucntion(*names) # a j p ## *이 없으면 에러.
my_dict = {'x':1, 'y':2, 'z':3}
my_fucntion(**my_dict) # 1 2 3



print('람다 표현식' + '-----'*5)
def addtion(x, y):
    return x + y

lambda x,y: x + y

#나이가 어린 순으로 정렬하기
studnets = [('김지민', 25), ('서준', 20), ('민우', 30)]
def get_Age(student):
    return student[1]

result = sorted(studnets, key=get_Age)
print(result)

result2 = sorted(studnets, key=lambda x: x[1])
print(result2)

print('모듈' + '-----'*5)
import math
print(math.pi)
print(math.sqrt(4))

from math import pi, sqrt
print(pi)
print(sqrt(4))

from math import sqrt as my_sqrt # 별칭을 사용함으로서 sqrt라는 동일 이름 함수가 있어도 공존 가능

import 사용자정의모듈my_math
print(사용자정의모듈my_math.add(10, 20))

from 사용자정의패키지my_package.math import my_math
from 사용자정의패키지my_package.statistics import tools

print(my_math.add(1, 2)) #3
print(tools.mod(1, 2)) #1



print('map함수와 split메서드' + '-----'*5)
numbers1 = '1 2 3'.split()
print(numbers1)
numbers2 = list(map(int, numbers1))
print(numbers2)


numbers = [1, 2, 3, 4, 5]

def square(x):
    return x **2

# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1) # [1, 4, 9, 16, 25]
# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2) # [1, 4, 9, 16, 25]



print('for-else문과 while-else문' + '-----'*5)
registed_ids = ['admin', 'user01', 'guest', 'user02']
id_to_check = 'guest' # 이미 리스트에 존재하는 아이디

for existing_id in registed_ids:
	if existing_id == id_to_check:
		print('이미 사용 중인 아이디입니다.')
		break # 중복 아이디를 찾았으므로 확인 절차 중단
else:
	# for 루프가 break로 중단되어서 이 부분은 실행 안 
	print('사용 가능한 아이디입니다.')


count = 1
while count <= 3:
    if count <= 0:
        break
    print(count)
    count += 1
else:
    print('break 안 걸리고 완료')


print('enumerate 함수, zip 함수' + '-----'*5)
respondents = ['은지', '정우', '소민', '태호']
answers = ['', '좋아요', '', '괜찮아요']

for i, response in enumerate(answers):
	if response == '':
		print(f"{respondents[i]} 미제출")

"""
은지 미제출
소민 미제출
"""

scores = [
	[10, 20, 30],
	[40, 50, 39],
	[20, 40, 50],
]

for score in zip(*scores):
	print(score)
	
"""
(10, 40, 20)
(20, 50, 40)
(30, 39, 50)
"""

print('list comprehension' + '-----'*5)
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)
print(squared_numbers) # [1, 4, 9, 16, 25]

squared_numbers2 = [num**2 for num in numbers]
print(squared_numbers2) # [1, 4, 9, 16, 25]

data1 = [[0] * (5) for _ in range(5)]
# for _ in range(5)에서 언더바(_)는 반복 변수를 실제로 안 쓸 때 관용적으로 쓰는 이름. "이 값은 필요 없고, 그냥 5번 반복만 하고 싶다"
print(data1) # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

print('리스트 생성하는 3가지 방법' + '-----'*5)
# loop
result1 = []
for i in range(10):
    result1.append(i)

# list comprehension
result2 = [i for i in range(10)]

# map
result3 = list(map(lambda x:x, range(10)))

print(result1, result2, result3)

text = 'heLLo, woRld!'
new_Text = text.swapcase().replace('l', 'z')
print(new_Text)

print('딕셔너리 매서드' + '-----'*5)
# D.keys()
person = {'name': 'Alice', 'age': 25}
print(person.keys())
print(list(person.keys()))
for item in person.keys():
    print(item)

# D.items()
for key, value in person.items():
    print(key, value)

# D.setdefault()
print(person.setdefault('country', 'KOREA'))
print(person)

# D.update()
person.update(age=100)
print(person)



print('defaultdict' + '-----'*5)
# 기존 기본 딕셔너리
text = 'banana'
counts = {}

for char in text:
    if char not in counts:
        counts[char] =0
    counts[char] += 1

print(counts)

# defaultdict 활용
from collections import defaultdict

text = 'banana'
counts = defaultdict(int) #숫자 세기
for char in text:
    counts[char] += 1

print(counts)

# defaultdict로 색깔별 과일 분류
from collections import defaultdict

fruits = [('red', 'apple'), ('yellow', 'banana'), ('red', 'cherry')]
fruit_by_color = defaultdict(list) # 그룹핑/리스트 모으기
for a, b in fruits:
    fruit_by_color[a].append(b)

print(fruit_by_color)
print(dict(fruit_by_color))

print('set 연산자' + '-----'*5)
set1 = {0, 1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)




print('클래스' + '-----'*5)
#인스턴스 매서드와 클래스 매서드
class Person:
    population = 0 # 클래스 변수. 모든 Person의 인스턴스가 공유

    def __init__(self, name): # 초기 설정
        self.name = name
        Person.increase_population()

    @classmethod
    def increase_population(cls):
        cls.population += 1

person1 = Person('Alice')
person2 = Person('Bella')

print(Person.population) #2

# 스태틱 메서드
class MathUtils:
    @staticmethod
    def add(a, b):
         return a + b

print(MathUtils.add(3, 5)) #8

# 은행 계좌 클래스 만들기
class BankAccount:
    interest_rate = 0.02

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액 부족!')

    @classmethod
    def set_interest_rate(cls, rate):
        cls.interest_rate = rate

    @staticmethod
    def is_positive(amount):
        return amount > 0 

alice_acc = BankAccount('Alice', 1000)

alice_acc.deposit(1000)
alice_acc.withraw(500)

print(alice_acc.balance)

BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)

print(BankAccount.is_positive(alice_acc.balance))


# 매직 메서드 __str__(self)
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'원의 반지름: {self.radius}'

c1 = Circle(1)
c2 = Circle(2)
print(c1)
print(c2)




print('다중 상속' + '-----'*5)
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'

class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'

class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'

class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'
    def cry(self):
        return '첫째가 응애'

baby1 = FirstChild('아가')
print(baby1.cry())
print(baby1.swim())
print(baby1.walk())
print(baby1.gene)



print('super() 함수' + '-----'*5)
# 단일 상속
class Person:
    def __init__(self, name, age, number, email):
        self.name = name
        self.age = age
        self.number = number
        self.emil = email

class Student(Person):
    def __init__(self, name, age, number, email, student_id):
        super().__init__(name, age, number, email) # self 매개변수는 안 적어도 됨. 부모 클래스에 있는 매개변수들을 가져오는 것.
        self.student_id =student_id


# 다중 상속
class ParentA:
    def __init__(self):
        self.value_a = 'ParentA'
    def show_value(self):
        print(f'Value from ParentA: {self.value_a}')

class ParentB:
    def __init__(self):
        self.value_b = 'ParentB'
    def show_value(self):
        print(f'Value from ParentB: {self.value_b}')

class Child(ParentA, ParentB):
    def __init__(self):
        super().__init__() # self 매개변수는 안 적어도 됨
        self.value_c = 'Child'
    def show_value(self):
        super().show_value()
        print(f'Value from Child: {self.value_c}')

child = Child()
child.show_value()

print(child.value_c)
print(child.value_a)



print('복수 예외처리' + '-----'*5)
try:
    x = int(input('숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:
    print('0으로 못나눔')
except ValueError:
    print('유효한 숫자가 아님')
else:
    print(f'결과: {y}')
finally:
    print('프로그램이 종료')

# 예외 객체
my_list = []
try:
    number = my_list[1]
except IndexError as error:
    print(f'{error}가 발생했습니다.')