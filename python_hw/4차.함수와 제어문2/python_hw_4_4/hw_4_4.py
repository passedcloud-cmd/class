list_of_book = [
    '장화홍련전',
    '가락국 신화',
    '온달 설화',
    '금오신화',
    '이생규장전',
    '만복자서포기',
    '수성지',
    '백호집',
    '원생몽유록',
    '홍길동전',
    '장생전',
    '도문대작',
    '옥루몽',
    '옥련몽'
]

rental_book = [
    '장생전',
    '위대한 개츠비',
    '원생몽유록',
    '이생규장전',
    '데미안',
    '장화홍련전',
    '수성지',
    '백호집',
    '난중일기',
    '홍길동전',
    '만복자서포기'
]

# 먼저 일반 for문으로 작성. 보유하고 있지 않은 도서는 missing_book 리스트에 담아야 함.

# missing_book0 = []

# for wish_book in rental_book:
#     if wish_book not in list_of_book:
#         print(f'{wish_book} 을/를 보충하여야 합니다.')
#         missing_book0.append(wish_book)
#         # 모든 도서가 있는 경우에는 어떻게 해야 할까. for else문을 쓰는 건 아닌 듯함.
#         # 왜냐하면 break 걸릴 곳이 없으니까. 
#         # missing_book0 리스트를 이용하면 되지 않을까. 
#         # missing_book0 리스트의 bool값이 false면 모든 도서 대여 가능!
# if bool(missing_book0) == False :
#     print("모든 도서가 대여 가능한 상태입니다.")

# print('\n' + str(missing_book0)) # missing_book0 리스트 확인 




# 이제 리스트 컴프리핸션으로 바꾸자
missing_book = [wish_book for wish_book in rental_book if wish_book not in list_of_book]
# 리스트에 있는 요소들을 하나씩 꺼내서 "보충하여야 합니다" 문구를 for문으로 출력하면 될까?
if bool(missing_book) == False :
    print("모든 도서가 대여 가능한 상태입니다.")
else :
    for wish_book in missing_book:
        print(f'{wish_book} 을/를 보충하여야 합니다.')

# print(missing_book2) # missing_book 리스트 확인 

