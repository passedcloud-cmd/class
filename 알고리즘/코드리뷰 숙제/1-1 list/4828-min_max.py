import sys

sys.stdin = open('4828-min_max.txt')

T = int(input())

N = int(input())

for i in range(1, N + 1):
    arr = list(map(int, (input().split())))

for i in arr:
    min_num = arr[0]
    max_num = arr[0]
    if min_num > i:
        min_num = i
    if max_num < i:
        max_num = i

print(f"#{T} {max_num - min_num}")


# 정답 예시
#1 630739
#2 740510
#3 838110