import sys

sys.stdin = open('sample_input.txt')

T = int(input()) #3


for _ in range(T): # 전체적으로 T번 반복
    N, M = map(int, input().split())
    # print(N, M) # N, M값 확인용
    arr = list(map(int, input().split()))
    # print(arr) # arr 확인용
    for i in range(0, N-M+1): # 0번부터 N-M+1번까지 M개씩 더하기 반복
        sum_arr = 0
        sum_arr_min = 0
        sum_arr_max = 0
        for j in range(M):
            sum_arr += arr[i + j]
            sum_arr_min += arr[j]
            sum_arr_max += arr[j]
            if sum_arr < sum_arr_min:
                sum_arr_min = sum_arr
            if sum_arr > sum_arr_max:
                sum_arr_max = sum_arr
    print(sum_arr_max - sum_arr_min)



# # N,M = 10 ,3인 경우
# for _ in range(1):
#     N, M = map(int, input().split())
#     # print(N, M) # N, M값 확인용
#     arr = list(map(int, input().split()))
#     # print(arr) # arr 확인용
#     for i in range(0, 8): # 0번부터 N-M+1번까지 M개씩 더하기 반복
#         sum_arr_min = arr[0] + arr[1] + arr[2]
#         sum_arr_max = arr[0] + arr[1] + arr[2]
#         sum_arr = arr[i] + arr[i + 1] + arr[i + 2]
#         if sum_arr < sum_arr_min:
#             sum_arr_min = sum_arr
#         if sum_arr > sum_arr_max:
#             sum_arr_max = sum_arr
#     print(sum_arr_max - sum_arr_min)
#
# # N,M = 10 ,5인 경우
# for _ in range(1):
#     N, M = map(int, input().split())
#     # print(N, M) # N, M값 확인용
#     arr = list(map(int, input().split()))
#     # print(arr) # arr 확인용
#     for i in range(0, 6): # 0번부터 N-M+1번까지 M개씩 더하기 반복
#         sum_arr_min = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
#         sum_arr_max = arr[0] + arr[1] + arr[2] + arr[3] + arr[4]
#         sum_arr = arr[i] + arr[i + 1] + arr[i + 2] + arr[i + 3] + arr[i + 4]
#         if sum_arr < sum_arr_min:
#             sum_arr_min = sum_arr
#         if sum_arr > sum_arr_max:
#             sum_arr_max = sum_arr
#     print(sum_arr_max - sum_arr_min)