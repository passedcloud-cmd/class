food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.

# 리스트의 각 요소 dict 값이 "{이름}은/는 {종류}(이)다".로 나오게 해야함.
# 그렇다면 디렉토리에서 key값을 불러오게 하면 되지 않을까
# print(food_list[i]['이름'])
# print(food_list[i]['종류']) 이것들을 i번 반복하게 하면 될 것 같다
# 리스트의 i 자체가 디렉토리임을 주의!

# for i in food_list:
#     if i['이름'] == '토마토':
#         i['종류'] = '과일'
#         print(str(i['이름']) + " 은/는 " + str(i['종류']) + " (이)다.")
#     elif i['이름'] == '자장면':
#         print("자장면엔 고춧가루지")
#         print(str(i['이름']) + " 은/는 " + str(i['종류']) + " (이)다.")
#     else:
#         print(str(i['이름']) + " 은/는 " + str(i['종류']) + " (이)다.")

# # 토마토의 종류를 과일로 변경해야 하니까 if문 사용
# # 자장면에 문자열을 추가해야 하니까 elif

# print(food_list) # 반복문이 끝나고 food_list 출력




# 이제 for문을 while문으로 변경해야 함
# 몇 번 반복할 건지는 len를 사용해야 할 듯. count에 len(food_list)를 넣고 한 번 돌릴 때마다 -1을 하자
# print(len(food_list)) # food_list의 길이는 3이니까 1이 되면 중단하는 걸로.

count = len(food_list)
i = -1

while count > 0:
    count = count -1
    i = i + 1
    if food_list[i]['이름'] == '토마토':
        food_list[i]['종류'] = '과일'
        print(str(food_list[i]['이름']) + " 은/는 " + str(food_list[i]['종류']) + " (이)다.")
    elif food_list[i]['이름'] == '자장면':
        print("자장면엔 고춧가루지")
        print(str(food_list[i]['이름']) + " 은/는 " + str(food_list[i]['종류']) + " (이)다.")
    else:
        print(str(food_list[i]['이름']) + " 은/는 " + str(food_list[i]['종류']) + " (이)다.")

print(food_list)