# -*- coding: utf-8 -*-
"""Python_Study3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dj0Y9Xm51zjRLvFXbBlE_DBO9D4NGbNT
"""

import sys

sys.path

sys.path,append

l=[1,-3,2,0,-5,6]

def positive(l):
  result=[i for i in l if i>0]
  return result

print(positive([1,-3,2,0,-5,6]))

def two_times(numberList):
  result=[]
  for number in numberList:
    result.append(number*2)
  return result

result = two_times([1,2,3,4])
print(result)

def two_times(numberList):
  result=[number*2 for number in numberList]
  return result

result = two_times([1,2,3,4])
print(result)

def two_times(numberList):
  return numberList*2
print(list(filter(two_times,[1,2,3,4])))

print(list(map(two_times,[1,2,3,4])))

print(list(map(lambda x:x*2,[1,2,3,4])))

