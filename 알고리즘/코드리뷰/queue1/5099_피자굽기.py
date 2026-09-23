import sys
sys.stdin = open("5099_피자굽기.txt")
T = int(input())

from collections import deque

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese_list = list(map(int, input().split()))
    # cheese_deque = deque(cheese_list)

    last_pizza = -1
    # 피자를 전부 빼낼 때까지 반복
    while cheese_list:
        # 피자 개수 만큼 확인
        for i in range(len(cheese_list)):
            # 치즈양이 0이면 꺼내기
            if cheese_list[i] == 0:
                cheese_list.pop(i)
                last_pizza = i

                # 그 자리에서 남은 피자를 순서대로 넣기
                cheese_deque = deque(cheese_list)
                if cheese_deque:
                    cheese_deque.rotate(-i)
                    cheese_list = list(cheese_deque)

        # 남은 피자들의 치즈는 절반이 줄어든다
        for i in range(len(cheese_list)):
            cheese_list[i] = cheese_list[i] // 2

    print(last_pizza)


















#1 4
#2 8
#3 6