#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 21:13:24 2021

@author: kavi
"""

myfile = open("/home/kavi/XII/poem.txt","r")
'''
str = myfile.read(30)
print(str)
t = myfile.tell()
print(t)

str1 = myfile.read(50)
print(str1)

str2 = myfile.readline()
print(str2)

str3 = myfile.readline()
print(str3)

print(myfile.tell())

str4=myfile.readlines()
s = str4.split()
for i in s:
    print(i)
#print("List of strings",len(s))
  
count = 0
for line in myfile:
    print("Lines of file:",line)
    words = line.split()
    print(words)
    for word in words:
        if word[0] not in 'B':
            print(word)
            count += 1
print(count)

data = myfile.read()
print("Record:",data)
count = 0
for letter in data:
    print("Letters",letter)
    if letter.isupper():
        count +=1
print(count)
'''
