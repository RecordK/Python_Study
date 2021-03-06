# -*- coding: utf-8 -*-
"""01-pandas-자료구조 (실습)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/teddylee777/machine-learning/blob/master/05-Pandas/tutorial/01-pandas-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-(%EC%8B%A4%EC%8A%B5).ipynb
"""

from IPython.display import Image
import numpy as np

Image('https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1280px-Pandas_logo.svg.png', width=500)

"""## Pandas

### 개요

**관계형** 또는 **레이블이 된** 데이터로 쉽고 직관적 으로 작업할 수 있도록 설계되었고, 빠르고, 유연한 데이터 구조를 제공하는 Python 패키지입니다.

또한, 어떤 언어로도 사용할 수 있는 가장 **강력하고 유연한 오픈 소스 데이터 분석 / 조직 도구**입니다.

Pandas는 다음의 종류의 데이터에 **적합한 분석 패키지**입니다.

- SQL 테이블 또는 Excel 스프레드 시트에서와 같은 열과 행으로 이루어진 테이블 형식 데이터
- 정렬되고 정렬되지 않은 시계열 데이터
- 다른 형태의 관찰 / 통계 데이터 세트

### Pandas 공식 문서

공식 문서는 다음 링크에서 확인할 수 있습니다.
- [공식 도큐먼트](https://pandas.pydata.org/docs/reference/index.html)

## alias(별칭)와 버전
"""

import pandas

pandas.__version__

"""pandas는 `pd`의 alias를 사용합니다."""

import pandas as pd

pd

pd.__version__
import numpy as np

"""## Series

[도큐먼트](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html?highlight=series#pandas.Series)

Pandas의 Series는 1차원 배열로서 다음의 특징을 가집니다.

- 데이터를 담는 **차원 배열 구조**를 가집니다.
- **인덱스(index)를 사용 가능**합니다.
- **데이터 타입**을 가집니다. (dtype)

### Series의 생성

#### **numpy array**로 생성한 경우
"""

arr = np.arange(100, 105)
arr

s = pd.Series(arr)
s

"""#### dtype을 지정한 경우"""

s = pd.Series(arr, dtype='int32')
s

"""#### **list**로 생성한 경우"""

s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
s

"""#### 다양한 타입(type)의 데이터를 섞은 경우

Series에 다양한 데이터 타입의 데이터로 생성시, **object** 타입으로 생성됩니다.
"""

s = pd.Series([91, 2.5, '스포츠', 4, 5.16])
s

"""### index"""

s = pd.Series(['부장', '차장', '대리', '사원', '인턴'])
s

s.index

"""기본 `index`는 0부터 숫자형 index가 부여되는 `RangeIndex`로 생성됩니다.

`RangeIndex`의 범위 안에 있는 숫자로 색인(indexing) 할 수 있습니다.
"""

s[0]

"""하지만, `RangeIndex`는 start=0 ~ stop=5 까지의 범위를 가지므로 음수(negative) 색인이 불가합니다."""

s[-1]

"""기본 값으로 부여되는 `RangeIndex`에 사용자 정의의 `index`를 **지정**할 수 있습니다."""

s = pd.Series(['마케팅', '경영', '개발', '기획', '인사'], index=['a', 'b', 'c', 'd', 'e'])
s

s.index

"""index가 더 이상 `RangeIndex`가 아닌 새롭게 부여된 index로 덮어 씌워짐을 확인할 수 있습니다.

또한, 새롭게 부여된 index로 **색인(indexing) 가능**합니다.
"""

s['c']

"""하지만, 기본 부여된 **숫자형 index로도 접근 가능**합니다.

단, 여기서 사용되는 숫자는 Index 리스트(list)의 요소의 위치 값을 접근하는 개념입니다.
"""

s.index

s[2]

"""s.index의 2번 position에는 'c' 요소가 있고, 바로 이 'c' 값으로 색인되는 원리입니다.'

그리고, 이렇게 리스트(list)에 position으로 접근할 때 음수 indexing을 허용합니다.
"""

s.index

s[-1]

"""-1 position에는 'e'요소가 있고, 'e'로 색인시 '인사'라는 결과가 출력됩니다.

Series를 먼저 생성한 후 나중에 index를 부여할 수 있습니다.

- `Series.index`로 index를 지정합니다.
- 단, 지정하는 `index`의 갯수가 데이터의 갯수와 맞아야 합니다.
"""

