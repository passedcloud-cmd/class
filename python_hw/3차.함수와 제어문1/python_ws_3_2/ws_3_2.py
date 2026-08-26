number_of_people = 0 # 전역 변수

def increase_user(): # 실습 1에서 작성한 함수
    global number_of_people # 전역 변수로 선언
    number_of_people += 1


def create_user(name, age, address):
    """increase_user 함수를 호출하여 number_of_people값이 증가
    name, age, address를 인자로 받아 user_info에 키값에 값을 할당
    완성된 user_info 딕셔너리를 반환"""
    print("현재 가입 된 유저 수 : " + str(number_of_people))
    increase_user() # 가입된 유저 수 1명 증가
    user_info = {'name': name, 'age': age, 'address': address}
    print(f'{name}님 환영합니다!')
    print(user_info)
    print("현재 가입 된 유저 수 : " + str(number_of_people))
    return user_info

create_user('홍길동', 30 ,'서울')