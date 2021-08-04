#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:26:59 2021

@author: kavi
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:05:17 2021

@author: kavi
"""

import csv
def addcsv(userName, passWord):
    print("Performing write operation in csv file:")
    f = open('user.csv','w')
    newFileWrite = csv.writer(f)
    newFileWrite.writerow([userName,passWord])
    f.close()
def readcsv():
    print("Reading a content fromm csv file:")
    with open('user.csv','r') as fr:
        newFileReader = csv.reader(fr)
        f = open('usercopy.csv','a')
        newFileWrite = csv.writer(f)
        for row in  newFileReader :
            print(row[0],row[1])
            row1 = newFileReader.next()
            newFileWrite.writerow(row + row1)
       # f = open('usercopy.csv','a')
        print("Copy File Success")
        #newFileWrite = csv.writer(f)
       
        f.close()
    fr.close()
def searchcsv(userName):
    print("Searching Password of a User:")
    with open('user.csv','r') as fr:
        newFileReader = csv.reader(fr)
        for row in  newFileReader :
            if row[0]==userName:
                print(row[0],row[1])
    
addcsv('ravi','123')
readcsv()
searchcsv('ravi')
    
    