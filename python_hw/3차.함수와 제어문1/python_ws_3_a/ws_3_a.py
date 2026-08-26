def my_multi(number_1, number_2):
    """두 인자를 곱하는 함수입니다
    my_multi(2, 3) 결과 : 6
    """
    return number_1 * number_2

result_1 = my_multi(2, 3)

print(result_1)

# my_multi(2, 3) 결과 : 6
# 함수를 수정하고 호출 결과를 result_1 변수에 할당하여 출력하시오.


# def is_negative(number):
#     """전달한 인자가 0이하면 True
#     그렇지 않으면 False를 return합니다
#     if문을 사용
#     """
#     if number <= 0 :
#         return True
#     else :
#         return False
    

def is_negative(number):
    """전달한 인자가 0이하면 True
    그렇지 않으면 False를 return
    """
    return bool(number<=0)

result_2 = is_negative(3)

print(result_2)

# is_negative(3) 결과 : False
# 함수를 수정하고 호출 결과를 result_2 변수에 할당하여 출력하시오.


def default_arg_func(default='기본 값'):
    """인자를 전달하지 않으면
    '기본 값' 텍스트가 출력됩니다
    """
    return default

result_3 = default_arg_func()
result_4 = default_arg_func('다른 값')

print(result_3)
print(result_4)