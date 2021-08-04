#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:11:20 2021

@author: kavi

Write a function to count the number of lines in a text file, ‘textdata.TXT’

which starts and end with ‘w’ and ‘e’ respectively.


f = open(r"/home/kavi/XII/textdata.txt","w")
f.writelines("William byer is a small boy\n")
f.writelines("Will is wise\n ")
f.writelines("He studies in Hawkin at States\n")
f.writelines("Will fear about strange")
f.close()
f1 = open(r"/home/kavi/XII/textdata.txt","r")
lines = f1.readlines()
count = 0
x= 1
print("Lines of files:",lines)
for i in lines:
    print('Line %d : %sLength is : %d'%(x,i,len(i))) 
    x+=1
    s = i.split()
    print("After split:",s)
    if s[0][0] == "W" and s[-1][-1]=='e':
#   if i[0]=="W" and i[-1]=="e":
        count += 1
print("**********************************************")
print("Line Starts and end with characters:",count)
f1.close()

"""
f = open(r"/home/kavi/XII/textdata.txt","w")
# write(),writelines()
f.writelines("William byer is a short boy r\n")
f.writelines("He fear for stanger\n")
f.writelines("Will is Wiser")
f.close()


f = open(r"/home/kavi/XII/textdata.txt","r")
lines = f.readlines()
print(lines)
count = 0
for i in lines:
    print("Lines:",i)
    s = i.split()
    print(s)
    
#start W and end with r
    if s[0][0]=="W" and s[-1][-1]=="r":
        count += 1
print("Count of lines:",count)

f.close()
















































