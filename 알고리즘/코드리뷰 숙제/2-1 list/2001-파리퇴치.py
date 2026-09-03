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

    # 더하기 영역에서 


    # 배열을 순회하며 더하기 영역을 찾기
    # N - M + 1 까지만 이동해야 함. 
    for r in range(N - M + 1):
        for c in range(N - M + 1):


    





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