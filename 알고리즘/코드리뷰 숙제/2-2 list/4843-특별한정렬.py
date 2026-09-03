# import sys
# sys.stdin = open("4843-특별한정렬.txt")

# T =int(input())

# for tc in range(1, T + 1):
#     # N은 숫자 개수 
#     N = int(input())

#     arr = list(map(int, input().split()))

#     # 값을 2개씩 비교하니까 N-1 입력. 마지막에 N-2번째를 N-1(마지막)번째와 비교하니까. 
#     for i in range(0, N-1):

#         # 인덱스가 0이거나 짝수(0도 짝수 취급)면 큰 수 순서대로 배열  
#         if i % 2 == 0:
#             for j in range(i, N):
#                 max_index = i # 최대값의 인덱스는 구간의 첫 번째로 임의 배정 
#                 if arr[max_index] < arr[j]:
#                     max_index = j
#                     # 더 큰 값을 찾았다면 위치 바꾸기
#                     arr[i], arr[max_index] = arr[max_index], arr[i]

#         # 인덱스가 홀수면 작은 수 순서대로 배열
#         else:
#             for k in range(i, N):
#                 min_index = i # 최소값의 인덱스는 구간의 첫 번째로 임의 배정 
#                 if arr[min_index] > arr[k]:
#                     min_index = k
#                     # 더 큰 값을 찾았다면 위치 바꾸기
#                     arr[i], arr[min_index] = arr[min_index], arr[i]         

#     # arr는 리스트
#     # 리스트에서 값을 꺼내고 쉼표로 잇기
#     result = ", ".join(str(n) for n in arr[:10])
#     print(f'#{tc} {result}')    


import sys
sys.stdin = open("4843-특별한정렬.txt")

T =int(input())

for tc in range(1, T + 1):
    # N은 숫자 개수 
    N = int(input())

    arr = list(map(int, input().split()))

    # 값을 2개씩 비교하니까 N-1 입력. 마지막에 N-2번째를 N-1(마지막)번째와 비교하니까. 
    for i in range(0, N-1):

        # 인덱스가 0이거나 짝수(0도 짝수 취급)면 큰 수 순서대로 배열  
        if i % 2 == 0:
            max_index = i # 최대값의 인덱스는 구간의 첫 번째로 임의 배정 
            for j in range(i + 1, N):
                if arr[max_index] < arr[j]:
                    max_index = j
            # 더 큰 값을 찾았다면 위치 바꾸기
            arr[i], arr[max_index] = arr[max_index], arr[i]

        # 인덱스가 홀수면 작은 수 순서대로 배열
        else:
            min_index = i # 최소값의 인덱스는 구간의 첫 번째로 임의 배정 
            for k in range(i + 1, N):
                if arr[min_index] > arr[k]:
                    min_index = k
            # 더 작은 값을 찾았다면 위치 바꾸기
            arr[i], arr[min_index] = arr[min_index], arr[i]         

    # arr는 리스트. 리스트에서 값을 꺼내고 쉼표로 잇기
    result = " ".join(str(n) for n in arr[:10]) # 출력값 개수가 10개이므로 arr[:10]
    print(f'#{tc} {result}')    



# 오답 노트 
# 안쪽 반복문에서는 인덱스만 찾고, 반복문이 끝난 뒤 딱 한 번만 교환하는 것.
# arr[i], arr[max_index] = arr[max_index], arr[i]을 for문 밖으로 꺼내야 함.





# 입력
# 3
# 10
# 1 2 3 4 5 6 7 8 9 10
# 10
# 67 39 16 49 60 28 8 85 89 11
# 20
# 3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26


# 출력
# #1 10 1 9 2 8 3 7 4 6 5
# #2 89 8 85 11 67 16 60 28 49 39
# #3 98 3 97 9 88 17 75 18 71 21