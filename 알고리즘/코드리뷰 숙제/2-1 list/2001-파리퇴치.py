import sys
sys.stdin = open('2001-파리퇴치.txt')

T= int(input())

for test_case in range(1, T + 1):
    # N은 배열의 크기, M은 파리채의 크기
    N, M = map(int, input().split())

    # arr 배열을 만듦
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_num = arr[0][0] + arr[0][1] + arr[1][0] + arr[1][1] # 최댓값 임의로 정함

    # 더하기 영역에서 시작점-끝점 영역을 찾아서 그 영역 내 값 더하기
    # N - M + 1 까지만 이동해야 함. 그 밖은 영역 벗어남 
    for r in range(N - M + 1):
        for c in range(N - M + 1):

            # 한 칸씩 이동할 때마다 M x M 파리채 영역 합을 초기화
            sum_for_M = 0 

            # 시작점과 끝점 
            r1, c1 = r, c
            r2, c2 = r + M - 1, c + M -1

            # M x M 영역 더하기 
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    sum_for_M += arr[i][j]
            
            # 최댓값 구하기
            if sum_for_M > max_num:
                max_num = sum_for_M

    print(f'#{test_case} {max_num}')
    


    





# 입력
# 10
# 5 2
# 1 3 3 6 7
# 8 13 9 12 8
# 4 16 11 12 6
# 2 4 1 23 2
# 9 13 4 7 3
# 6 3
# 29 21 26 9 5 8
# 21 19 8 0 21 19
# 9 24 2 11 4 24
# 19 29 1 0 21 19
# 10 29 6 18 4 3
# 29 11 15 3 3 29

# 출력
# 1 49
# 2 159