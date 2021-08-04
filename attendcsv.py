#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 13:23:18 2021

@author: kavi
"""
import csv
def write_attendance():
    print("****New Attendance Entry****")
    ch='y'
    fobjw=open('Attandance.csv','w') 
    swriter = csv.writer(fobjw)
    print("Writing new file:")
    while ch=='y':
            admissionno=int(input('Enter admission No:') )
            Name=input('Enter Name of student:')
            attendance = int(input('attendance:')) 
            workday = int(input("Enter no of working days:"))
            rec=[admissionno,Name,attendance,workday] 
            swriter.writerow(rec)
            ch = input("Y or N:")
            
    
    fobjw.close()
    
def count_short_attendance(): 
    print("********Count attendance******")
    fobj=open('Attandance.csv','r') 
    ereader = csv.reader(fobj)
    num = 0
    try:
        for rec in ereader:
                  
                 a=rec[2]/rec[3]* 100  
                 if a < 94.0:  
                     print("Below:")
                     print(rec[0],rec[1],rec[2],rec[3],a) 
                     num = num + 1
                 else:
                     print("Above:")
                     print(rec[0],rec[1],rec[2],rec[3],a) 
                     
        print("Total no of students with below attendance:",num)
    except EOFError:
        fobj.close()
    return num
    

print(write_attendance())
print("Total number of students with below attendance:",count_short_attendance())