N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
# N번만큼 반복하여 data_1에 담긴 문자열을 인덱스 번호 순대로 arr_1 리스트에 추가
# append 메서드 활용

# 문자열도 시퀀스인가? yes. 그렇다면 인덱싱 가능.

for i in range(len(data_1)):
    arr_1.append(data_1[i])

print(arr_1)


M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
# 공백을 기준으로 문자열을 나누기
# split 메서드 활용
# 홀수만 출력하기

data_2.split()


# print(type(data_2.split())) # split은 리스트를 반환
# print(data_2.split())
# print(data_2[0])
# print(type(data_2[0])) # data_2 요소 값들은 str
# print(type(int(data_2[0])))
# print(int(data_2[0])) # int를 씌우면 정수가 됨
# print(int(data_2[0]) + 19)

# data_2.split()의 반환값을 저장해야 함!
arr_2 = data_2.split()

for i in range(len(arr_2)):
    if int(arr_2[i]) % 2 == 1:
        print(arr_2[i])
