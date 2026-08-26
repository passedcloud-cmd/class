# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    result = set1 | set2
    return result

    
def union_multiple_sets(*sets):
    # if문으로 셋이 2개 이하일 때 안내문 출력
    # 순환문으로 넘겨받은 셋을 모두 합해야 함.
    pass


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
