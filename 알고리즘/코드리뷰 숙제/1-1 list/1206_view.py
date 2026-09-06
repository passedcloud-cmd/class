import sys
sys.stdin = open("1206_view.txt")

# test_case가 10이라고 문제에 주어짐
T = 10

for test_case in range(1, T + 1):
    # 건물의 개수 N
    N = int(input())

    # 각 건물의 높이
    each_height = list(map(int, input().split()))

    # 조망권 보장된 층의 개수
    result_counting = 0

    # n번째 건물에서 왼쪽 두 건물과 오른쪽 두 건물의 높이차를 각각 구하기
    # 높이차 4개가 전부 양수라면 조망권 보장된 층이 있음
    # 높이차가 가장 작은 수 = 조망권 보장된 층의 수
    for n in range(2, N - 2):
        # 높이차 4번 구하기
        left_2 = each_height[n] - each_height[n - 2]
        left_1 = each_height[n] - each_height[n - 1]
        right_2 = each_height[n] - each_height[n + 2]
        right_1 = each_height[n] - each_height[n + 1]

        # 높이차 4개가 모두 양수 -> n번째 건물이 가장 높다 -> 조망권 보장된 층이 있다
        if left_2 > 0 and left_1 > 0 and right_2 > 0 and right_1 >0 :

            #최솟값 구하기
            height_arr = [left_2, left_1, right_1, right_2]
            min_height = height_arr[0] # 최솟값 임의로 할당
            for i in height_arr:
                if min_height > i:
                    min_height = i

            # 조망권 보장 층수 누적
            result_counting += min_height

    print(f'#{test_case} {result_counting}')



# 출력
#1 691
#2 9092
#3 8998
#4 9597
#5 8757
#6 10008
#7 10194
#8 10188
#9 9940
#10 8684