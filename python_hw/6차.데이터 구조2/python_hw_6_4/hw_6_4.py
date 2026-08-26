# 아래 함수를 수정하시오.
# 기존의 딕셔너리에 새로운 키-값 쌍을 인자로 받아야 함. 인자 추가.
def add_item_to_dict(dictionary, key, value):
    new_dict = dictionary.copy()
    new_dict.update({key:value})
    return new_dict


my_dict = {'name': 'Alice', 'age': 25}
result = add_item_to_dict(my_dict, 'country', 'USA')
print(result)
