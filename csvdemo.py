#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 15:17:12 2021

@author: kavi
"""

"""write a python program to perform read and write to csv file.
[user,password]"""

import csv
f = open("userpassdemo.csv","w",newline="\r\n")
writerobj = csv.writer(f,delimiter = "\t")
writerobj.writerows([['user','password'],['email','id']])
#writerobj.writerow(['Lizy','123'])
print("Successfully executed")
f.close()

fr = open("userpassdemo.csv","r",newline="\r\n")
readerobj = csv.reader(fr,delimiter = "\t")
print(readerobj)
for row in readerobj:
    print(row[0])
    for i in row:
        print(i)
    '''
    print("Row 1",row[7])
    print("Row 2",row[1])
    if row[1] =='id':
        print("ID Found")
        print(row[1])
    else:
        print("Not Found")'''
#writerobj.writerow(['Lizy','123'])
print("Successfully executed")
f.close()