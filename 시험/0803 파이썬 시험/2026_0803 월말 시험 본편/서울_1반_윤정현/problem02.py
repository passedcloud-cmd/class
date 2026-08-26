############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 제한 내장 함수:  len
# 기본 점수 (9점): 제한 내장 함수를 사용하여 해결
# 가산점(+3점): 제한 내장 함수 없이 직접 구현 (총 12점)

def count_long_names(names, min_length):
    # for문으로 요소 순회
    count_min_lenght_name = 0
    for name in names:
        # for 문으로 각 요소들 길이 구하기
        
        len_of_name = 0
        for i in name:
            len_of_name += 1

        # 이름들 길이가 min_lenght보다 긴지 확인
        if len_of_name >= min_length:
            count_min_lenght_name += 1

    return count_min_lenght_name

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(count_long_names(['kim', 'developer', 'ssafy', 'a'], 5))  # 2 ('developer', 'ssafy')
print(count_long_names(['a', 'bb', 'ccc'], 5))                  # 0
#####################################################