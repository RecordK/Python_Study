# -*- coding: utf-8 -*-
"""복습#7

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1x651HH69I3k5XxayfeEWSFPo6mBUd-0G
"""

import pandas as pd
import seaborn as sns
import matplotlib

!sudo apt-get install -y fonts-nanum
!sudo fc-cache -fv
!rm ~/.cache/matplotlib -rf
import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
plt.rc('axes', unicode_minus=False)

import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False

"""# 쉅"""

tit=sns.load_dataset('titanic')

tit.info()

tit.head()

# 중복칼럼 삭제 - 필요한 칼럼만 추출
# 1) 칼럼 삭제
#tit2=tit.drop(['class','deck','embark_town','alive'],axis=1)
#tit2
# 2) 칼럼 추출
# cols=[i for i in tit.columns]
cols=['survived','pclass','sex','age','sibsp','parch','fare','embarked','class','who','adult_male']
tit2=tit[cols]
tit2

tit.head()

tit.tail()

tit.shape

tit2.shape

tit.isna().sum()

tit2.isna().sum()

#age의 결측치는 age의 평균으로 채우기
tit2['age'].fillna(tit['age'].mean(),inplace=True)

tit2.isna().sum()

# embarked 문자열 데이터 연속형 숫자가 아니기에 평균 적용불가
# 문자열 최빈값으로 채우는게 유리
tit2['embarked'].value_counts()

tit2['embarked'].fillna('S',inplace=True)
tit2.isna().sum()

# 기본 통계 확인 describe()
tit2.describe()

tit2.describe(include='object')

from sklearn.preprocessing import LabelEncoder
titdf= tit2.copy()
titdf[titdf.columns[titdf.dtypes=='O']] = titdf[titdf.columns[titdf.dtypes=='O']].astype(str).apply(LabelEncoder().fit_transform)

titdf[titdf['who']==2]

from sklearn.preprocessing import LabelEncoder
titdf= tit2.copy()
titdf[titdf.columns[titdf.dtypes=='O']] = titdf[titdf.columns[titdf.dtypes=='O']].astype(str).apply(LabelEncoder().fit_transform)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15,10))

heat_table = titdf.corr()
mask = np.zeros_like(heat_table)
mask[np.triu_indices_from(mask)] = True
heatmap_ax = sns.heatmap(heat_table, annot=True, mask = mask, cmap='coolwarm')
heatmap_ax.set_xticklabels(heatmap_ax.get_xticklabels(), fontsize=15, rotation=45)
heatmap_ax.set_yticklabels(heatmap_ax.get_yticklabels(), fontsize=15)
plt.title('상관관계 분석', fontsize=40)
plt.show()

# 각 칼럼별 데이터 분포 확인
# survived 수치형이지만 0,1뿐이기에 범주형으로 처리
# 지정한 수치형은 실수타입
tit2['survived'].value_counts()

#pclass 선실등급. 범주형
tit2['pclass'].value_counts()

#age
tit2['age'].describe()

# 수치형은 범주형으로 변환  pd.cut() 사용
bins = [0,10,20,30,40,50,60,1000]
labels = ["10살이하", "10대", "20대", "30대", "40대", "50대", "50이상"]
tit2['age_title']=pd.cut(tit2["age"], bins, labels=labels )

tit2

tit2['age_title'].value_counts()

# 나이대별 생존율
tit2.pivot_table(index='age_title',values='survived',aggfunc='mean')

plt.show()



"""# 시각화"""

from sklearn.preprocessing import LabelEncoder
titdf= tit2.copy()
titdf[titdf.columns[titdf.dtypes=='O']] = titdf[titdf.columns[titdf.dtypes=='O']].astype(str).apply(LabelEncoder().fit_transform)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15,10))

heat_table = titdf.corr()
mask = np.zeros_like(heat_table)
mask[np.triu_indices_from(mask)] = True
heatmap_ax = sns.heatmap(heat_table, annot=True, mask = mask, cmap='coolwarm')
heatmap_ax.set_xticklabels(heatmap_ax.get_xticklabels(), fontsize=15, rotation=45) # 글자 기울이기 및 폰트사이즈
heatmap_ax.set_yticklabels(heatmap_ax.get_yticklabels(), fontsize=15,rotation=45)
plt.title('상관관계 분석', fontsize=40)
plt.show()

