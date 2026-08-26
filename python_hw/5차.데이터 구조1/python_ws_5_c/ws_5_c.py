# original_word 변수에 담긴 각 문자열을 모두 나누어 arr리스트에 담는다.
# extend 메서드를 활용
# arr리스트를 출력

# 문장에서 잘못된 내용을 제거하는 함수 restructure_word 함수 작성
# 인자로 넘겨받은 word 문자열을 순회하며 아래 조건에 맞춰 arr에서 불필요한 문자열을 제거
# 만약 순회중인 문자열이 숫자면, 해당 숫자만큼 반복하여 arr의 마지막 요소를 제거
# isdecimal 메서드와 pop 메서드를 활용
# 그외의 경우 arr에서 해당 문자열 제거
# remove 메서드 활용


def restructure_word(word, arr):
    for char in word:
        if char.isdecimal():
            n = int(char)
            for _ in range(n):
                arr.pop()
        else:
            arr.remove(char)
    return arr

original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []


# 불필요한 문자를 제거한 arr 반환
# 함수 호출 결과를 result 변수에 담고 result를 출력
# result에 할당된 리스트를 하나의 문자열로 변환하여 출력 - join 메서드 활용


# result = restructure_word(word, arr)

arr.extend(original_word)
print(arr)  
# 문자 단위로 나뉜 리스트 확인

result = restructure_word(word, arr)
print(result)              
print(''.join(result))     

