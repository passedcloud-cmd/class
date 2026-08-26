############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.


def is_user_data_valid(dir_data):
    values_list = list(dir_data.values())
    for i in range(len(values_list)):
        if values_list[i] == "":
            result = False
            break
        else:
            result = True
    return result









































# def is_user_data_valid(user_data):
#     # key의 value값이 하나라도 비어있으면 False를 반환합니다
#     # 딕셔너리의 value값을 가져오자
#     list_data = list(user_data.values())
#     # print(list_data)
#     for i in range(len(list_data)):
#         if list_data[i] == "":
#             result = False
#             break
#         else:
#             result = True
#     return result


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

user_data = {'a': 'apple', 'b': '    '}
print(is_user_data_valid(user_data))

