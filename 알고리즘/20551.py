import sys
sys.stdin = open("20551.txt")

T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())

    # 조건에 성립하지 않으면 continue
    if A < 1 or B < 2 or C < 3:
        continue

    eat = 0 # eat 0으로 초기화
    
    if B >= C:
        eat += B - (C - 1) # B - eat = C - 1
        B = C - 1

    if A >= B:
        eat += A - (B - 1) # A - eat = C - 1
        A = B - 1

    print(f'#{test_case} {eat}')


#1 -1
#2 0
#3 1
#4 2