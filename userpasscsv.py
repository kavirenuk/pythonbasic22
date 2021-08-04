#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:05:17 2021

@author: kavi
"""
'''
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
        print(newFileReader)
        for row in  newFileReader :
            print(row[0],row[1])
    fr.close()
def searchcsv(userName):
    print("Searching Password of a User:")
    with open('user.csv','r') as fr:
        newFileReader = csv.reader(fr)
        for row in  newFileReader :
            print(row)
            if row[0]==userName:
                print(row[1])
    
addcsv('ravi','123')
readcsv()
searchcsv('ravi')
'''
import csv
#write to csv
f = open("userpassword.csv","w",newline="\n")
fileWrite = csv.writer(f,delimiter="\t")
soc = [["user","password"],["email.id","code"]]
fileWrite.writerow(soc)
print("Successfully executed")
f.close()
fr = open("userpassword.csv","r",newline="\n")
print("Reading from csv")
fileRead = csv.reader(fr,delimiter="\t")
for row in fileRead:
    print(row[0],row[1])
fr.close()




    
    