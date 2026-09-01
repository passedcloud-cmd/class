import sys

sys.stdin = open("4834-숫자카드.txt")

T = int(input()) #5

for t in range(T):
    N = int(input())
    arr = list(map(int, input())) # 띄어쓰기 없이 이어진 str을 split() 안 붙여도 됨
    counting_number = {}
    for i in arr:
        counting_number[i] = 0
    for i in arr:
        counting_number[i] += 1

    # 카드 개수 구하기
    number_of_cards = 1
    for i in counting_number:
        if counting_number[i] > number_of_cards:
            number_of_cards = counting_number[i]

    # 가장 많이 나온 숫자 구하기
    keys = []
    for key, value in counting_number.items():
        if value == number_of_cards:
            keys.append(key)

    max_mode_number = keys[0]
    for k in keys:
        if k > max_mode_number:
            max_mode_number = k

    print(f"#{t+1} {max_mode_number} {number_of_cards}")
    

# 입력
# 3
# 5
# 49679
# 5
# 08271
# 10
# 7797946543