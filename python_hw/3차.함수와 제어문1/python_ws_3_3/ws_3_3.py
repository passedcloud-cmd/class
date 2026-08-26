number_of_book = 100 # 전역 변수

def decrease_book(number):
    """한 번에 대여하는 책의 수를 정수로 넘겨 받음
    넘겨받은 값만큼 number_of_book의 수를 감소
    현재 남은 책의 수를 출력
    """
    global number_of_book # 전역 변수로 다시 선언이 꼭 필요한가 봄
    number_of_book = number_of_book - number
    print("남은 책의 수 : " + str(number_of_book))
    
def rental_book(name, number):
    """rental_book 함수가 실행 될 때, decrease_book 함수 호출
    """
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')


rental_book('홍길동', 3)