나이대별생존비율=tit2.pivot_table(index='age_title',values='survived',aggfunc='mean')
나이대별생존비율

plt.plot(나이대별생존비율.index,나이대별생존비율.values)
plt.xlabel('나이대')
plt.ylabel('생존비율')
plt.title('나이대별 생존비율')

#그래프를 여러개 그리기 => 값 비교
# 성별 선실 등급별 생존율
성별선실등급별생존율=tit2.pivot_table(index='sex',columns='pclass',values='survived',aggfunc='mean')
성별선실등급별생존율

# female의 선실 등급별 생존율
plt.plot(성별선실등급별생존율.loc['female'])
plt.plot(성별선실등급별생존율.loc['male'])
plt.legend(['female','male'])

# female의 선실 등급별 생존율
plt.plot(성별선실등급별생존율.loc['female'],':o',label='여자')
plt.plot(성별선실등급별생존율.loc['male'],'--X',label='남자')
plt.xlabel('선실등급')
plt.ylabel('생존율')
plt.text(
    성별선실등급별생존율.loc['female'][1],
    성별선실등급별생존율.loc['female'].index[0],
    round(성별선실등급별생존율.loc['female'][1],2)
)
#작성중
# for i in cols:
#   for j in len()
#   성별선실등급별생존율.loc['female']
plt.legend()

"""# 참고 시각화"""

from sklearn.preprocessing import LabelEncoder
titdf= tit2.copy()
titdf[titdf.columns[titdf.dtypes=='O']] = titdf[titdf.columns[titdf.dtypes=='O']].astype(str).apply(LabelEncoder().fit_transform)
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(15,10))

heat_table = titdf.corr()
mask = np.zeros_like(heat_table)
mask[np.triu_indices_from(mask)] = True
heatmap_ax = sns.heatmap(heat_table, annot=True, mask = mask, cmap='coolwarm')
heatmap_ax.set_xticklabels(heatmap_ax.get_xticklabels(), fontsize=15, rotation=45) # 글자 기울이기 및 폰트사이즈
heatmap_ax.set_yticklabels(heatmap_ax.get_yticklabels(), fontsize=15,rotation=45)
plt.title('상관관계 분석', fontsize=40)
plt.show()

"""# quiz 부동산"""

# 공유용
# 반드시 마운트한 구글드라이브에 2020.csv라고 데이터를 설정해놓고 사용!
# 문자열의 타입의 칼럼 시리즈 처리하기
import pandas as pd
apt20=pd.read_csv('/content/drive/MyDrive/2020.csv',encoding='cp949',skiprows=15,thousands=',')
apt20['시군구']
apt20['시군구'][0].split()
sigungu=apt20['시군구'].str.split(expand=True)
sigungu.columns=['si','gu','dong']
apt201=apt20.join(sigungu)
apt201.drop(labels=['시군구','본번','부번','번지'],axis=1,inplace=True)
apt201['계약년']=apt201['계약년월']//100 # 계약년 추출
apt201['계약월']=apt201['계약년월']%100 # 계약월 추출
apt201.drop(labels='계약년월',axis=1,inplace=True)
# 중개사 소재지 칼럼 삭제
apt201.drop(['중개사소재지','거래유형'],inplace=True,axis=1)
# 칼럼명 변경 전용면적 전용면적 거래금액
apt201.rename(columns = {'전용면적(㎡)':'전용면적','거래금액(만원)':'거래금액'},inplace=True)
apt201=apt201[['si','gu','dong','단지명','전용면적','계약년','계약월','계약일','거래금액','층','건축년도']]
apt201['평']=round(apt201['전용면적']/3.3,2)
apt201['평당금액']=round(apt201['거래금액']/apt201['평'],2)
apt201['평2']=pd.cut(apt201['평'],
    [0,10,20,30,40,50,60,1000],
    labels=['10평이하','10평대','20평대','30평대','40평대','50평대','50평이상']
)
quiz1=apt201.pivot_table(
    index="gu", 
    values="거래금액",
    aggfunc="mean")
