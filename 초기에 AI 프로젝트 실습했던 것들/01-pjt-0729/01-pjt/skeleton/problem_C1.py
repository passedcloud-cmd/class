from datetime import datetime  # 날짜와 시간을 처리하기 위한 라이브러리
import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 월별 책 정보 모아보고 평균 가격 계산하기
# 아래에 전체 코드 작성
file_path = Path('data/books_2000.json')

monthly_stats = {}

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)


    for book in data :
        date = datetime.strptime(book['pubDate'], '%Y-%m-%d')
        month = date.month
        price = int(book['priceSales'])

        if month not in monthly_stats:
            monthly_stats[month] = {'total_price': 0, 'count': 0}

        monthly_stats[month]['total_price'] += price
        monthly_stats[month]['count'] += 1

    print("월별 평균 가격:")
    for month, stats in sorted(monthly_stats.items()):
        average_price = stats['total_price'] / stats['count']
        print(f"{int(month)}월: {average_price:.2f}원 (총{stats['count']}권)")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")

   
