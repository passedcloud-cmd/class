import sys

sys.stdin = open('4828-min_max.txt')

T = int(input()) #3

count = 1

for _ in range(T): # T=3번 반복
    N = int(input())
    arr = list(map(int, (input().split())))
    print(arr)
    # print(N)
    for _ in range(N):
        for j in arr:
            min_num = arr[0]
            max_num = arr[0]

            if min_num > j:
                min_num = j

            if max_num < j:
                max_num = j

    print(f"#{count} {max_num - min_num}")
    count += 1



# 정답 예시
#1 630739
#2 740510
#3 838110