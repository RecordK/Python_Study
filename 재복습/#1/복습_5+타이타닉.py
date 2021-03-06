# -*- coding: utf-8 -*-
"""복습#5+타이타닉

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SPNcvzOBATc3VRUF7xTUSCj7CzIIO-T4
"""

import pandas as pd
url='https://raw.githubusercontent.com/TeamLab/machine_learning_from_scratch_with_python/master/code/ch12/titanic/train.csv'
tit=pd.read_csv(url)
tit

tit.info()

tpa=tit[['Pclass','Age']]
tas=tit[['Age','Survived']]

tpa.plot.scatter(x='Pclass',y='Age')

tas.plot.bar(x='Age',y='Survived')

tit.sort_values(['Pclass','Age'],ascending=[False,True])

tit['Age'].isnull()

sum(tit['Age'].isnull())

tit[tit['Age'].isnull()]

tit[tit['Age'].isnull()]['Pclass'].value_counts()

tit[tit['Age'].isnull()]['Sex'].value_counts()

#Cabin 항목별 빈도수
tit['Cabin'].value_counts()

sum(tit['Cabin'].isna())

tit[tit['Cabin'].isna()]['Pclass'].value_counts()#티켓 등급별 빈도수

tit[tit['Age'].isna()]

age_mean=tit['Age'].mean()

tit['Age']=tit['Age'].fillna(age_mean)

tit.info()

tit['Embarked'].isnull()

print(tit['Embarked'].value_counts()[0]) #맨 처음 값
print(tit['Embarked'].value_counts().index[0]) #맨 처음 값의 인덱스

emax=tit['Embarked'].value_counts().index.max() #맨처음값값

tit['Embarked']=tit['Embarked'].fillna(emax)

tit.info()

#pd.cut(Seriesdata,경계값리스트트,labels=구간별별 이름리스트)
pd.cut(
    tit['Age'],
    [0,15,25,45,60,100],
    labels=['소아','청년','장년','중년','노년']
)

tit[tit['Pclass']==1]

tit[~tit['Pclass'].isin([1,2])]

#성별 생존율

pd.pivot_table(values='Survived',index='Sex',data=tit)

# 승객객 등급별 생존율
pd.pivot_table(values='Survived',index='Pclass',data=tit)

# 승객 등급별 성별 생존율
pd.pivot_table(values='Survived',index=['Pclass','Sex'],data=tit)

# 승객 등급별 성별 생존율
pd.pivot_table(values='Survived',index='Pclass',columns='Sex',data=tit)

# 성별별 생존자 수 
tit.pivot_table(values='Survived',index='Sex',aggfunc='sum')

# 성별별 생존자 수 
tit.pivot_table(values='Age',index='Sex',aggfunc='max')

# 성별 승객등급별최고령생존자나이
tit[tit['Survived']==1].pivot_table(values='Age',index='Sex',columns='Pclass',aggfunc='max')

tit[tit['Age']==57]

