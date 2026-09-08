# # 위에서 아래로 
# import sys
# sys.stdin = open('1210_ladder1.txt')
# T = 10 # 문제에 주어짐
# for test_case in range(1, T + 1):
#     # N은 test case 번호
#     N = int(input())
#     # ladder 만들기
#     ladder = [list(map(int, input().split())) for _ in range(100)]

#     # x=0 row에서 c를 0~99까지 훑고
#     for c in range(100):
#         # 시작점 r, c좌표
#         start_c = c
#         r = 0

#         # ladder[0][c] == 1인 지점이 있으면 시작
#         if ladder[0][c] == 1:

#             # x =99까지 아래로 이동
#             while r < 99: 
#                 #좌측에 길이 있으면 왼쪽이 경계선이거나 0일 때까지 -1씩(왼쪽으로) 이동
#                 if 0 <= c - 1 < 100 and ladder[r][c - 1] == 1:
#                     while 0 <= c - 1 < 100 and ladder[r][c - 1] == 1:
#                         c -= 1

#                 #우측에 길이 있으면 오른쪽이 경계선이거나 0일 때까지 +1씩(오른쪽으로) 이동
#                 elif 0 <= c + 1 < 100 and ladder[r][c + 1] == 1:
#                     while 0 <= c + 1 < 100 and ladder[r][c + 1] == 1:
#                         c += 1

#                 #좌측이나 우측으로 갔든 안 갔든 아래쪽으로 한 칸씩 이동
#                 r += 1

#         # 2인 지점을 찾았으면 break for c
#         if ladder[r][c] == 2:
#             result = start_c
#             break # for c

#         else:
#             result = -1

#     print(f'#{N} {result}')

    

# # 아래에서 위로
# import sys
# sys.stdin = open('1210_ladder1.txt')
# T = 10 # 문제에 주어짐
# for test_case in range(1, T + 1):
#     # N은 test case 번호
#     N = int(input())
#     # ladder 만들기
#     ladder = [list(map(int, input().split())) for _ in range(100)]

    
#     # ladder[99][c] = 2인 좌표를 찾기
#     # c를 0부터 99까지 훑기
#     for c in range(100):
#         if ladder[99][c] == 2:
#             # 시작점 찾음
#             r = 99
#             c = c
#             # 시작점을 찾았으니 break for c
#             break #for c

#     # ladder[99][end_c]부터 위로 올라가야 함
#     # r = 0까지 이동
#     while r > 0 :
#         # 왼쪽에 길이 있는 경우
#         if 0 <= c - 1 < 100 and ladder[r][c - 1] == 1:
#             while 0 <= c - 1 < 100 and ladder[r][c - 1] == 1:
#                 c -= 1

#         # 오른쪽에 길이 있는 경우
#         elif 0 <= c + 1 < 100 and ladder[r][c + 1] == 1:
#             while 0 <= c + 1 < 100 and ladder[r][c + 1] == 1:
#                 c += 1

#         # 왼쪽으로 갔든 안 갔든 위로 한 칸 이동
#         r -= 1

#     print(f'#{test_case} {c}')


# 위에서 아래로, 델타 
import sys
sys.stdin = open("1210_ladder1.txt")
T = 10 # 문제에 명시

# 방향키 좌우상
dr = [0, 0, -1]
dc = [-1, 1, 0]

for test_case in range(1, T + 1):
    # N은 test_case 번호
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # end_c 찾기. 
    for c in range (100):
        if ladder[99][c] == 2:
            # 도착점
            r = 99
            c = c
            break #for c

    # 좌,우,상 돌면서 1인 지점으로 나아가기
    # r = 0일 때까지 계속 이동
    while r > 0:
        # 다음으로 이동할 nr, nc 구하기
        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]

            # 경계와 ladder[nr][nc] 값 체크
            if 0 <= nr < 100 and 0 <= nc < 100 and ladder[nr][nc] == 1:
                # 이전 길로 가지 않게 걸어온 길은 0으로 처리
                ladder[r][c] = 0
                r = nr
                c = nc

    print(f'#{N} {c}')
            

    








# 오답노트
# return 값은 start_y 아니면 -1이므로 result == 2 라고 하면 안됨

# 출력
#1 67
#2 45
#3 39
#4 24
#5 91
#6 93
#7 90
#8 4
#9 99
#10 35

