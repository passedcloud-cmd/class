number_of_people = 0

def increase_user(): # 실습 1에서 작성한 함수
    global number_of_people # 전역 변수로 선언
    number_of_people += 1

def decrease_book(number): # 실습 3에서 작성한 함수
    """한 번에 대여하는 책의 수를 정수로 넘겨 받음
    넘겨받은 값만큼 number_of_book의 수를 감소
    현재 남은 책의 수를 출력
    """
    global number_of_book # 전역 변수로 다시 선언이 꼭 필요한가 봄
    number_of_book = number_of_book - number
    print("남은 책의 수 : " + str(number_of_book))
    

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']





# 실습 2에서 작성한 함수를 활용
def create_user(name, age, address): 
    """increase_user 함수를 호출하여 number_of_people값이 증가
    name, age, address를 인자로 받아 user_info에 키값에 값을 할당
    완성된 user_info 딕셔너리를 반환"""
    increase_user() # 가입된 유저 수 1명 증가
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    return user_info




many_user = [{'이름' : '김시습', '나이' : 20}, {'이름' : '허균', '나이' : 16}, {'이름' : '남영로', '나이' : 52}, {'이름' : '임제', '나이' : 36}, {'이름' : '박지원', '나이' : 60}]

number_of_book = 100

# def rental_book(info):
#     """info 인자는 {'고객 이름' : 고객 나이} 형태의 딕셔너리
#     info 딕셔너리에서 고객의 이름과 나이 추출
#     추출한 나이를 10으로 나눈 몫으로 대여할 책의 수를 계산
#     decrease_book 함수를 호출
#     대여 완료 메시지 출력"""
#     # name = info.keys() # 키만 추출하는 .keys()
#     # age = info.values() # 밸류만 추출하는 .values()
#     number = 53 // 10
#     decrease_book(number)
#     print(str(info.keys()) + "님이" + str(number) + "권의 책을 대여하였습니다.")
# # dict_values는 나누기를 할 수 없고 int 함수로 감쌀 수도 없음

# def rental_book(info):
#     """info 인자는 {'고객 이름' : 고객 나이} 형태의 딕셔너리
#     info 딕셔너리에서 고객의 이름과 나이 추출
#     추출한 나이를 10으로 나눈 몫으로 대여할 책의 수를 계산
#     decrease_book 함수를 호출
#     대여 완료 메시지 출력"""
#     name = list(info.keys()) # 키만 추출하는 .keys()
#     age = list(info.values()) # 밸류만 추출하는 .values()
#     for i in name :
#         print(str(i) + "님 환영합니다!")
#     number = age // 10
#     for i in age : 
#         decrease_book(number)
#     print(str(info.keys()) + "님이" + str(number) + "권의 책을 대여하였습니다.")
# # dict_values는 나누기를 할 수 없고 int 함수로 감쌀 수도 없음

def rental_book(info):
    for name, age in info.items():
        # name에는 key(이름), age에는 value(나이)가 들어감
        number = age // 10 
        decrease_book(number)
        print(f"{name}님이 {number}권의 책을 대여하였습니다.")

# rental_book({'김시습': 20}) # 결과값 확인





# 새로운 딕셔너리 틀 만들기
# print(many_user[0]['이름'])
# print(many_user[0]['나이'])
# user_info.append({many_user[0]['이름'] : many_user[0]['나이']}) 
# print(user_info)

user_info = []

# for문으로 user_info 리스트 채우기
for i in many_user : 
    user_info.append({i['이름'] : i['나이']})  # i에 딕셔너리 형태가 이미 들어가 있음!
# print(user_info) # 결과값 확인




# 전체 로직 실행

for i in user_info:
    for name, age in i.items():
        print(f"{name}님 환영합니다!")

for i in user_info :
    rental_book(i)
