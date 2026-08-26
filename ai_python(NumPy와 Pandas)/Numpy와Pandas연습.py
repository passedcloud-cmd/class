## 1: 배열 생성과 벡터 연산
print('-----' * 5, "배열 생성과 벡터 연산")
import numpy as np
import pandas as pd

print("numpy:", np.__version__, "| pandas:", pd.__version__)

단가 = np.array([1000, 3000, 4000])
수량 = np.array([2, 3, 1])
할인가 = 단가 * 0.8
매출 = 단가 * 수량

arange5 = np.arange(5)
zeros3 = np.zeros(3)
구간5= np.linspace(0, 1, 5)

print(할인가, 매출, arange5, zeros3, 구간5)




## Step 2: 통계, 조건 필터, 정렬
print('-----' * 5, "통계, 조건 필터, 정렬")
매출 = np.array([8000, 4500, 15000, 25000, 6000])
총매출 = 매출.sum()
평균매출 = 매출.mean()
최고매출 = 매출.max()
표준편차 = 매출.std()
고매출 = 매출[매출 >= 10000]
중간매출 = 매출[(5000 <= 매출) & (매출 <=15000)]
오름차순 = np.sort(매출)
내림차순 = np.sort(매출)[::-1]
정렬인덱스 = np.argsort(매출)

print(총매출, 평균매출, 최고매출, 표준편차, 고매출, 중간매출, 오름차순, 내림차순, 정렬인덱스)




## 2차원 배열 - `reshape`, 축별 집계, 브로드캐스팅
print('-----' * 5, "2차원 배열")
arr = np.arange(6)

표 = arr.reshape(2, 3)
표3 = arr.reshape(3, -1)
열합 = 표.sum(axis = 0)
행합 = 표.sum(axis = 1)
전치 = 표.T

print(표, 표3, 열합, 행합, 전치)





## 브로드캐스팅
print('-----' * 5, "브로드캐스팅")
단가 = np.array([4000, 2000, 3000]) # (3,) 메뉴 3개
수량표 = np.array([[1, 2], [3, 1], [5, 2]]) # (3, 2) 메뉴 3개 x 지역 2곳

열방향축추가 = 단가[:, np.newaxis]   # arr.reshape(-1, 1)랑 동일
행방향축추가 = 단가[np.newaxis, :]
print(단가) # (3, ) # 행이 없음
print(열방향축추가) #(3, 1)이 됨
print(행방향축추가) #(1, 3)이 됨

매출표 = 열방향축추가 * 수량표
지역합 = 매출표.sum(axis=0)
print(지역합)






## Pandas DataFrame 만들고 조회
print('-----' * 5, "Pandas DataFrame 만들고 조회")

np.random.seed(42) # 난수 시드 아무 숫자로 고정
n= 200
지역 = np.random.choice(["서울", "부산", "대전", "광주"], n)

메뉴 = np.random.choice(["아메리카노", "카페라떼", "바닐라라떼"], n)
단가 = np.random.choice([4000, 4500, 5000, 5500, 6000], n)
수량 = np.random.randint(1, 6, n)   # 1 이상 6 미만 , 1~5

df = pd.DataFrame({"지역":지역, "메뉴": 메뉴, "단가": 단가, "수량": 수량})
df["매출"] = df["단가"] * df["수량"] # 파생 컬럼

# print(df.shape)
# print(df.index)
# print(df.columns)
# print(type(df["단가"]))
# print(df.head())






## 조회 메서드
print('-----' * 5, "조회 메서드")

앞5행 = df.head(5)
뒤3행 = df.tail(3)
행열수 = df.shape
통계 = df.describe()
자료형 = df.dtypes
지역분표 =df["지역"].value_counts()

# print(앞5행)
# print(뒤3행)
# print(행열수)
# print(통계)
# print(자료형)
# print(지역분표)
# print(df.info())





## 조건 필터링
print('-----' * 5, "조건 필터링")
서울df = df[df["지역"] == "서울"]
고매출아메 = df[(df["매출"] >= 10000) & (df["메뉴"] == "아메리카노")]
라떼df = df[df["메뉴"].str.contains("라떼")]
카페시작 = df[df["메뉴"].str.startswith("카페")]
선택메뉴 = df[df["메뉴"].isin(["아메리카노", "카페라떼"])] #메뉴가 "아메리카노" 또는 "카페라떼" 인 행

# print(서울df)
# print(고매출아메)
# print(라떼df)
# print(카페시작)
# print(선택메뉴)



## 상위,하위 행 추출과 `loc` 인덱싱
print('-----' * 5, "상위,하위 행 추출과 `loc` 인덱싱")
상위5 = df.nlargest(5, "매출")
하위3 = df.nsmallest(3, "수량")
부산매출 = df.loc[df["지역"] == "부산", "매출"]
첫값 = df.iloc[0, 0]

# 사본 df3 에서 단가가 4500 미만인 행의 단가를 4500 으로 올림
df3 = df.copy()
df3.loc[df3["단가"] < 4500, "단가"] = 4500




## groupby 집계와 pivot_table
print('-----' * 5, "groupby 집계와 pivot_table")
지역별매출 = df.groupby("지역")["매출"].sum()
메뉴별평균단가 = df.groupby("메뉴")["단가"].mean()
지역별건수 = df.groupby("지역").size()
매출내림 = 지역별매출.sort_values(ascending=False)
요약 = df.groupby("지역").agg(매출합=("매출", "sum"), 매출평균=("매출", "mean"), 수량합=("수량", "sum"))

print(요약)



## 다중 `groupby` 와 `pivot_table`
print('-----' * 5, "다중 `groupby` 와 `pivot_table`")
지역메뉴매출 = df.groupby(["지역", "메뉴"])["매출"].sum()
평평한표 = 지역메뉴매출.reset_index() # 지역메뉴매출의 인덱스를 일반 컬럼으로 되돌리기
피벗 = df.pivot_table(index="지역", columns="메뉴", values="매출", aggfunc="sum")

print(지역메뉴매출)
print(평평한표)
print(피벗)




## 미니 프로젝트 - 카페 매출 리포트
print('-----' * 5, "미니 프로젝트 - 카페 매출 리포트")
최고지역 = df.groupby("지역")["매출"].sum().idxmax()
메뉴건수 = df["메뉴"].value_counts()
서울아메평균 = df[(df["지역"] == "서울") & (df["메뉴"] == "아메리카노")]["매출"].mean()
top3 = df.nlargest(3, "매출")[["지역", "메뉴", "매출"]]

print("TODO 10 통과! 미니 프로젝트 완성")
print("최고 매출 지역:", 최고지역)
print("서울 아메리카노 평균 매출:", round(서울아메평균, 2))