# ########################
# ### BFS_Queue
# ##########################
# import sys
# sys.stdin = open("27816_섬 찾기.txt")

# N, M = map(int, input().split())
# map = [list(input()) for _ in range(N)]

# # # 섬 확인용
# # for row in map:
# #     print(row)

# # 방향키 상 하 좌 우 좌상 우상 좌하 우하
# dr = [-1, 1, 0, 0, -1, -1, 1, 1]
# dc = [0, 0, -1, 1, -1, 1, -1, 1]

# visited = [[False] * M for _ in range(N)]

# # bfs로 섬을 방문체크 하기
# from collections import deque
# def bfs_queue(start_r, start_c, direction):

#     queue = deque()
#     queue.append([start_r, start_c])
#     visited[start_r][start_c]= True

#     while queue:
#         r, c = queue.popleft()

#         # 주변 땅도 확인
#         for i in range(direction):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             # 경계체크
#             if 0 <= nr < N and 0 <= nc < M:
#                 # 땅이고 방문한 적이 없다면
#                 if map[nr][nc] == '1' and not visited[nr][nc]:
#                     #큐에 넣기
#                     visited[nr][nc] = True
#                     queue.append([nr, nc])

# # 완전 탐색
# cnt = 0
# for r in range(M):
#     for c in range(N):
#         if map[r][c] == '1' and not visited[r][c]:
#             cnt +=1 
#             # 해당 섬 방문 체크
#             bfs_queue(r, c, 8)

# print(cnt)

# # 오답노트
# # 결과가 0인 핵심 원인은 글자 '1'과 숫자 1을 비교하고 있어서 계속 if map[r][c] == 1가 False로 나옴
# # map = [list(input()) for _ in range(N)]로 하면 리스트 내부 요소들이 문자열




# ########################
# ### DFS_stack
# ##########################
# import sys
# sys.stdin = open("27816_섬 찾기.txt")

# N, M = map(int, input().split())
# map = [list(map(int, input())) for _ in range(N)]

# # # 섬 확인용
# # for row in map:
# #     print(row)

# # 방향키 상 하 좌 우 좌상 우상 좌하 우하
# dr = [-1, 1, 0, 0, -1, -1, 1, 1]
# dc = [0, 0, -1, 1, -1, 1, -1, 1]

# visited = [[False] * M for _ in range(N)]

# # dfs_스택 함수 만들기
# def dfs_stack(start_r, start_c, direction):
#     stack = [(start_r, start_c)]
#     visited[start_r][start_c] = True

#     while stack:
#         r, c = stack.pop()

#         if map[r][c] == 1 and not visited[r][c]:
#             visited[r][c] = True

#         for i in range(direction):
#             nr = r + dr[i]
#             nc = c + dc[i]

#             if 0<=nr<N and 0<=nc<M:
#                 if map[nr][nc] == 1 and not visited[nr][nc]:
#                     stack.append((nr,nc))

# cnt = 0
# for r in range(N):
#     for c in range(M):
#         if map[r][c] == 1 and not visited[r][c]:
#             cnt += 1
#             dfs_stack(r, c, 8)

# print(cnt)




########################
### DFS_재귀
##########################
import sys
sys.stdin = open("27816_섬 찾기.txt")

N, M = map(int, input().split())
map = [list(map(int, input())) for _ in range(N)]

# # 섬 확인용
# for row in map:
#     print(row)

# 방향키 상 하 좌 우 좌상 우상 좌하 우하
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

visited = [[False] * M for _ in range(N)]

# dfs_재귀 함수 만들기
def dfs_stack(start_r, start_c, direction):
    
    visited[start_r][start_c] = True

    for i in range(direction):
        nr = start_r + dr[i]
        nc = start_c + dc[i]

        if 0<=nr<N and 0 <=nc<M:
            if map[nr][nc] == 1 and not visited[nr][nc]:
                dfs_stack(nr, nc , direction)

cnt = 0
for r in range(N):
    for c in range(M):
        if map[r][c] == 1 and not visited[r][c]:
            cnt += 1
            dfs_stack(r, c, 8)

print(cnt)
