# min_max_practice 문제
"""
[문제] 내장 함수 min(), max()를 사용하지 않고
       리스트에서 최댓값과 최솟값을 구하시오.

조건
  1. min(), max(), sorted(), sort() 사용 금지
  2. 반복문(for)과 비교 연산자(<, >)만 사용

예시
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  최솟값: 1
  최댓값: 9
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
minimal_number = numbers[0]
maximum_number = numbers[0]

for i in numbers:
    if i < minimal_number:
        minimal_number = i
    if i > maximum_number:
        maximum_number = i

print(f'최솟값: {minimal_number}\n최댓값: {maximum_number}')







# 1번 문제

############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않으면 추가 점수를 얻습니다.
def min_score(list_score):
    minimal_score = list_score[0] 
    for i in list_score:
        if i < minimal_score:
            minimal_score = i
    result = minimal_score
    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(min_score([30, 60, 90, 70])) # 30
print(min_score([0, 10, 20, 30, 40, 50])) # 0
print(min_score([50, 70, 50, 45, 80, 80])) # 45
#####################################################

# 테스트 코드는 이곳에
print(min_score([100, 100])) # 110
print(min_score([2, 0, -2])) # -2







print('-----' * 5)
# 2번 문제
def under_60(list_score):
    number_of_under60 = 0
    for i in list_score:
        if i < 60:
            number_of_under60 += 1
    result = number_of_under60
    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(under_60([30, 60, 90, 70])) # 1
print(under_60([0, 10, 20, 30, 40, 50])) # 6
print(under_60([50, 70, 50, 45, 80, 80])) # 3
#####################################################







print('-----' * 5)
# 3번 문제
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(dir_data):
    list(dir_data.values())
    for i in list(dir_data.values()):
        if bool(i) is False:
            result = False
            break
        else:
            result = True
    return result

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################






print('-----' * 5)
# 4번 문제
############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))
def is_id_valid(data_dir):
    try:
        int(data_dir['id'][-1])
        result = True
    except ValueError:
        result = False
    return result

def is_id_valid2(data_dir):
    last_chr = data_dir['id'][-1]
    if last_chr.isdecimal() is True:
        result = True
    else:
        result = False
    return result


#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True
print(is_id_valid2(user_data1)) # True

user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
print(is_id_valid2(user_data2)) # False
#####################################################
