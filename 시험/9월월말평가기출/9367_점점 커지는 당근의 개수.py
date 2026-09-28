import sys
sys.stdin = open('9367_점점 커지는 당근의 개수.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    carrets = list(map(int, input().split()))

    cnt = 1 # 시작값은 1
    max_cnt = 1 # 최댓값의 시작점도 1
    for i in range(N-1):
        if carrets[i] < carrets[i+1]:
            cnt +=1
            max_cnt = max(cnt, max_cnt)
        else:
            # 연속이 깨지면 cnt 값 리셋 
            cnt = 1

    print(f'#{test_case} {max_cnt}')
