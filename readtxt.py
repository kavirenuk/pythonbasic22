#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:45:37 2021

@author: kavi
"""

'''
Write a function to read data from a text file ‘DATA.TXT',
 and display word which have maximum number of vowels characters.
'''
f1=open('data.txt','r')
s=f1.read() 
print(s)
countV=0 
countC=0
words=s.split() 
print(words,', ',len(words))
maxV=0 
final='' 
for word in words: 
    countV=0
    for ch in word: 
         if ch.isalnum()==True:
             if  ch in ['a','e','i','o','u','A','E','I','O','U']:#ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':              
                 countV+=1
                 if maxV<countV:
                      maxV=countV  
                      final=word 
print('Final : ',final,', maxV: ',maxV)
