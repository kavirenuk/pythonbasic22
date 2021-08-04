#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 10:30:58 2021

@author: kavi
"""

import pickle
member = {}

def writemem():
    ch = 'Y'
    f = open("member.dat","ab")
    while ch.upper() =='Y':
        MemberNo = int(input("Member No:"))
        Name =input("Member Name:")
        member["MemberNo"] = MemberNo
        member['Name']=Name
        pickle.dump(member,f)
        ch = input("Y or N:")
    f.close()
          
def readbin(check):
    f = open("member.dat","rb")
    try:
        while True:
            member=pickle.load(f)
            if member['MemberNo']==check:
                print(member)
    except:
        f.close()
        
def displaybin():
    f = open("member.dat","rb")
    try:
        while True:
            member=pickle.load(f)
            print(member)
    except:
        f.close()
#writemem()
check = int(input("Search :"))
readbin(check)
#displaybin()
