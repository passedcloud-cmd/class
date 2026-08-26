# 아래 함수를 수정하시오.
def find_min_max(data):
    """주어진 리스트에서
    최솟값과 최댓값을 찾는 함수"""
    min_number = min(data)
    max_number = max(data)
    return (min_number, max_number)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)

# result 타입 확인
# print(type(result)) 