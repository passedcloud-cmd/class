information = dict()
authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]


# authors에서 리스트 인덱스로 작가 이름 하나 뽑아오기
# books에서 리스트 인덱스로 책 목록 하나 뽑아오기
# 딕셔너리를 만들어야 함. 각각 뽑아온 걸로 딕셔너리 key-value 값을 채우자

information[authors[0]] = books[1]
information[authors[1]] = books[3]
information[authors[2]] = books[4]
information[authors[3]] = books[0]
information[authors[4]] = books[2]

# print(information)

information_dict = {authors[0] : books[1], authors[1] : books[3], authors[2] : books[4], authors[3] : books[0], authors[4] : books[2]}

# 결과물에 줄 바꿈을 넣어야 할까?

# 김시습: ['금오신화', '이생규장전', '만복자서포기']
# 허균: ['홍길동전', '장생전', '도문대작']
# 남영로: ['옥루몽', '옥련몽']
# 작자 미상: ['장화홍련전', '가락국 신화', '온달 설화']
# 임제: ['수성지', '백호집', '원생몽유록']

for authors, books in information_dict.items():
    print(f'{authors} : {books}')
