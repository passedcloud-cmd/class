############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_id_valid(data_dir):
    last_chr = data_dir['id'][-1]
    try: int(last_chr)
    except ValueError:
        result = False
    else:
        result = True
    return result



















# def is_id_valid(user_data):
#     # 딕셔너리의 id키의 value 값만 꺼내면 됨
#     # value값을 str로 변환하고 [-1]인덱싱으로 마지막 자리만 가져오기
#     # 마지막 자리를 int로 변환했을 때 잘못된 인자라고 에러가 안 뜨면 True
#     try: int(str(user_data['id'])[-1])
#     except ValueError:
#         result = False
#     else:
#         result = True
#     return result


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################


user_data3 = {
    'id': 'jungssafy5-1h',
    'password': '1q2w3e4r1',
}
print(is_id_valid(user_data3))