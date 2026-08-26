# black_list = [
#     'Hoeger LLC',
#     'Keebler LLC',
#     'Yost and Sons',
#     'Johns Group',
#     'Romaguera-Crona',
# ]

# import requests
# from pprint import pprint as print

# API_URL = 'https://jsonplaceholder.typicode.com/users'

# response = requests.get(API_URL)
# parsed_data = response.json()

# print(response)

## 회사명과 사용자 이름 매칭
# censored_user_list = {}

# def create_user():
#     for i in range(len(parsed_data)):
#         censored_user_list[parsed_data[i]['company']['name']] = parsed_data[i]['name']

# create_user()
# print(censored_user_list)



# 일단 따라 적어보겠음

"""
로직 흐름 3단계:
    1단계 [수집] API에서 유저 10명을 받아, 위경도 조건 통과자만 리스트에 쌓는다.
    2단계 [검열] 블랙리스트 소속이면 등록 거부(False), 아니면 통과(True).
    3단계 [그룹핑] 통과한 유저를 회사별로 묶어 {회사: [이름들]} 형태로 만든다.
"""

from pprint import pprint

import requests

# 등록을 거부할 블랙리스트 회사 목록
black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

# 1단계 [수집] -- API에서 유저를 받아, 조건 통과자만 리스트에 쌓는다
def collect_users():
    # 빈 리스트를 먼저 만든다 -> 조건을 통과한 유저를 여기에 쌓을 것이다.
    dummy_data = []

    for i in range(1, 11):
        api_url = f'https://jsonplaceholder.typicode.com/users/{i}'
        response = requests.get(api_url).json()
        # print(response)를 하면 아무것도 안 나옴

        # 위도/경도는 문자열로 오므로 float으로 변환해서 비교한다
        lat = float(response['address']['geo']['lat']) # response는 리스트 아닌가? 인덱싱 안 해도 돼?
        lng = float(response['address']['geo']['lng'])

        # 조건: 위도와 경도가 모두 -80 ~80 번위일 때만 수집
        if -80 < lat < 80 and -80 < lng <80:
            user_info = {
                'name': response['name'],
                'lat': response['address']['geo']['lat'],
                'lng': response['address']['geo']['lng'],
                'company': response['company']['name'],
            }
            dummy_data.append(user_info) # 누적: 통과한 사람만 쌓기

    return dummy_data

collect_users()
print(dummy_data)






