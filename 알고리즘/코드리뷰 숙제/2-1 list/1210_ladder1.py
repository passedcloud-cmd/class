import sys
sys.stdin = open("1210_ladder1.txt")


def find_destination(arr, start_y):
    # 시작점 초기화
    x, y = 0, start_y

    # 최하단 x=99까지 반복
    while x < 99:
        # 왼쪽 확인
        if y - 1 >=0 and arr[x][y - 1] == 1:
            while y - 1 >= 0 and arr[x][y - 1] == 1:
                y -= 1

        # 오른쪽 확인
        elif y + 1 < 100 and arr[x][y + 1] == 1:
            while y + 1 < 100 and arr[x][y + 1] == 1:
                y += 1

        x += 1

    # x = 99에 도달
    if arr[x][y] == 2:
        return start_y
    else:
        return -1
    

T = 10 # 문제에서 주어짐
for test_case in range(1, T + 1):
    N = int(input()) # 테스트 케이스 번호
    arr = [list(map(int, input().split())) for _ in range(100)]

    for c in range(100):
        if arr[0][c] == 1:
            result = find_destination(arr, c)

        if result != -1: 
            print(f'#{N} {result}')
            break

# 오답노트
# return 값은 strat_y 아니면 -1이므로 result == 2 라고 하면 안됨

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

