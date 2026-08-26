# 아래에 코드를 작성하시오.
# Myth 클래스를 정의
# Myth의 인스턴스 수를 기록할 수 있는 클래스 변수 type_of_myth를 정의하고, 0을 할당
# 생성자 매서드 정의
    # 신화의 이름을 인자로 받음
    # 각 인스턴스는 고유한 이름을 담을 수 있는 name 변수를 가지고, 인자로 넘겨받은 이름을 할당 받음
    # 인스턴스가 생성될 때마다 type_of_myth가 1 증가

class Myth:
    type_of_myth = 0

    def __init__(self, name):
        self.name = name
        Myth.number_of_myth()

    def name_of_myth(self):
        print(self.name)

    @classmethod
    def number_of_myth(cls):
        cls.type_of_myth += 1

    @staticmethod
    def description():
        print("신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.")

myth1 = Myth('dangun')
myth1.name_of_myth()
myth2 = Myth('greek & rome')
myth2.name_of_myth()
print("현재까지 생성된 신화 수: " + str(Myth.type_of_myth))
Myth.description()

# 신화에 대한 설명을 출력하는 description 스태틱 메서드 정의

# 2개 이상의 인스턴스를 생성하고, 각 인스턴스의 name을 출력
# Myth 클래스의 type_of_myth를 출력한다
# description 스태틱 메서드를 호출
