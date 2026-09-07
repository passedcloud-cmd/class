import sys
sys.stdin = open("1210_ladder1.txt")

def find_destination(input_arr, start_y):
    x = 0
    y = start_y

    if input_arr[x][y] == 1:
        while x < 99:
            # 좌측
            if 0 <= y - 1 and input_arr[x][y-1] == 1:
                while y - 1 >= 0 and input_arr[x][y-1] == 1:
                    y -= 1
            # 우측
            elif y + 1 < 100 and input_arr[x][y+1] == 1:
                while y + 1 < 100 and input_arr[x][y+1] == 1:
                    y += 1
            
            x += 1 #좌나 우로 이동했으면 무조건 아래로 내려가야 함. 그렇지 않으면 다시 좌우로 이동하면서 무한 루프에 빠짐

    if input_arr[x][y] == 2:
        return start_y

    elif input_arr[x][y] != 2:
        return -1

# 문제에 명시
T = 10

for test_case in range(1, T + 1):
    # test_case 번호 N
    N = int(input())

    # arr 만들기. 100 x 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    for row in range(100):
        result = find_destination(arr, row)
        if result != -1:
            break

    print(f'#{N} {result}')












# import sys
# sys.stdin = open("1210_ladder1.txt")
#
# def find_destination(input_arr, start_c):
#     """x = 0, y = start_y에서 출발하여 x = 99, y =2인 곳까지 내려가기"""
#     result = -1   # 미리 기본값 설정!
#
#     # 방향키 설정 좌, 우, 하
#     dr = [0, 0, 1]
#     dc = [-1, 1, 0]
#
#     # 시작점 초기화
#     r = 0
#     c = start_c
#
#     # 시작점 input_arr[0][start_c] == 1일 때만 시작한다는 조건
#     if input_arr[0][start_c] == 1:
#         # x = 99일 때 멈추기
#         while r < 99:
#             # 세 방향 좌, 우, 하 돌면서 나아갈 방향 모색
#             for i in range(3):
#                 # 다음 방향
#                 nr = r + dr[i]
#                 nc = c + dc[i]
#                 # 경계 체크
#                 if 0 <= nr < 100 and 0 <= nc < 100 and arr[nr][nc] == 1:
#                     # 기존 자리는 0으로 처리해서 되돌아가지 않도록 함
#                     arr[r][c] = 0
#                     r, c = nr, nc
#                     break # for i
#
#         # arr[99][c] == 2이면 시작점 c를 출력하고 break. 그렇지 않으면 -1 출력
#         if arr[99][c] == 2:
#             result = start_c
#
#     return result
#
# T = 10 # 문제에 명시
#
# for test_case in range(1, T + 1):
#     # test_case 번호 N
#     N = int(input())
#
#     # arr 만들기. 100 x 100
#     arr = [list(map(int, input().split())) for _ in range(100)]
#
#     # 0 <= c < 100 반복
#     for n in range(100):
#         y_pose = find_destination(arr, n)
#         if y_pose != - 1:
#             answer_c = y_pose
#             break
#
#     print(answer_c)


        
    


                



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

