# -*- coding: utf-8 -*-
"""Python_Study2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zntSn2LGrUAxvasnkvB_U79uvJdd9foP
"""

def is_odd(n):
  if n%2==0:
    return "짝수"
  else :
    return "홀수"

def avg(*args):
  sol=0
  for i in args:
    sol+=i
    return sol/len(args)

input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)

print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 열린 파일 객체를 닫는다.
f2 = open("test.txt", 'r')
print(f2.read())
f2.close() # 열린 파일 객체를 닫는다.

a="xasdf"

a.find('a')

a.index('a')

# with open('test.txt','w') as f:
#   data=input()
#   data.replace("java","python")
#   f.write(data)

class FourCal:

  def __init__(self, first, second):
    self.first = first
    self.second = second
    
  def setdata(self,b,c):
    self.b =b
    self.c =c

  def add(self):
      result=self.b+self.c
      return result
  
  def mul(self):
      result=self.b*self.c
      return result

  def sub(self):
      result=self.b-self.c
      return result

  def div(self):
      result=self.b/self.c
      return result

