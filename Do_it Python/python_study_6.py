# -*- coding: utf-8 -*-
"""python_study_6

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p53Hd0lkDRgCkF1UUni9inQCZ_TsXnob
"""

## 연습문제 5
## 피보나치 수열
def x(n):
  if n ==0:return 0
  if n==1: return 1
  return x(n-2)+x(n-1)
for i in range(10):
  print(x(i))

## 연습문제 6
user=input()
x=user.split(",")
total=[int(i) for i in x]

sum(total)

l = [i for i in range(1,10)]

l

x=int(input())
s=[x*i for i in l]
print(s)

f=open('abc.txt',r)
lines=f.readlines()
f.close()

lines.reverse()
f=open('abc.txt',w)
for line in lines:
  line=line.strip()
  f.write(line)
  f.write('\n')
f.close()



