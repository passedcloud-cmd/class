############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 파이썬 내장 함수 min 함수를 사용하지 않으면 추가 점수를 얻습니다.

def min_score(list_score):
    minimum_score = list_score[0]
    for i in range(len(list_score)):
        if list_score[i] < minimum_score:
            minimum_score = list_score[i]
    return minimum_score











# def min_score(scores):
#     min_number = scores[0]
#     for i in range(len(scores)):
#         # 기준을 하나 두고 for문으로 반복해서 비교?
#         if scores[i] < min_number:
#             min_number = scores[i]
#     return min_number

# 하나의 값을 기준으로 둠
# 리스트 내 요소를 한 번 돌면서 값을 비교한다
# 돌다가 기준값보다 작은 값이 나오면 그게 새로운 기준값이 됨
# 새로운 기준값과 나머지 요소를 비교하게 됨
# 가장 작은 값이 남음
            


    


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
print(min_score([100, 100])) 
print(min_score([2, 0, -2]))

