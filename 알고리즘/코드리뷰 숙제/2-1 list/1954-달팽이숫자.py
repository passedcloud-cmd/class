# ## 델타 이동

# import sys
# sys.stdin = open("1954-달팽이숫자.txt")

# T = int(input())

# # 방향키 설정: 우 하 좌 상
# # 왜나하면 예) 우우우 - 하하하 - 좌좌좌 - 상상 이런 식으로 움직일 거니까.
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]

# for tc in range(1, T + 1):
#     N = int(input()) # N은 행렬의 크기
#     # 크기가 N X N이고 0으로 채워진 행렬 만들기
#     arr = [[0] * N for _ in range(N)]

#     # 시작점 [0, 0]과 방향 0
#     r, c, direction = 0, 0, 0

#     for num in range(1, (N * N + 1)):
#         arr[r][c] = num
        
#         # 다음 row와 다음 column
#         nr = r + dr[direction]
#         nc = c + dc[direction]
        
#         if not ((0 <= nr < N) and (0 <= nc < N) and (arr[nr][nc] == 0)):
#             direction = (direction + 1) % 4 # 0, 1, 2, 3 반복 
#             nr = r + dr[direction]
#             nc = c + dc[direction]

#         r = nr
#         c = nc

#     print(f'#{tc}')
#     for row in arr:
#         print(*row)

############################################################
# 다시 풀어보기
import sys
sys.stdin = open('1954-달팽이숫자.txt')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 방향키 우하좌상
    dr = [0, 1 , 0, -1]
    dc = [1, 0, -1, 0]

    # 시작점과 방향 초기화
    r1, c1, direction = 0, 0, 0

    # 다음 이동
    nr = r1 + dr[direction]
    nc = c1 + dc[direction]

    # 행 고정 이동
    for r in range(N):
        for c in range(N):
            










##############################################################
## 테두리만 도는 방법

# import sys
# sys.stdin = open("1954-달팽이숫자.txt")

# T = int(input())

# for tc in range(1, T + 1):

#     N = int(input())

#     # 크기가 N X N이고 0으로 채워진 행렬 만들기
#     arr = [[0] * N for _ in range(N)]

#     # 구간별 출발 시작점, 도착점 
#     start, end = 0, N-1

#     # 초기값
#     num = 1

#     while start <= end:
#         # N이 홀수일 때 가운데 처리
#         if start == end :
#             arr[start][end] = num
#             break
#         # for문 4개로 위, 오른쪽, 아래, 왼쪽 
#         # 위쪽 테두리
#         for c in range(start, end):
#             arr[start][c] = num
#             num += 1
#         # 오른쪽 테두리
#         for r in range(start, end):
#             arr[r][end] = num
#             num += 1
#         # 아래쪽 테두리
#         for c in range(end, start, -1):
#             arr[end][c] = num
#             num += 1
#         #왼쪽 테두리
#         for r in range(end, start, -1):
#             arr[r][start] = num
#             num += 1

#         # 한 바퀴 돌았으니까 start와 end 각각 +1, -1
#         start += 1
#         end -= 1

#     print(f'#{tc}')
#     for row in arr:
#         print(*row)


# # 오답노트
# # for r in range(end, start, -1):
# # end숫자부터 시작해서 start + 1 까지 이동함. 



# 입력
# 2
# 3
# 4

# 출력
# #1
# 1 2 3
# 8 9 4
# 7 6 5
# #2
# 1 2 3 4
# 12 13 14 5
# 11 16 15 6
# 10 9 8 7