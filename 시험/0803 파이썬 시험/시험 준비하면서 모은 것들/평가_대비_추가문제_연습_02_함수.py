# 02_함수 practice 1: 1번 all() 구현
def my_all(elements):
    if bool(elements) is False:
        result = True
        return result
    else:
        for i in elements:
            if bool(i) is False:
                result = False
                break
            else:
                result = True
        return result
    
print(my_all([]))
print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(all([]), all([1, 2, 5, '6']), all([[], 2, 5, '6']))

# 모범 답안
def my_all(elements):
    # 1. 변수 초기화
    result = True
    # 2. 반복
    for element in elements:
        # 3. 조건 - 요소가 참이 아니라면
        # # 해당 값이 참인지 거짓인지 알기 위해서는 bool 즉 아래와 같이 생각할 수 있는데,
        # if bool(element) == False:
        # # 거짓인지 확인하는 것은 not True를 확인하는 것이다.
        # if not bool(element):
        # # if에서는 자동 형변환이 발생한다.
        # # 따라서, 다음과 같이 작성할 수 있다.
        if not element:
            result = False
            # 4. 한번이라도 발생하면 종료시켜야 하기 때문에, break
            break
    # 5. 반환
    return result

# 그럼 이제 비어있는 경우는 어떻게 처리될까?
# 아니다. 비어있다면 반복문이 돌지 않을 것이고, 바로 result에 True가 반환된다.
# 즉 이 로직에서는 따로 예외처리를 할 필요가 없다.

# 함수는 return과 함께 호출이 종료된다. 
# 즉, 함수라면 아래와 같이 작성이 가능하다.
def my_all(elements):
    for element in elements:
        # 하나라도 거짓이면,
        if not element:
            # False 반환
            return False
    # False 반환된 적이 없다면, 모두 참이므로 True
    return True



# 02_함수 practice 1: 2번 any() 구현

def my_any(elements):
    if bool(elements) is False:
        result = False
    else:
        for i in elements:
            if bool(i) is True:
                result = True
                break
            else:
                result = False
        return result

print(my_any([1, 2, 5, '6']))
print(my_any([[], 2, 5, '6']))
print(my_any([0]))
print(any([1, 2, 5, '6']), any([[], 2, 5, '6']), any([0]))

# 모범 답안
'''
핵심 - all 뒤집기
'''
def my_any(elements):
    for element in elements:
        if element:
            return True
    return False



print('-----' * 5)
# 02_함수 practice 2: 1번 불쌍한 달팽이

import math

def snail(height, day, night):
    if height <= 0:   # height에 0이하 값을 넣을 경우
        result = 0
    elif height <= day:   # 첫날 낮에 도착
        result = 1
    elif day < night :   # 오를 수 없는 날
        result = "오를 수 없음"  
    else:
        day_move = day - night
        # 마지막 날은 need_day에서 제외하고, 나중에 +1 하기
        # (need_day - 1) * day_move + day >= height 
        need_day = math.ceil((height - day) / day_move) + 1
        result = need_day
    return result

print(snail(100, 5, 2)) #33
print(snail(100, 9, 3)) # 17
print(snail(100, 10, 9)) # 91

# 모범답안
def snail(height, day, night):
    count = 0
    while True:
        count += 1
        height -= day
        if height <= 0:
            return count
        height += night



# 02_함수 practice 2: 2번 자릿수 더하기 (SWEA #2058)
def sum_of_digit(number):
    number_to_str = str(number)
    sum = 0
    for i in number_to_str:
        sum = sum + int(i)
    result = sum
    return result

print(sum_of_digit(1234)) #10
print(sum_of_digit(4321)) #10

# 모범답안
''' 
접근방법

각 자리의 수를 알아내려면 어떻게 해야할까?
321 = 3*100 + 2*10 + 1*1 로 표현 가능하다.

단계적으로 생각하면 어떻게 될까.
321/10 => 몫 32, 나머지 1 (일의자리)
    32/10 => 몫 3, 나머지 2 (십의자리)
        3/10 => 몫 0, 나머지 3 (백의자리)
            0/10 => 종료

계속 10으로 나누는 반복을 하다가
몫이 0이 되면 종료하자.
'''

def sum_of_digit(number):
    # 1. 변수 초기화
    total_sum = 0
    # 2. 한자리의 경우 0/10 => 0 즉, False 가 될 때까지.
    while number / 10:
        # 3. 몫과 나머지를 분리하기
        # 아래의 코드는 number, remainder = divmod(number, 10) 으로 변경 가능하다.
        remainder = number % 10
        number = number // 10
        # 4. 나머지를 더하기
        total_sum += remainder
    return total_sum

print(sum_of_digit(1234))


# 02_함수 practice 3: 회문 판별
# 각각 while문과 재귀함수를 사용한 함수를 2개 만들기

def is_pal_while(word):
    # word의 개수 구하기
    chr_count = len(word) - 1
    order = 0
    while chr_count > 0:
        chr_count -= 1
        order += 1
        # 순서대로 읽었을 때의 한 글자와 거꾸로 읽었을 때의 한 글자가 같으면 True
        if word[order] == word[chr_count]:
            result = True
        else:
            result = False
            break
    return result

print(is_pal_while('tomato')) #False
print(is_pal_while('racecar')) #True
print(is_pal_while('azza')) #True

def is_pal_while2(word):
    result = True
    while len(word) >= 1:
        if word[0] == word[-1]:
            word = word[1:-1]
            result = True
        else:
            result = False
            break
    return result

print(is_pal_while2('tomato')) #False
print(is_pal_while2('racecar')) #True
print(is_pal_while2('azza')) #True

# 재귀함수로 구하기
# 내부에 스스로가 반복되어야 함
def is_pal_recursive(word):
    if len(word) <= 1:       # base case: 종료 조건 추가
        result = True
        return result        # 첫 번재 경우에 대해 return 값을 반환해야 함
    if word[0] == word[-1]:
        word = word[1:-1]
        return is_pal_recursive(word)
    else:
        return False

print(is_pal_recursive('tomato')) #False
print(is_pal_recursive('racecar')) #True
print(is_pal_recursive('azza')) #True

print('---' * 10)

