import requests
from pprint import pprint as print

API_URL = 'https://jsonplaceholder.typicode.com/users'

response = requests.get(API_URL)
parsed_data = response.json()

print(response)
# print(parsed_data) # parased_data 확인

dummy_data = []

# for i in range(len(parsed_data)):
#     if float(parsed_data[i]['address']['geo']['lat']) < 80 and float(parsed_data[i]['address']['geo']['lng']) > (-80):
#         dummy_data.append(parsed_data[i]['company']['name'])
#         dummy_data.append(parsed_data[i]['address']['geo']['lat'])
#         dummy_data.append(parsed_data[i]['address']['geo']['lng'])
#         dummy_data.append(parsed_data[i]['name'])

# print(dummy_data)

# 정리를 하자

for i in range(len(parsed_data)):
    if -80 < float(parsed_data[i]['address']['geo']['lat']) < 80 and -80 < float(parsed_data[i]['address']['geo']['lng']) < 80:
        dummy_data.append({'company' : parsed_data[i]['company']['name'], 'lat' : parsed_data[i]['address']['geo']['lat'], 'lng' : parsed_data[i]['address']['geo']['lng'], 'name' : parsed_data[i]['name']})

print(dummy_data)