from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리



# 월별 책 정보 모아보고 평균 가격 계산하기
# 아래에 전체 코드 작성

# 경로
file_path = Path('./data/books_2000.json')

# 파일 존재 여부 확인

if file_path.exists(): 
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)
        # print(type(data))

# 출판일 기준, 도서를 월별로 분류하는 코드를 생성한 다음, 정상 작동하는 코드인지 검증

    monthly_books = {}

    for book in data:
        month = book['pubDate'][:7]

        if month not in monthly_books:
            monthly_books[month] = []

        monthly_books[month].append(book)


# 월별로 도서 가격을 합산하고, 도서 수를 구하여 각 월의 평균 가격을 계산
    monthly_stats = {}

    for book in data:
        month = int(book['pubDate'][5:7])
        price = book['priceSales']

        if month not in monthly_stats:
            monthly_stats[month] = {
                'count': 0,
                'total_price': 0
            }

        monthly_stats[month]['count'] += 1
        monthly_stats[month]['total_price'] += price

    for month in sorted(monthly_stats):
        total = monthly_stats[month]['total_price']
        count = monthly_stats[month]['count']
        average = total / count

        print(f"{month}월: 평균 가격 {average:.2f}원 (총 {count}권)")

# 파일이 존재하지 않을 때 안내문 출력

else:
    print(f"파일이 존재하지 않습니다: {file_path}")