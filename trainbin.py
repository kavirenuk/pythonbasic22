#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 09:37:42 2021

@author: kavi
"""

import pickle
'''
train = {}
f = open("TRAIN.dat","wb")
ch = 'Y'
try:
    while ch.upper() =='Y' :
        Tno = int(input("Tno:"))
        From =input("From :")
        To = input("To:")
        train['Tno']=Tno
        train['From']= From
        train['To'] =To
        pickle.dump(train,f)
        ch = input("Y or N:")
        
except:
    f.close()
'''
def searchTrain(To):
    f = open("TRAIN.dat","rb")
    trains = {}
    print("Searching and display")
    try:
        while True:
            train = pickle.load(f)
            if train['To']==To:
                print(train)
    except:
        f.close()
dest = input("Destination:")
searchTrain(dest)

    