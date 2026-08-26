data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
# 대문자이거나 공백 ' '인 경우만 출력
# isupper 메서드 활용
# 모든 문자열은 한 줄에 출력

# if문을 사용할까?
# 인덱싱을 해서 요소가 대문자이거나 공백이면  리스트에 추가

arr_1 =[]

for i in range(len(data_1)):
    if data_1[i].isupper() == True or data_1[i] == ' ':
        arr_1.append(data_1[i])
        # arr_1 원본값이 변경

# print(arr_1) # arr_1 확인

# 모든 문자열을 한 줄에 출력해야 함
for text in arr_1:
    print(text, end='')

print()

data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.
#'내힘들다' 각 글자들이 위치한 index번호를 find 메서드로 찾는다
# 찾은 index번호를 arr 리스트에 append메서드로 추가
# sort 메서드로 arr 리스트를 오름차순으로 정렬
# 각 요소 번째에 위치한 문자열을 출력
# 모든 문자열은 한 줄에 출력


# '내힘들다'가 4음절이니까 find 메서드 4번 반복?
# print(data_2.find('내'))
# print(data_2.find('힘'))
# print(data_2.find('들'))
# print(data_2.find('다'))

# arr 리스트에 append 메서드로 추가합시다
arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))
print(arr)

# sort 메서드로 리스트를 오름차순 정렬
arr.sort() #원본 데이터를 변경

print(arr)

# 각 요소 번째에 위치한 문자열을 출력
for i in arr:
    print(data_2[i], end='')
