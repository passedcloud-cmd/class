import sys
sys.stdin = open('algo2_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 목장의 크기
    N = int(input())
    # 목장맵. 크기 N x N
    my_map = [list(map(int, input().split())) for _ in range(N)]

    # # 확인용 출력p
    # for row in my_map:
    #     print(row)

    # 방향키 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 방문 기록 N x N
    visited = [[False] * N for _ in range(N)]

    # bfs_queue로 탐색 함수 만들기 - 양을 발견하면 해당 양이 있는 무리를 확인
    from collections import deque
    def bfs_queue(start_r, start_c):
        # 큐에 시작 좌표 넣고 시작
        queue = deque()
        queue.append([start_r, start_c])

        # 양의 수
        tmp_cnt = 0
        while queue:
            r, c = queue.popleft()
            # 해당 좌표에 양이 있고, 방문한 적이 없다면
            if my_map[r][c] == 1 and not visited[r][c]:
                # 양 한 마리 세기
                tmp_cnt += 1
                # 방문 표시 하기
                visited[r][c] = True

                # 인근에 양이 또 있는지 확인해야 함
                for i in range(4): # 상하좌우 네 방향 확인
                    nr = r + dr[i]
                    nc = c + dc[i]
                    # 경계 체크
                    if 0 <= nr < N and 0 <= nc < N:
                        # 만약 다음 좌표에 또 양이 있고, 방문한 적이 없다면
                        if my_map[nr][nc] == 1 and not visited[nr][nc]:
                            # queue에 다음 좌표 넣기
                            queue.append([nr, nc])
        # 결과는 양의 수
        return tmp_cnt

    # 늑대의 수
    cnt_wolf = 0
    # 맵을 완전 탑색하기
    for i in range(N):
        for j in range(N):
            # 해당 좌표에 양이 있고 방문한 적이 없다면
            if my_map[i][j] == 1 and not visited[i][j]:
                # 양 무리 탐색
                cnt_sheep = bfs_queue(i, j)
                # 만약 양의 수가 5 이상이라면 늑대 한 마리 추가
                if cnt_sheep >= 5:
                    cnt_wolf += 1

    print(f'#{test_case} {cnt_wolf}')