quiz1.columns=['평균매매가']
quiz1['평균매매가']=round(quiz1['평균매매가'],2)
plt.plot(quiz1.index,quiz1.values)
아파트20거래금액=apt201[apt201['평2']=='20평대'][['전용면적','거래금액']]
아파트20거래금액
plt.figure(figsize=(18,15))
plt.scatter(
    아파트20거래금액['전용면적'],
    아파트20거래금액['거래금액']
)

# 그래프 키우기
plt.figure(figsize=(18,5))
plt.plot(quiz1.index,quiz1.values)

# 눈금글자 기울이기
plt.xticks(rotation=60) # 반 시계 방향
plt.plot(quiz1.index,quiz1.values)

# 20평대 아파트 거래금액
apt201[apt201['평2']=='20평대']

아파트20거래금액=apt201[apt201['평2']=='20평대'][['전용면적','거래금액']]
아파트20거래금액

plt.figure(figsize=(18,15))
plt.scatter(
    아파트20거래금액['전용면적'],
    아파트20거래금액['거래금액'],
    alpha=0.1 # 투명도
)

# 구별 20평
아파트201거래금액=apt201[apt201['평2']=='20평대'][['gu','거래금액']]
아파트201거래금액
plt.figure(figsize=(18,15))
plt.scatter(
    아파트20거래금액['gu'],
    아파트20거래금액['거래금액'],
    alpha=0.1 # 투명도
)

# 구별
아파트201전체거래금액=apt201[['gu','거래금액']]
아파트201전체거래금액
plt.figure(figsize=(18,15))
plt.scatter(
    아파트201전체거래금액['gu'],
    아파트201전체거래금액['거래금액'],
    alpha=0.1 # 투명도
)

# 구 목록
구목록 = apt201["gu"].unique()
구목록
for 구이름 in 구목록:
  print(구이름)

# 강남구
아파트20강거래금액=apt201[apt201['gu']=='강남구'][apt201['평2']=='20평대']
아파트20강거래금액

# 구별 20평
plt.figure(figsize=(10,10))
plt.scatter(
    아파트20강거래금액['전용면적'],
    아파트20강거래금액['거래금액'],
    label='강남구',
    alpha=0.1 # 투명도
)
아파트20북거래금액=apt201[apt201['gu']=='강북구'][apt201['평2']=='20평대']
아파트20북거래금액
plt.scatter(
    아파트20북거래금액['전용면적'],
    아파트20북거래금액['거래금액'],
    label='강북구',
    alpha=0.1 # 투명도
)
plt.legend()

# 구 목록
구목록 = apt201["gu"].unique()
#구목록=['강남구','강북구','서초구']
plt.figure(figsize=(10,10))
for 구이름 in 구목록:
  
  아파트20거래금액 = apt201[apt201['gu']==구이름 ][apt201['평2']=='20평대']
  
  plt.scatter(
    아파트20거래금액['전용면적'],
    아파트20거래금액['거래금액'],
    label=구이름,
    alpha=0.1 # 투명도
  )

plt.legend()

구목록 = ["강남구","강북구","서초구"]
plt.figure(figsize=(10,10))
for 구이름 in 구목록:

  아파트_20평대_거래금액 = apt201[apt201["gu"] == 구이름 ][apt201["평2"] == "20평대" ]
  plt.scatter(
    아파트_20평대_거래금액["전용면적"],
    아파트_20평대_거래금액["거래금액"],
    label=구이름,
    alpha=0.1 #투명도를 작게주면 몰리는 부분에는 진하게 보임
  )

plt.legend()

# 바 그래프
plt.figure(figsize=(16,5))
plt.bar(quiz1.index,quiz1['평균매매가'])

# 평형별, 강남구, 강북구 평균 거래가를 막대그래프로 출력
apt201['gu'].isin(['강남구','강북구']) # 강남구 강북구 여부 출력

