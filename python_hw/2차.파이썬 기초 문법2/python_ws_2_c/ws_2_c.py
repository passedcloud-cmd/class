data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

# 아래에 코드를 작성하시오.

# 딕셔너리
first_data = {'제목' : '', '일차' : '', '단계' : '', '과목' : ''}

# data는 값이 1개짜리 리스트
# print(data[0])
dict = data[0]
# print(type(data[0]))
# data[0]은 딕셔너리


# print(dict['results'])
# dict['results']는 리스트


# print(dict['results'][0])
# dict['results'][0]는 딕셔너리


# print(dict['results'][0]['properties'])
# print(dict['results'][0]['properties']['제목']['title'][0]['plain_text'])
# 리스트에서 첫 번째 요소는 0번이라는 것 명심. 리스트는 순번으로 인덱스 불러오기가 가능하나, 딕셔너리는 순서가 없어서 key값으로 value를 불러온다.

title = dict['results'][0]['properties']['제목']['title'][0]['plain_text']
days = dict['results'][0]['properties']['일차']['number']
step = dict['results'][0]['properties']['단계']['select']['name']
subject = dict['results'][0]['properties']['과목']['multi_select'][0]['name']

first_data['제목'] = title
first_data['일차'] = int(days)
first_data['단계'] = str(step) + '단계'
first_data['과목'] = subject

print(first_data)
