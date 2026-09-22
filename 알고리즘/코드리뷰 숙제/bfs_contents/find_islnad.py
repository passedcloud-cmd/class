# 섬 찾기
# 섬 준비
import sys
sys.stdin = open('04_input.txt')
N, M = map(int, input().split())
islands = [list(map(int, input())) for _ in range(N)]



#방향키 상하좌우 상좌 상우 하좌 하우
dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, -1, 1, -1, 1]

#큐 만들기
from collections import deque
queue = deque()

# 섬을 모두 방문처리하는 함수 만들기
def visite_island(start_r, start_c, visited, direction):
    # 시작점은 방문 처리
    visited[start_r][start_c] = True
    # 시작점을 큐에 push
    queue.append((start_r, start_c))

    # queue가 빌 때까지 반복
    while queue:
        r, c = queue.popleft

        # 다음으로 이동
        for i in range(direction):
            nr = r + dr[i]
            nc = c + dc[i]

            # 경계 내에 있다면
            if 0 <= nr < N and 0 <= nc < M:
                # 땅이고 방문한적 없다면
                if islands[nr][nc] == 1 and not visited[nr][nc]:
                    # 다음 땅을 방문
                    visited[nr][nc] = True
                    # 다음 땅을 큐에 추가
                    queue.append((nr, nc))

# 섬 개수 새는 함수 만들기
cnt_island = 0
def count_island(direction):
    for i in range(N):
        for j in range(M):
            if islands[i][j] == 1 and not visited[i][j]:
                cnt_island += 1
                visite_island(i, j, visited, direction)

    return cnt_island

print(cnt_island)