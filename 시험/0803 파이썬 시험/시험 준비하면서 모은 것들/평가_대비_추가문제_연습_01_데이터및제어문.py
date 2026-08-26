# 01_데이터_및_제어문: 1번 갯수 구하기
students = ['김철수', '이영희', '조민지']
count = 0
for i in students:
    count += 1
print(count)

# +다른 방법
print(len(students))



# 01_데이터_및_제어문: 2번 득표수 구하기
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
lee_count = 0
for i in range(len(students)):
    if students[i] == '이영희':
        lee_count += 1
print(lee_count)



# 01_데이터_및_제어문: 3번 최댓값 구하기
numbers = [7, 10, 22, 4, 3, 17]
max_number = numbers[0]
for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
print(max_number)

# +내장 함수를 사용하는 방법
print(max(numbers))
print(sorted(numbers)[-1])



# 01_데이터_및_제어문: 4번 최솟값 구하기
numbers = [7, 10, 22, 4, 3, 17]
min_number = numbers[0]
for i in range(len(numbers)):
    if numbers[i] < min_number:
        min_number = numbers[i]
print(min_number)



# 01_데이터_및_제어문: 5번 최댓값과 등장 횟수 구하기
numbers = [7, 10, 22, 7, 22, 22]
frequency = {}
max_number = numbers[0]
for i in range(len(numbers)):
    frequency[numbers[i]] = 0

for i in range(len(numbers)):
    if numbers[i] > max_number:
        max_number = numbers[i]
    if numbers[i] in numbers:
        frequency[numbers[i]] +=1

high_frequency = list(frequency.values())[0]
for i in range(len(frequency.values())):
    if list(frequency.values())[i] > high_frequency:
        high_frequency = list(frequency.values())[i]

print(max_number, high_frequency)

# 문제를 잘못봐서 다시 푸는 최댓값과 최댓값의 등장 횟수 구하기
numbers = [7, 10, 22, 7, 22, 22]
max_number = numbers[0]
for i in numbers:
    if i > max_number:
        max_number = i

count_max_number = 0
for i in numbers:
    if i == max_number:
        count_max_number += 1

print(max_number, count_max_number)

# 모범 답
max_value = numbers[0]
count = 0
for number in numbers:
    if number > max_value:
        max_value = number
        count = 1
    elif number == max_value:
        count += 1

print(max_value, count)



# 01_데이터_및_제어문: 6번 5의 개수 구하기
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
count_5 = 0
for i in range(len(numbers)):
    if numbers[i] == 5:
        count_5 += 1
print(count_5)



# 01_데이터_및_제어문: 7번 'a'가 싫어
# word = input()
word = 'apple is apple'
list_word = list(word)
for i in list_word:
    if i == 'a':
        list_word.remove('a')
word = "".join(list_word)
print(word)

# 모범 답안
# 문자열을 하나씩 확인하면서, a가 아니면, 기록한다.(변수 result)
result = ''
for char in word:
    if char != 'a':
        result += char
# 5. 끝
print(result)



# 01_데이터_및_제어문: 8번 단어 뒤집기
# word = input()
word = 'hello'
print(word[::-1])

# 다른 풀이
word = 'apple'
# 1. 초기화
result = ''
# 2. 단어 순회하면서,
for char in word:
    # 3. 앞에 더 해나간다.
    result = char + result
print(result)