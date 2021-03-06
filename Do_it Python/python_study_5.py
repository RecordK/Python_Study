# -*- coding: utf-8 -*-
"""python_study_5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zLEIVva9-3wlM1PCup1_gSH0mxM8427I
"""

##6-5~07-1

import sys

option = sys.argv[1]
memo=sys.argv[2]

print(option)
print(memo)

def search(dirname):
  print(dirname)

search("/content")

import os

def search(dirname):
  filenames=os.listdir(dirname)
  for filename in filenames:
    full_filename=os.path.join(dirname,filename)
    print(full_filename)
search("/content")

import os

def search(dirname):
  filenames=os.listdir(dirname)
  for filename in filenames:
    full_filename=os.path.join(dirname,filename)
    ext=os.path.splitext(full_filename)[-1]
    if ext=='.py':
      print(full_filename)
search("/content")

import os

def search(dirname):
  try:
    filenames=os.listdir(dirname)
    for filename in filenames:
      full_filename=os.path.join(dirname,filename)
      ext=os.path.splitext(full_filename)[-1]
      if os.path.isdir(full_filename):
        search(full_filename)
      else :
        ext=os.path.splitext(full_filename)
  except PermissionError:
    pass
    

search("/content")

import os

for (path, dir, files) in os.walk("/content"):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == '.py':
            print("%s/%s" % (path, filename))

data = """
park 800905-1049118
kim  700905-1059119
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))

import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

