number_of_people = 0 # 전역 변수

def increase_user():
    global number_of_people # 전역 변수로 선언
    number_of_people += 1

increase_user()
print("현재 가입된 유저 수 : " + str(number_of_people))

# increase_user()
# increase_user()
# increase_user()
# increase_user()
# print(number_of_people) # 5