#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:28:32 2021

@author: kavi
"""

'''
A binary file 'ATTENDANCE.DAT' has structure [Admission_Number, Name, Attendance, Working_days] .
 Write a function count_short_attendance() in Python that would read
 contents of the file 'ATTENDANCE.DAT' and display the details of those students 
 whose attendance is below 75%. Also display the total number of students with attendance 
 below 75%.

'''
import pickle
def write_attendance():
    print("****New Attendance Entry****")
    ch='y'
    fobjw=open('Attandance.dat','wb') 
    print("Writing new file:")
    while ch=='y':
            admissionno=int(input('Enter admission No:') )
            Name=input('Enter Name of student:')
            attendance = int(input('attendance:')) 
            workday = int(input("Enter no of working days:"))
            rec=[admissionno,Name,attendance,workday] 
            pickle.dump(rec,fobjw)
            ch = input("Y or N:")
            
            
    
    fobjw.close()

    
def count_short_attendance(): 
    print("********Count attendance******")
    fobj=open('Attandance.dat','rb') 
    num = 0
    try:
        while True: 
                 rec=pickle.load(fobj)  
                 a=rec[2]/rec[3]* 100  
                 if a < 85.0:  
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
