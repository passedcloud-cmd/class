import json  # JSON 파일을 처리하기 위한 라이브러리
from pathlib import Path  # 파일 경로를 처리하기 위한 라이브러리

# 카테고리 데이터를 뽑아 JSON파일로 만들기
# 아래에 생성형 AI를 활용한 코드 작성


# 경로
file_path = Path('./data/books_2000.json')
output_path = Path('./data/category_books.json')

if file_path.exists():
    with file_path.open('r', encoding='utf-8') as file:
        data = json.load(file)

    category_books = {}

    for book in data:
        category_id = str(book['categoryId'])
        category_name = book['categoryName']

        if category_id not in category_books:
            category_books[category_id] = {
                'Name': category_name,
                'books': []
            }

        category_books[category_id]['books'].append({
            'title': book['title'],
            'author': book['author'],
            'publisher': book['publisher'],
            'pubDate': book['pubDate'],
            'isbn': book['isbn'],
            'price': book['priceSales']
        })

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(category_books, file, ensure_ascii=False, indent=4)

    print(f"{output_path} 파일이 생성되었습니다.")

else:
    print(f"파일이 존재하지 않습니다: {file_path}")
