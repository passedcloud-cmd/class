# # 아래 함수를 수정하시오.
# def check_number():
#     try: 
#         x = int(input("숫자를 입력하세요: "))
#         if x > 0:
#             print("양수입니다.")
#         elif x == 0:
#             print("0입니다.")
#         elif x < 0:
#             print("음수입니다.")
#     except ValueError:
#         print('잘못된 입력입니다.')

# check_number()

# while문을 사용해서 계속 반복해보자


def check_number():
    while True:
        try: 
            x = int(input("숫자를 입력하세요: "))
            if x > 0:
                print("양수입니다.")
            elif x == 0:
                print("0입니다.")
            elif x < 0:
                print("음수입니다.")
        except ValueError:
            print('잘못된 입력입니다.')
            break

check_number()