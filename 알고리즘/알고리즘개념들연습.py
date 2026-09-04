# def bubble_sort(arr):
#     """이웃한 두 값을 비교하면서 큰 값을 뒤쪽으로 이동.
#     한 바퀴 돌 때마다 마지막 수가 고정됨."""
#     N = len(arr)
#     for i in range(N-1, 0, -1): # N-1(마지막 수)부터 1번째 수까지.
#         for j in range(i):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]

#     return arr

def bubble_sort(arr):
    """이웃한 두 값을 비교하면서 큰 값을 뒤쪽으로 이동.
    한 바퀴 돌 때마다 마지막 수가 고정됨."""
    N = len(arr)
    for i in range(N-1): # 인덱스 0부터 N-2번째까지.
        for j in range(N-1-i): # 한 바퀴 돌 때마다 마지막 수가 고정되므로 범위 N-1에서 i를 빼기
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
    
numbers = [64, 13, 9, 62, 3]
sorted_numbers = bubble_sort(numbers)
print("정렬 후:", sorted_numbers) # [3, 9, 13, 62, 64]





def counting_sort(input_arr):
    """
    1. 원본 배열에서 가장 큰 수를 기준으로 counting 배열 만들기
    2. 원본 배열의 숫자를 하나씩 세면서 counting 배열에 누적
    3. counting 배열의 앞쪽 요소를 더하면서 배열 업데이트
    4. sorted 배열을 만들어서 요소 배열
    """
    # input_arr에서 가장 큰 수를 찾기
    max_num = input_arr[0] # 임의로 최댓값 설정
    for i in range(len(input_arr)): 
        if input_arr[i] > max_num:
            max_num = input_arr[i]
    print(f'최댓값: {max_num}')
    # 0으로 채운 counting 배열 만들기
    counting_arr = [0] * (max_num + 1) # 0도 있기 때문에 max_num + 1

    # 원본 배열을 한 바퀴 돌면서 counting 배열에 각 숫자 개수 기록
    for i in input_arr:
        counting_arr[i] += 1
    print(f'counting_arr: {counting_arr}')

    # counting_arr에서 앞쪽 숫자 개수 누적해서 칸 채우기
    for i in range(0, max_num): 
        counting_arr[i + 1] += counting_arr[i]
    print(f'counting_arr: {counting_arr}')

    # result_arr 만들기
    result_arr = [0] * len(input_arr)
    for i in input_arr[::-1]:
        result_arr[counting_arr[i]-1] = i
        counting_arr[i] -= 1 

    return result_arr
    
arr = [0, 4, 1, 3, 1, 2, 4, 1]
print('정렬 결과:', counting_sort(arr))  # [0, 1, 1, 1, 2, 3, 4, 4]
# 확인용 sorted 
sorted_arr = sorted(arr)
print(f'오리지널:{arr}, sorted함수:{sorted_arr}')
