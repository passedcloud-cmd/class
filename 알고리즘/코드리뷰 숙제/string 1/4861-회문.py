import sys
sys.stdin = open("4861-회문.txt")
T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # N x N 배열 만들기
    arr = [input() for _ in range(N)]

    # 테스트 케이스마다 result 초기화
    result = 0

    # 가로 기준으로 회문 찾기
    for r in range(N):
        for c in range(N - M + 1):
            word = arr[r][c : c + N]
            if word == word[::-1]:
                result = word
                break
        if result != 0:
            break

    # 가로 기준으로 못 찾았으면 세로 기준으로 회문 찾기
    if result == 0:
        for c in range(N):
            for r in range(N - M + 1):
                column_word_list = []
                for i in range(M):
                    column_word_list.append(arr[r + i][c])
                column_word = "".join(column_word_list)
                if column_word == column_word[::-1]:
                    result = column_word
                    break #for r
            if result != 0:
                break #for c

    print(f'#{test_case} {result}')

# 오답노트
# word = arr[r][c : c + N] 로 N짜리 문자열 뽑기

# 문자열 만드는 법 1
# column_word_list = []
# for i in range(M):
#     column_word_list.append(arr[r + i][c])
# column_word = "".join(column_word_list)

# 문자열 만드는 법 2
# vertical_word = ""
# for i in range(M):
#     vertical_word += grid[r + i][c]

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