# 아래 함수를 수정하시오.

# set으로 변경하면 저절로 중복된 요소가 사라짐
def remove_duplicates_to_set(list):
    a = set(list)
    return a


result = remove_duplicates_to_set([1, 2, 2, 3, 4, 4, 5])
print(result)