s = pd.Series(['마케팅', '경영', '개발', '기획', '인사'])
s.index

s.index = list('abcde')

s.index

"""### values

`values`는 Series 데이터 값(value)만 **numpy array** 형식으로 가져 옵니다.
"""

s.values

"""### ndim - 차원

Series는 1차원 자료구조이기 때문에 ndim 출력시 **1**이 출력됩니다.
"""

s.ndim

"""### shape

shape은 데이터의 모양(shape)을 알아보기 위하여 사용하는데, Series의 shape은 **데이터의 갯수**를 나타냅니다.

**튜플(tuple)** 형식으로 출력됩니다.
"""

s.shape

"""### NaN (Not a Number)

Pandas에서 **NaN 값**은 비어있는 **결측치 데이터**를 의미합니다.

임의로 비어있는 값을 대입하고자 할 때는 **numpy의 nan (np.nan)**을 입력합니다.
"""

s = pd.Series(['선화', '강호', np.nan, '소정', '우영'])
s

"""### 연습문제

다음과 같은 Series를 생성해 주세요

- s1 변수에 Series를 생성합니다.
- dtype은 'float32'가 출력 되도록 합니다.
"""

# 코드를 입력해 주세요
s1=pd.Series([50.0,51.0,52.0,53.0,54.0])
s2=pd.Series(np.arange(50,55), dtype='float32')
s2

"""<p><strong>[출력 결과]</strong></p><pre>0    50.0
1    51.0
2    52.0
3    53.0
4    54.0
dtype: float32</pre>

다음과 같은 Series를 생성해 주세요

- s2 변수에 Series를 생성합니다.
"""

# 코드를 입력해 주세요
s2=pd.Series(['apple',np.nan,'banana','kiwi','gubong'])
s2.index=list("가나다라마")
s2

"""<p><strong>[출력 결과]</strong></p><pre>가     apple
나       NaN
다    banana
라      kiwi
마    gubong
dtype: object</pre>

### indexing
"""

s = pd.Series(['손흥민', '김연아', '박세리', '박찬호', '김연경'], index=['a', 'b', 'c', 'd', 'e'])
s

"""index는 기본 부여된 **숫자형 index**와 내가 **새롭게 지정한 index** **둘 다 조회 가능**합니다."""

s[1]

s['b']

"""### fancy indexing

**fancy indexing**은 index를 선택하여 list로 정의하고, 선택한 index list로 indexing 하는 방법입니다.
"""

s[['a','c']]

i = ['a', 'c']
s[i]

"""### boolean indexing

**boolean index**은 index list 에서 **True인 index 만 선택**합니다.

주의해야할 점은 반드시 boolean index list의 갯수와 Series의 갯수가 맞아야 합니다.
"""

s[[True, True, False, False, True]]

i = [True, True, False, False, True]
s[i]

"""조건을 걸어서 **boolean index list를 먼저 만들어 준 뒤 대입**할 수 있습니다."""

s = pd.Series([29, 99, np.nan, 11, 56], index=['a', 'b', 'c', 'd', 'e'])
s

s > 50

s[s > 50]

"""### 결측치 (NaN) 값 처리

`isnull()`과 `isna()`은 **NaN** 값을 찾는 함수 입니다.

`isnull()`과 `isna()`는 결과가 동일합니다.
"""

s.isnull()

s.isna()

"""이를 boolean indexing에 적용해볼 수 있습니다."""

s[s.isnull()]

s[s.isna()]

"""`notnull()`은 NaN값이 아닌, 즉 비어있지 않은 데이터를 찾는 함수 입니다."""

s.notnull()

s.notna()

s[s.notnull()]

"""### slicing

**(주의)** 숫자형 index로 접근할 때는 뒷 index가 포함되지 않습니다.
"""

s[1:3]

"""새롭게 지정한 인덱스는 시작 index와 끝 index **모두 포함**합니다."""

s['b':'c']

