# 03_데이터구조_및_활용 practice 1: 1번 복잡한 리스트의 합
numbers = [
    [1, 4],
    [10, 5],
    [20, 30]    
]

""" 예시 답
sum_list([[1, 4], [10, 5], [20, 30]]) # 70
"""

## for 문을 활용하여 풀이하기
def sum_list(list1):
    sum_numbers = 0
    for i in list1:
        for j in i:
            sum_numbers += j
    return sum_numbers

print(sum_list([[1, 4], [10, 5], [20, 30]])) #70
# print(sum_list([[1, 4], [10, 5], [20, 10]])) #50

## Index로 접근하여 풀이하기
def sum_list_index(list1):
    sum_number = 0
    for i in range(len(list1)):
        sum_number = sum_number + sum(list1[i])
    return sum_number

print(sum_list_index([[1, 4], [10, 5], [20, 30]])) #70
# print(sum_list([[1, 4], [10, 5], [20, 10]])) #50


## while 문을 활용하여 풀이하기
element_number = 0
sum_number = 0
# 리스트의 길이를 넘을 때까지 반복할 때마다 숫자 카운트
def sum_list_while(list1):
    while element_number <= len(list1):
        sum_number = sum(list1(element_number)) + sum_number
        element_number += 1
    return sum_number

print(sum_list_index([[1, 4], [10, 5], [20, 30]])) #70
# print(sum_list([[1, 4], [10, 5], [20, 10]])) #50




print('-----' * 5)
# 03_데이터구조_및_활용 practice 1: 2번 시험 점수
'''* A반 학생들의 점수는 아래와 같고, students 리스트에 저장되어 있다.

    * A학생(국어 100점, 수학 80점, 영어 100점)
    * B학생(국어 90점, 수학 90점, 영어 60점)
    * C학생(국어 80점, 수학 80점, 영어 80점)
'''

## 학생별 출력
students = [
    [100, 80, 100],
    [90, 90, 60],
    [80, 80, 80],
]

for i in students:
    studentstotal_score = 0
    for j in i:
        studentstotal_score += j
    print(studentstotal_score)

# 280
# 240
# 240

# + 그냥 for 문
for student in students:
    print(sum(student))



## 과목별 출력
for i in range(len(students)):
    subject_total_score = 0
    # i는 숫자 int
    # 각 요소의 j번째 값들을 합하기
    # students[0][0] + students[1][0] students[2][0]
    # students[0][1] + students[1][1] students[2][1]
    # students[0][2] + students[1][2] students[2][2]
    for j in students:
        subject_total_score += j[i]
    print(subject_total_score)

# 270
# 250
# 240




print('-----' * 5)
# 03_데이터구조_및_활용 practice 2: 1번 모든 위치

def my_find(text, alphabet):
    find_alphabet = []
    if alphabet not in text:
        result = -1
    else:
        # 찾는 알파벳이 없을 때까지 계속 반복
        for i in range(len(text)):
            if text[i] == alphabet:
                find_alphabet.append(text.find(alphabet, i))
        result = find_alphabet
    return result 

print(my_find('apple', 'p')) # [1, 2]
print(my_find('a', 'p')) # -1

# +enumerate 함수 이용
def my_find(text, alphabet):
    index_list = []
    if alphabet not in text:
        result = -1
    else: 
        for index, chr in enumerate(text):
            if chr == alphabet:
                index_list.append(index)
        result = index_list
    return result

print(my_find('apple', 'p')) # [1, 2]
print(my_find('a', 'p')) # -1
# print(my_find('qwpeomdalksjdfngjat', 'j')) # [11, 16]



print('-----' * 5)
# 03_데이터구조_및_활용 practice 2: 2번 출석 체크

def check(n, students):
    total_list = []
    # 먼저 students를 split로 띄어쓰기 기준으로 나누고 map으로 각 요소를 int로 바꾸기
    # map 결과값은 이터레이터 map 객체라서 list 등으로 변환
    students_list = list(map(int, students.split()))
    # print(students_list) # students_list 확인

    for i in range(n):
        total_list.append(i+1)
    # print(total_list) # total_list 확인

    # students_list요소가 total_list에 있으면 삭제
    for i in students_list:
        if i in total_list:
            total_list.remove(i)
    # print(total_list) # 결석생 제거된 total_list 확인

    # 리스트를 일반 값으로 변환해야함 join 사용
    result = ' '.join(map(str, total_list))
    return result

print(check(7, '1 3 5')) # 2 4 6 7

# + 모범답
def check(n, students):
    students = list(map(int, students.split()))
    result = []
    for i in range(1, n+1):
        if i not in students:
            result.append(str(i))
    return ' '.join(result)




print('-----' * 5)
# 03_데이터구조_및_활용 practice 3: 1번 썩은 과일 찾기
def change_rotten_fruit(fruit_bag):
    # 요소를 하나씩 보고, 요소 앞에 [0:6]이 rotten이면 [5:]으로 슬라이싱
    if bool(fruit_bag) is False:
        fruit_bag = []
        result = fruit_bag
    else:
        for i in range(len(fruit_bag)):
            if fruit_bag[i][0:6] == 'rotten':
                fruit_bag[i] = fruit_bag[i][6:].lower()
        result = fruit_bag
    return result

