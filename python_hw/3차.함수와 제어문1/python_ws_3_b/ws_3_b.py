# pro_num = 1000
# global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# def create_data():
#     data = {}
#     return data

# result_1 = create_data()
# result_2 = create_data()
# result_3 = create_data()


pro_num = 1000
global_data = {'subject': 'python', 'day': 3, 'title': '함수 활용하기'}

# global에 정의된 pro_num 변수의 값에 1을 더한 값이란
# global 키워드로 변수의 스코프를 전역 범위로 지정하라는 뜻

def create_data(subject, day, title = None):
    global pro_num
    pro_num = pro_num + 1
    data = {'과목': subject, '일차': day, '제목': title, '문제 번호': pro_num}
    return data

result_1 = create_data('python', 3)
result_2 = create_data(subject = str('web'), day = int(1), title = 'web 연습하기')

# global_data변수를 언패킹해서 인자로 전달하기
result_3 = create_data(**global_data)

print(result_1)
print(result_2)
print(result_3)