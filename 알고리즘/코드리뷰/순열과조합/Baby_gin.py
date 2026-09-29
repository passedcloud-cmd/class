## 순열
import sys
sys.stdin = open('Baby_gin.txt')

def find_run(arr):
    return arr[2] == arr[1] + 1 and arr[1] == arr[0] + 1

def find_triplet(arr):  
    return arr[2] == arr[1] == arr[0]

T = int(input())
for test_case in range(1, T+1):
    cards = list(map(int, input()))
    result = 0

    import itertools
    cards_list = list(itertools.permutations(cards))

    for per in cards_list:
        left = per[0:3]
        right = per[3:]


        if (find_run(left) or find_triplet(left)) and (find_run(right) or find_triplet(right)):
            result = 1
            break # for per

    print(f'#{test_case} {result}')



        






#1 1
#2 1
#3 0
#4 1
#5 1
#6 1
#7 1
#8 1
#9 0