print(change_rotten_fruit(['apple', 'rottenBanana', 'apple'] )) # ['apple', 'banana', 'apple']
print(change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape'])) # ['apple', 'banana', 'apple', 'grape']
print(change_rotten_fruit([]))


# + 메서드 써보기. 비어있는 경우 고민 안해도 됨. all(), any() 참고
def change_rotten_fruit(fruit_bag):
    result = []
    for fruit in fruit_bag:
        fruit = fruit.replace('rotten', '')
        fruit = fruit.lower()
        result.append(fruit)
    return result




print('-----' * 5)
# 03_데이터구조_및_활용 practice 3: 2번 중복되지 않은 숫자의 합
# 각 요소를 하나씩 꺼낸 다음 .count() 매서드를 통해 1개인 것만 합하기 
def sum_of_repeat_number(numbers):
    count_1 = 0
    for i in numbers:
        if numbers.count(i) == 1 :
            count_1 += i
    result = count_1
    return result

print(sum_of_repeat_number([4, 4, 7, 8, 10])) # 25
print(sum_of_repeat_number([4, 4, 7, 8, 10, 5])) # 30

# + 다른 풀
# 한번 등장한 것을 저장(once)
# 두번이상 등장한 것을 저장(multiple)
# 한번이라도 등장하였다면,
    # multiple로 옮기고
    # once에서 삭제한다.
# 등장한 적이 없고, multiple에 없다면,
    # once에 추가한다.

def sum_of_repeat_number(numbers):
    once = []
    multiple = []
    for number in numbers:
        if number in once:
            multiple.append(number)
            once.remove(number)
        elif number not in multiple:
            once.append(number)
    return sum(once)




print('-----' * 5)
# # 03_데이터구조_및_활용 practice 4: 1번 종합 소득세 계산
def tax(won):
    # if/elif/elif 로 구간 나누기
    if won <= 1200:
        take_tax = won * 0.06
    elif 1200 < won <= 4600:
        take_tax = 1200 * 0.06 + (won - 1200) * 0.15
    elif 4600 < won:
        take_tax = 1200 * 0.06 + (4600 - 1200) * 0.15 + (won - 4600) * 0.35
    result = take_tax
    return take_tax

print(tax(1200)) # 72.0
print(tax(4600)) # 582.0
print(tax(5000)) # 722.0




print('-----' * 5)
# # 03_데이터구조_및_활용 practice 4: 2번 카쉐어링 요금 계산
import math

def fee(minute, distance):
    # 대여 요금 : 10분당 1,200원
    minute_fee = minute // 10 * 1200
    # 보험료 : 30분당 525원 (50분을 빌리면, 1시간으로 계산)
    # 시간을 60으로 나눴는데 나머지가 50 이상이면 몫에 +1
    if minute % 30 == 0 :
        ensurance = (minute / 30) * 525
    elif 0 > minute % 30 > 20 :
        ensurance = (minute / 30) * 525
    elif 20 >= minute % 30 :
        ensurance = ((minute / 30) + 1) * 525    
    # 주행 요금: distance는 km당 170원, 100km가 넘어가면 넘어간 부분에 대하여 85원
    if distance > 100 :
        distance_fee = 100 * 170 + (distance - 100) * 85
    elif distance <= 100 : 
        distance_fee = distance * 170
    result = math.ceil(minute_fee + ensurance + distance_fee)
    return result

print(fee(600, 50)) # 91000
print(fee(600, 110)) # 100350



print('-----' * 5)
# # 03_데이터구조_및_활용 practice 4: 3번 문자열 탐색
count_same = 0
def start_end(words):
    global count_same
    # 요소 반복
    for i in words:
        if len(i) >= 3 and i[0] == i[-1]:
            count_same += 1
    result = count_same
    return result

print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg'])) #3



print('-----' * 5)
# 03_데이터구조_및_활용 practice 4: 4번 Collatz 추측
# > 1. 입력된 수가 짝수라면 2로 나눈다. 
# > 2. 입력된 수가 홀수라면 3을 곱하고 1을 더한다.
# > 3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복한다.
def collatz(num):
    count_num = 0
    while num != 1:
        if count_num > 500:
            count_num = -1
            break
        elif num % 2 == 0:
            num = num / 2
            count_num += 1
        elif num % 2 == 1:
            num = (num * 3) + 1
            count_num += 1
    result = count_num
    return result

print(collatz(6)) #8
print(collatz(16)) #4
print(collatz(27)) #111
print(collatz(626331)) #-1


print('-----' * 5)
# 03_데이터구조_및_활용 practice 4: 5번 딕셔너리 뒤집기
def dict_invert(my_dict):
    new_dict = {}
    # key와 value를 .key()와 .value()로 모두 꺼내서 리스트화
    origin_keys = list(my_dict.keys())
    origin_values = list(my_dict.values())
    # 리스트에 있는 요소들을 거꾸로 배치
    for i in range(len(my_dict)):
        new_dict[origin_values[i]] = origin_keys[i]
    result = new_dict
    return result

print(dict_invert({1: 10, 2: 20, 3: 30})) #=> {10: [1], 20: [2], 30: [3]}
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) #=> {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True})) #=> {True: [1, 2, 3]}

# + 모범 답안 .items()사용
def dict_invert(my_dict):
    new_dict = {}
    for key, item in my_dict.items():
        if item not in new_dict:
            new_dict[item] = [key]
        else:
            new_dict[item].append(key)
    result = new_dict
    return new_dict
    # 딕셔너리에 값이 없는 경우
    

print(dict_invert({1: 10, 2: 20, 3: 30})) #=> {10: [1], 20: [2], 30: [3]}
print(dict_invert({1: 10, 2: 20, 3: 30, 4: 30})) #=> {10: [1], 20: [2], 30: [3, 4]}
print(dict_invert({1: True, 2: True, 3: True})) #=> {True: [1, 2, 3]}

# + 다른 풀이. mydict.get('key', '기본값') → key에 해당하는 value 가져옴. 키가 없으면 기본값을 반환.
def dict_invert(my_dict):
    result = {}
    for key, value in my_dict.items():
        result[value] = result.get(value, []) + [key]
    return result