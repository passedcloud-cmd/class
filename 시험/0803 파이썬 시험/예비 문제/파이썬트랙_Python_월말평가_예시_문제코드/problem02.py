############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def under_60(list_score):
    # 리스트 요소를 for문으로 돌면서 60보다 작은 것을 찾아야함
    # 바깥에 score_count = 0으로 시작
    score_count = 0
    for i in range(len(list_score)):
        if list_score[i] < 60:
            score_count += 1
    return score_count




































# def under_60(scores):
#     # count_under_60 변수를 만들고 0을 할당
#     # for문으로 돌면서 < 60 을 만족하면 count_under_60이 1씩 증가하도록 하기
#     global count_under_60
#     count_under_60 = 0
#     for i in range(len(scores)):
#         if scores[i] < 60:
#             count_under_60 += 1
#     return count_under_60


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(under_60([30, 60, 90, 70])) # 1
print(under_60([0, 10, 20, 30, 40, 50])) # 6
print(under_60([50, 70, 50, 45, 80, 80])) # 3
#####################################################