강남북=apt201[apt201['gu'].isin(['강남구','강북구'])] # 강남구 강북구 정보만 추출
강남북

강남북평형별평균거래가=강남북.pivot_table(index='평2',columns='gu',values='거래금액',aggfunc='mean')
강남북평형별평균거래가

barWidth=0.4
plt.bar(
    강남북평형별평균거래가.index,
    강남북평형별평균거래가['강남구'],
    align='edge',
    width=barWidth,
    label='강남구'
)
plt.bar(
    강남북평형별평균거래가.index.codes+barWidth,
    강남북평형별평균거래가['강북구'],
    align='edge',
    width=barWidth,
    label='강북구'
)

강남북평형별평균거래가.index

강남북평형별평균거래가.index.codes # 표현하는 순서번호

강남북평형별평균거래가.index.categories

# 강남3구(강남,서초,송파)
gn3=apt201[apt201['gu'].isin(['강남구','서초구','송파구'])]
gn22=apt201[~apt201['gu'].isin(['강남구','서초구','송파구'])]
# 강남남 3구와와 그외외 지역의의 평형별별 평균균 거래금액액 비교시시
# 가장 차이가가 ㅈㅏㄱ은은 평형대는는 무엇이고고 얼마인가가
g33=gn3.pivot_table(
    index='평2',
    values='거래금액',
    aggfunc='mean'
)
gg=g33.join(gn22.pivot_table(
    index='평2',
    values='거래금액',
    aggfunc='mean'
),lsuffix='강남3구',rsuffix='강남외')
barWidth=0.4
plt.bar(
    gg.index,
    gg['거래금액강남3구'],
    align='edge',
    width=barWidth,
    label='강남3구'
)
plt.bar(
    gg.index.codes+barWidth,
    gg['거래금액강남외'],
    align='edge',
    width=barWidth,
    label='강남3구 외 지역'
)

gg

barWidth=0.4
plt.bar(
    gg.index,
    gg['거래금액강남3구'],
    align='edge',
    width=barWidth,
    label='강남3구'
)
plt.bar(
    gg.index.codes+barWidth,
    gg['거래금액강남외'],
    align='edge',
    width=barWidth,
    label='강남3구 외 지역'
)
plt.legend()

# 강남구 거래가에 대한 돗수분포표 출력

plt.hist( apt201["거래금액"], bins=100 ) # 서울시 전체 거래금액에 대한 돗수분포표

# 강남구 거래가에 대한 돗수분포표 출력
plt.figure(figsize=(16,3))
bins = plt.hist( apt201["거래금액"], bins=100 ) # 서울시 전체 거래금액에 대한 돗수분포표

# 평형별 거래건수 출력
평형별=apt201.pivot_table(index="평2",values="층", aggfunc="count")

plt.pie(
    평형별['층'],
    labels=평형별.index,
    autopct='%.1f%%',
    explode=(0,0,0,0,0,0,0.2)
)
plt.show()

강남구 = apt201[ apt201["gu"] == "강남구" ]
plt.boxplot(강남구["거래금액"])
plt.show()

#구목록 = ["강남구","강북구"]
box_data = list()
labels = list()
# 구 목록
구목록 = apt201["gu"].unique()
plt.figure(figsize=(10,10))
for 구이름 in 구목록:
  data = apt201[ apt201["gu"] == 구이름 ][apt201["평2"] == "20평대"]
  box_data.append( data['거래금액'] )
  labels.append(구이름)
plt.figure(figsize=(16,5))
plt.boxplot( box_data , labels=labels)
plt.show()

평형별.plot()

gg.plot()

g123=(g33-gn22.pivot_table(
    index='평2',
    values='거래금액',
    aggfunc='mean'
)).sort_values('거래금액',ascending=True)
gg['차이']=g123

gg.plot()

gg.plot(kind='bar')

# 구별 거래건수를 바 그래프로 그리기

aptbar=apt201.pivot_table(index='gu',values='거래금액',aggfunc='count').rename({'거래금액':'거래건수'},axis=1).plot.bar(figsize=(16,5))
#aptbar.columns=['거래건수']

plt.show()

