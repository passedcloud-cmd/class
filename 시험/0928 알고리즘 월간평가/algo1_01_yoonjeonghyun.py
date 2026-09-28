import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())
for test_case in range(1, T+1):
    # N은 정수의 개수
    N = int(input())
    # 숫자들의 배열 arr
    arr = list(map(int, input().split()))
    # 결과값 None으로 시작
    result = None

    # 숫자가 2개인 경우 = 짝이 1개인 경우
    if N == 2:
        result = 1

    # 숫자가 3개인 경우도 1 출력
    elif N == 3:
        result = 1

    # 2개나 3개가 아니라면
    else:
        for i in range(1, N//2):
            # 앞자리와 뒷자리의 합 tmp_sum들
            tmp_sum1 = arr[i-1] + arr[N-i]
            tmp_sum2 = arr[i] + arr[N-1-i]
            
            # 합계 확인용
            # print(f'tem_sum1: {tmp_sum1}, tem_sum2: {tmp_sum2} ') 
            
            # 만약 tmp_sum2가 이전값보다 크지 않다면 result = 0
            if tmp_sum2 <= tmp_sum1:
                result = 0
                break # for i

            else:
                result = 1

    print(f'#{test_case} {result}')