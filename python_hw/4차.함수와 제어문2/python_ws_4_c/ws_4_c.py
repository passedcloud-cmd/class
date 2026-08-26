matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.

# matrix의 총 길이를 matrix_len 변수에 담는다.
matrix_len = 0

for i in matrix:
    matrix_len += 1

print(matrix_len)


# matrix가 가진 각 요소의 길이를 출력
# for문 안에 for문 

order = 0
for number in matrix:
    temporary_len = 0
    for i in number:
        temporary_len += 1
    if temporary_len <= 4: # temporary_len가 5일 땐 출력하면 안됨. if문 추가해야 할 듯
        # matrix를 인덱스할 방법을 찾아야 함. for 를 추가할까? →아니요. order라는 변수를 넣어 인덱싱하자.
        print(str(matrix[order]) + " 리스트는 " + str(temporary_len) + "개 만큼 요소를 가지고 있습니다.")
    order = order + 1



# range와 len을 사용하여 matrix와 matrix가 가진 각 리스트들의 인덱스를 기준으로 순회하도록 for문 작성

# for문 안에 for문을 넣어야 할 듯
for i in range(len(matrix)):   # 매트릭스 0 ~ 5 번째 요소. len(matrix)는 그냥 숫자라서 iterable아님. range 쓰자.
    for j in range(len(matrix[i])):    # 매트릭스 내부 요소
        print(f"matrix의 {i}, {j} 번째 요소의 값은 " + str(matrix[i][j]) + " 입니다.")





# print("matrix의 번째 요소의 값을 입니다.")