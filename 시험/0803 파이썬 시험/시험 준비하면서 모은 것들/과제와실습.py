# 1차.파이썬 기초문법1은 쉬워서 스킵

# 2차.파이썬 기초문법2: 깊은 복사와 indexing 접근Lv5
# 깊은 복사 방법
'''
import copy

backup_catalog = copy.deepcopy(catalog)

catalog[3][1] = '내 삶의 변화'
→ backup_catalog만 변함
'''


print('=====' * 5)
# 3차.함수와 제어문1: 함수 활용하기Lv2
pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# global에 정의된 pro_num 변수의 값에 1을 더한 값이란
# global 키워드로 변수의 스코프를 전역 범위로 지정하라는 뜻

def create_data(subject, day, title = None):
    global pro_num
    pro_num = pro_num + 1
    data = {'과목': subject, '일차': day, '제목': title, '문제 번호': pro_num}

    return data

result_1 = create_data('python', 3)
result_2 = create_data(subject = str('web'), day = int(1), title = 'web 연습하기')

# global_data변수를 언패킹해서 인자로 전달하기
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)


print('-----' * 5)
# 재귀 함수 만들기Lv3
def recur_example(number):
    '''
        함수(2) 실행
            number에 2 할당
            if 2 == 1 조건문 만족하지 않음
            else문 2 + 함수(2-1) 
                결과를 알기위해서는 함수(2-1)의 실행 결과가 필요

                함수(2-1) 실행
                    number에 1 할당
                    if 1 == 1 조건문 만족하므로 1 반환
            
            else문의 2 + 함수(2-1)중, 함수(2-1)의 실행결과가 1임을 알게되었음 
            2 + 1 반환
        결과 : 3  
    '''
    if number == 1:
        return 1
    else:
        return number + recur_example(number - 1)
result_1 = recur_example(5)
print(result_1) # 5 + 4 + 3 + 2 + 1 = 15

# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
# def power(base, exponent):
#     '''
#         함수(2, 3) 실행
#             base에 2 할당, exponent에 3할당
#             지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

#             아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
#                 2 * 함수(2, 3-1)

#             모든 상황을 반복하는 과정
#             2 * (2 * (2 * 1))  
#             결과 : 8
#     '''
#     if :
#         return 
#     else:
        
#         return
# result_2 = power(2, 3)
# print(result_2) # 2 * 2 * 2 * 1 = 8

# # 모든 자릿수 더하기 함수
# def sum_of_digits(number):
#     '''
#         함수(321) 실행
#         number가 10 미만인 경우, number 반환

#         아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
#             number를 10으로 나누 나머지 + 함수(number를 10으로 나눈 몫)
#             1 + (321 // 10)

#         모든 상황을 반복하는 과정
#         1 + 2 + 3
#         결과 : 6
#     '''
#     if :
#         return 
#     else:
#         return 
# result_3 = sum_of_digits(321)
# print(result_3) # 1 + 2 + 3 = 6








# 거듭 제곱 재귀 함수
# base = 밑, exponent = 지수
# base의 exponent승 == 2의 3승
def power(base, exponent):
    '''
        함수(2, 3) 실행
            base에 2 할당, exponent에 3할당
            지수가 0이 된 경우, 1을 반환 | 2의 0승은 1

            아닌경우, 지수가 0이 될 때까지 [exponent - 1] 을 다시 지수에 할당하여 함수 호출
                2 * 함수(2, 3-1)

            모든 상황을 반복하는 과정
            2 * (2 * (2 * 1))  
            결과 : 8
    '''
    if exponent == 0:
        return 1
    else :
        return base * power(base, exponent - 1)
    
# 1) 2 * power(2, 2)
# 2) 2 * 2 * power(2, 1)
# 3) 2 * 2 * 2 * power(2, 0)이 됨
# 4) power(2, 0) = 1 이므로 결국 2 * 2 * 2 * 1 = 8

result_2 = power(2, 3)
print(result_2) # 2 * 2 * 2 * 1 = 8



# 모든 자릿수 더하기 함수
def sum_of_digits(number):
    '''
        함수(321) 실행
        number가 10 미만인 경우, number 반환

        아닌경우, number가 10 미만이 될 때까지, number를 10으로 나눈 몫을 다시 number에 할당하여 함수 호출
            number를 10으로 나눈 나머지 + 함수(number를 10으로 나눈 몫)
            1 + (321 // 10)

        모든 상황을 반복하는 과정
        1 + 2 + 3
        결과 : 6
    '''
    if number < 10 :
        return number
    else:
        return (number % 10) + sum_of_digits(number // 10)

# 321을 넣으면
# 1) 나머지 1이 나오고 몫이 32가 나옴. 1은 더하고 32는 다시 돌려야함
# 2) 두 번째 돌리면 몫이 3 나오고 나머지 2가 나옴
# 3) 2는 10 미만이므로 끝임.
# 4) 결국 1 + 2 + 3이 됨

result_3 = sum_of_digits(321)
print(result_3) # 1 + 2 + 3 = 6

