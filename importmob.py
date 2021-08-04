#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 12:13:58 2021








@author: kavi
"""
import pickle
import mobilebin
mobilebin.write_Mobile() # function
mobilebin.Add_Mobile()
com = input("Enter to search company:")
c =mobilebin.count_company(com)
print(c)