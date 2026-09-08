import sys 
sys.stdin = open("4866_괄호검사.txt")
T = int(input())

for test_case in range(1, T + 1):
    input_txt = input()
    stack = []
    result = 1 # result가 1이면 유효, 0이면 오류

    for char in input_txt:
        # 여는 괄호 추가
        if char == '(' or char == '{':
            stack.append(char)

        # 닫는 괄호 ) 나오면
        elif char == ')':
            # 스택이 비어 있으면 종료. 스택에서 꺼낸 값이 (가 아니어도 종료. result는 0
            if stack == [] or stack.pop() != '(':
                result = 0
                break # for car

        # 닫는 괄호 }가 나오면
        elif char == '}':
            # 스택이 비어 있으면 종료. 스택에서 꺼낸 값이 {가 아니어도 종료. result는 0
            if stack == [] or stack.pop() != '{':
                result = 0 
                break # for car

    # 모든 문자를 확인했는데 스택에 값이 남아있으면 종료. result는 0
    if stack:
        result = 0

    print(f'#{test_case} {result}')




# 입력
# 3
# print('{} {}'.format(1, 2))
# N, M = map(int, input().split())
# print('#{} {}'.format(tc, find())


# 출력
# #1 1
# #2 1
# #3 0