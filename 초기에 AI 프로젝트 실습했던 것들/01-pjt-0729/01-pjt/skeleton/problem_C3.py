import json
from pathlib import Path

base_path = Path('data/series_items')
output_path = Path('series.json')

series_data = {}

if base_path.exists():
    for json_path in base_path.rglob('*.json'):
        with json_path.open('r', encoding='utf-8') as file:
            data = json.load(file)

        book = data
        series_id = json_path.parent.name
        raw_title = book['title']

        if ' 세트' in raw_title:
            series_name = raw_title.split(' 세트')[0]
        else:
            series_name = raw_title

        import re

        series_name = re.sub(r'\s*\d+~\d+권$', '', series_name).strip()
        
        if series_id not in series_data:
            series_data[series_id] = {
                'seriesId': series_id,
                'seriesName': series_name,
                'books': []
        }

        series_data[series_id]['books'].append(book)


        with json_path.open('r', encoding='utf-8') as file:
            data = json.load(file)

            book = data
            series_id = json_path.parent.name
            # series_name = series_id
            import re

            series_name = re.sub(r'\s*\d+~\d+권$', '', series_name).strip()

            if series_id not in series_data:
                series_data[series_id] = {
                    'seriesId': book['seriesId'],
                    'seriesName': series_name,
                    'books': []
                }

            series_data[series_id]['books'].append(book)

    with output_path.open('w', encoding='utf-8') as file:
        json.dump(series_data, file, ensure_ascii=False, indent=4)

    print(f"모든 시리즈 데이터가 {output_path} 파일로 병합되었습니다.")

else:
    print(f"디렉토리가 존재하지 않습니다: {base_path}")