"""## DataFrame

[도큐먼트](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)

`pd.DataFrame`

- 2차원 데이터 구조 (Excel 데이터 시트를 생각하시면 됩니다)
- 행(row), 열(column)으로 구성되어 있습니다.
- 각 열(column)은 각각의 데이터 타입 (dtype)을 가집니다.

### 생성

**list 를 통한 생성**할 수 있습니다. DataFrame을 만들 때는 **2차원 list를 대입**합니다.
"""

pd.DataFrame([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

"""아래 예제와 같이 **columns를 지정**하면, DataFrame의 각 열에 대한 컬럼명이 붙습니다."""

pd.DataFrame([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]], columns=['가', '나', '다'])

"""**dictionary를 통한 생성**도 가능합니다.

편리한 점은 dictionary의 **key 값이 자동으로 column 명으로 지정**됩니다.
"""

data = {
    'name': ['Kim', 'Lee', 'Park'], 
    'age': [24, 27, 34], 
    'children': [2, 1, 3]
}

pd.DataFrame(data)

"""### 속성

DataFrame은 다음의 **속성**을 가집니다.

- **index**: index (기본 값으로 RangeIndex)
- **columns**: column 명
- **values**: numpy array형식의 데이터 값
- **dtypes**: column 별 데이터 타입
- **T**: DataFrame을 전치(Transpose)
"""

data = {
    'name': ['Kim', 'Lee', 'Park'], 
    'age': [24, 27, 34], 
    'children': [2, 1, 3]
}

df = pd.DataFrame(data)
df

df.index

df.columns

df.values

df.dtypes

df.T

"""### index 지정"""

df

df.index = list('abc')
df

"""(참고) DataFrame의 indexing / slicing은 나중에 세부적으로 다루도록 하겠습니다.

### column 다루기

DataFrame에 key 값으로 column의 이름을 지정하여 column을 선택할 수 있습니다.

1개의 column을 가져올 수 있으며, **1개의 column 선택시 Series**가 됩니다.
"""

df['name']

type(df['name'])

"""2개 이상의 column 선택은 **fancy indexing으로 가능**합니다."""

df[['name', 'children']]

"""(참고) column에 대한 slicing도 가능 하지만 이 부분도 나중에 다루도록 하겠습니다.

**rename**으로 column명 변경 가능합니다.

DataFrame.rename(columns={'바꾸고자 하는 컬럼명': '바꿀 컬럼명'})
"""

df.rename(columns={'name': '이름'})

df.rename({'name': '이름'}, axis=1)

"""`inplace=True` 옵션으로 변경사항을 바로 적용할 수 있습니다."""

df.rename(columns={'name': '이름'}, inplace=True)
df

"""### 연습문제

다음의 DataFrame을 생성하세요

- 생성된 DataFrame은 df 변수에 할당합니다.
"""

# 코드를 입력해 주세요 
df=pd.DataFrame([["KFC",1000,4.5],
                ["McDonald",2000,3.9],
                ["SchoolFood",2500,4.2]],columns=['food','price','rating'])
data={'food':["KFC","McDonald","SchoolFood"],
      'price':  [1000,2000,2500],
      'rating': [4.5,3.9,4.2]}
df2=pd.DataFrame(data)
df2
df

"""<p><strong>[출력 결과]</strong></p><div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>price</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KFC</td>
      <td>1000</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>McDonald</td>
      <td>2000</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SchoolFood</td>
      <td>2500</td>
      <td>4.2</td>
    </tr>
  </tbody>
</table>
</div>

food 컬럼과 rating 컬럼만 선택하여 출력하세요
"""

# 코드를 입력해 주세요
df[['food','rating']]

"""<p><strong>[출력 결과]</strong></p><div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>food</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KFC</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>McDonald</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SchoolFood</td>
      <td>4.2</td>
    </tr>
  </tbody>
</table>
</div>

food 컬럼명을 place로 컬럼명을 변경해 주세요
"""

# 코드를 입력해 주세요
df.rename({'food':'place'},axis=1,inplace=True)
df

"""<p><strong>[출력 결과]</strong></p><div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>place</th>
      <th>price</th>
      <th>rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>KFC</td>
      <td>1000</td>
      <td>4.5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>McDonald</td>
      <td>2000</td>
      <td>3.9</td>
    </tr>
    <tr>
      <th>2</th>
      <td>SchoolFood</td>
      <td>2500</td>
      <td>4.2</td>
    </tr>
  </tbody>
</table>
</div>
"""