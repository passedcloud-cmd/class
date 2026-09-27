# 문자열 만드는 법 1
# column_word_list = []
# for i in range(M):
#     column_word_list.append(arr[r + i][c])
# column_word = "".join(column_word_list)

# 문자열 만드는 법 2
# vertical_word = ""
# for i in range(M):
#     vertical_word += grid[r + i][c]

# list(GOFFAKWFSM)를 하면
# ['G', 'O', 'F', 'F', 'A', 'K', 'W', 'F', 'S', 'M'] 됨



# #######################
# #### for 문으로 직접 탐색
# #####################
# import sys
# sys.stdin = open("4861-회문.txt")
# T = int(input())

# for test_case in range(1, T+1):
#     # N은 글자판 크기
#     # M은 찾아야하는 회문의 길이
#     N, M = map(int, input().split())
#     # 글자판은 NxN크기
#     arr = [list(input()) for _ in range(N)]

#     # # arr 확인용 출력
#     # for i in range(N):
#     #     print(arr[i])

#     found = False # 정답 찾았는지 안 찾았는지 확인용
#     result = None
#     # 가로 순회
#     for r in range(N):
#         for c in range(N-M+1):
#             # M 크기 짜리 tmp_txt
#             tmp_txt = arr[r][c : c+M]
#             # 그 텍스트를 거꾸로 뒤집기
#             tmp_txt_reverse = tmp_txt[::-1]

#             # tm=_txt가 뒤집어도 같다면 정답 찾은 것
#             if tmp_txt == tmp_txt_reverse:
#                 result = tmp_txt
#                 found = True # 정답 찾음
#                 break # for c 반복문 종료

#         if found: # 정답을 찾았으면 
#             break # for r 반복문 종료

#     # 세로 순회
#     if not found: # 정답 못 찾았으면 진행
#         for c in range(N):
#             for r in range(N-M+1):
#                 # M 크기 짜리 tmp_txt 만들기
#                 tmp_txt = []
#                 for i in range(M):
#                     tmp_txt.append(arr[r+i][c])

#                 # tmp_txt가 뒤집어도 같다면
#                 tmp_txt_reverse = tmp_txt[::-1]
#                 if tmp_txt == tmp_txt_reverse:
#                     result = tmp_txt
#                     found = True # 정답 찾음
#                     break # for r 반복문 종료

#             if found: # 정답 찾았으면
#                 break # for c 반복문 종료

#     print(f'#{test_case} {"".join(result)}')
    





#######################
#### 전치 행렬 사용
#####################
# zip(*arr) 아래와 같은 의미.
# zip(['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'])

# zip은 결과를 튜플로 엮어서 줌. 튜플도 슬라이싱과 인덱싱 가능.
# transposed_arr = list(zip(*arr))
# [('A', 'D', 'G'),
#  ('B', 'E', 'H'),
#  ('C', 'F', 'I')]

import sys
sys.stdin = open("4861-회문.txt")
T = int(input())

for test_case in range(1, T+1):
    # N은 글자판 크기
    # M은 찾아야하는 회문의 길이
    N, M = map(int, input().split())
    # 글자판은 NxN크기
    arr = [list(input()) for _ in range(N)]

    # # arr 확인용
    # for row in arr:
    #     print(row)

    result = None
    found = False
    # 가로 수색
    for r in range(N):
        for c in range(N-M+1):
            tmp_txt = arr[r][c:c+M]
            tmp_txt_reverse = tmp_txt[::-1]
            if tmp_txt == tmp_txt_reverse:
                result = tmp_txt
                found = True
                break
        if found:
            break

    # 세로 수색
    if not found:
        transposed_arr = list(zip(*arr))

        for r in range(N):
            for c in range(N-M+1):
                tmp_txt = transposed_arr[r][c: c+M]
                tmp_txt_reverse = tmp_txt[::-1]
                if tmp_txt == tmp_txt_reverse:
                    result = tmp_txt
                    found = True
                    break
            if found:
                break

    print(f'#{test_case} {"".join(result)}')







# 오답노트
# 문제의 원인: list(input().split())
# "GOFFAKWFSM".split()을 하면 이렇게 됩니다:
# ['GOFFAKWFSM']   # 통째로 원소 1개짜리 리스트!
# (원소가 1개라 뒤집어도 똑같음!)
# 리스트 안에 원소가 딱 1개밖에 없으면, 그 리스트를 거꾸로 뒤집어도 순서가 바뀔 게 없으니 항상 자기 자신과 같아지는 거예요. 문자열 내용이 회문이든 아니든 상관없이요!

# 입력
# 3
# 10 10
# GOFFAKWFSM
# OYECRSLDLQ
# UJAJQVSYYC
# JAEZNNZEAJ
# WJAKCGSGCF
# QKUDGATDQL
# OKGPFPYRKQ
# TDCXBMQTIO
# UNADRPNETZ
# ZATWDEKDQF
# 10 10
# WPMACSIBIK
# STWASDCOBQ
# AMOUENCSOG
# XTIIGBLRCZ
# WXVSWXYYVU
# CJVAHRZZEM
# NDIEBIIMTX
# UOOGPQCBIW
# OWWATKUEUY
# FTMERSSANL
# 20 13
# ECFQBKSYBBOSZQSFBXKI
# VBOAIDLYEXYMNGLLIOPP
# AIZMTVJBZAWSJEIGAKWB
# CABLQKMRFNBINNZSOGNT
# NQLMHYUMBOCSZWIOBINM
# QJZQPSOMNQELBPLVXNRN
# RHMDWPBHDAMWROUFTPYH
# FNERUGIFZNLJSSATGFHF
# TUIAXPMHFKDLQLNYQBPW
# OPIRADJURRDLTDKZGOGA
# JHYXHBQTLMMHOOOHMMLT
# XXCNJGTXXKUCVOUYNXZR
# RMWTQQFHZUIGCJBASNOX
# CVODFKWMJSGMFTCSLLWO
# EJISQCXLNQHEIXXZSGKG
# KGVFJLNNBTVXJLFXPOZA
# YUNDJDSSOPRVSLLHGKGZ
# OZVTWRYWRFIAIPEYRFFG
# ERAPUWPSHHKSWCTBAPXR
# FIKQJTQDYLGMMWMEGRUZ
#
# 출력
# #1 JAEZNNZEAJ
# #2 MWOIVVIOWM
# #3 TLMMHOOOHMMLT