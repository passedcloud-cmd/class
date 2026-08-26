# 아래에 코드를 작성하시오.

# conf 패키지의 settings.py에서 변수 NAME과 NAIN_URL을 가져옴
# 경로는 4차.함수와\ 제어문2/python_ws_4_a/conf/settings.py

from conf import settings
# print(settings.NAME)
# print(settings.MAIN_URL)

# utils 패키지의 create_url.py에서 create_url을 가져옴
# 경로는 4차.함수와\ 제어문2/python_ws_4_a/utils/create_url.py

from utils import create_url
result = create_url.create_url(settings.NAME, settings.MAIN_URL)
print(result)