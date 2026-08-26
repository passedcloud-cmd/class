"""
[문제] 내장 함수 min(), max()를 사용하지 않고
       리스트에서 최댓값과 최솟값을 구하시오.

조건
  1. min(), max(), sorted(), sort() 사용 금지
  2. 반복문(for)과 비교 연산자(<, >)만 사용

예시
  numbers = [3, 1, 4, 1, 5, 9, 2, 6]
  최솟값: 1
  최댓값: 9
"""

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# TODO: 여기에 코드를 작성하세요.

# 맨 처음 요소를 기준점으로 잡는다
# 리스트 내 다른 요소보다 큰지 작은지를 if문으로 비교

# 최솟값 구하기
# minimum = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] < minimum:
#         minimum = numbers[i]
        
# print(minimum)

# # 최댓값 구하기
# maximum = numbers[0]

# for i in range(len(numbers)):
#     if numbers[i] > maximum:
#         maximum = numbers[i]

# print(maximum)

# 최댓값과 최솟값 둘 다 for문 하나로 구하기
minimum = numbers[0]
maximum = numbers[0]
maximum = 1

print(minimum)
print(maximum)

for i in range(len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]
    elif numbers[i] > maximum:
        maximum = numbers[i]

print('최솟값:', minimum)
print('최댓값:', maximum)
