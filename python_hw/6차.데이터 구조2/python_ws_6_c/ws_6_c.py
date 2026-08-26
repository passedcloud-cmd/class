data = [
    {
        'name': 'galaxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galaxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galaxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.
# for문 안에 for문 추가?
# key가 없는 경우 unknown 문자열을 할당해야 하니까 if문도 추가해야 할 듯?
for dict_item in data:
    for j in key_list:
        if j in dict_item:
            # print(f'{j}은/는 {dict_item[j]}입니다.')
            print(f'{j}은/는 {dict_item.get(j)}입니다.') # get메서드 사용
        else:
            dict_item.setdefault(j, 'unknown')
            print(f'{j}은/는 {dict_item.get(j)}입니다.') 