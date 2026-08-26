############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def find_common(list_a, list_b):
    # set으로 만들어서 교집합
    set_a = set(list_a)
    set_b = set(list_b)
    common_set = set_a & set_b
    common_list = list(common_set)
    # result_list.sort()
    # return result_list
    # 아 list_a 기준으로 순서대로 반환해야함!!!!
    result_list = []
    for i in list_a:
        if i in common_list:
            result_list.append(i)
    return result_list

    
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_common([1, 2, 3, 4, 5], [2, 4, 6, 4]))                      # [2, 4]
print(find_common(['apple', 'banana', 'cherry'], ['cherry', 'apple', 'grape']))  # ['apple', 'cherry']
#####################################################