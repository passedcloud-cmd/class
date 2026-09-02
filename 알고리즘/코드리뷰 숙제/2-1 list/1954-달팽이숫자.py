import sys

sys.stdin = open("1954-달팽이숫자.txt")

# 임의의 N X N 행렬 생성
# N = int(input())
N = 4
arr = [[0] * T for _ in range(N)]

# 시작점: (1, 1)
r, c = 1, 1 

# 시계 방향 상-우-하-좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
direction_name = ['상', '우', '하', '좌']


# 배열의 첫 번째 칸은 1
arr[0][0]= 1
counting_num = 1

# (N-1번 직진 후 방향 바꾸기) x 3번 + (N-2번 직진 후 방향 바꾸기) x 2번
# + (N-3번 직진 후 방향 바꾸기 ) x 2번 ... (1번 직진 후 방향 바꾸기) x 2번
for _ in range(3):
    for i in range(N-1):
        counting_num += 1
        arr[r][c] = counting_num
    

for _ in range(2):
    for _ in range(N-1):
        c





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