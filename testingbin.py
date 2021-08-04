#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:17:47 2021

@author: kavi
"""

import pickle
'''
L = []
f = open("\\home\\kavi\\XII\\testbinlist.dat","wb")
L =[1,2,3,4,5]
pickle.dump(L,f)
f.close()
'''
f = open("\\home\\kavi\\XII\\testbinlist.dat","ab")
L= ['a','b']
pickle.dump(L,f)
f.close()

f = open("\\home\\kavi\\XII\\testbinlist.dat","rb")
try:
    
    while c:
        c=pickle.load(f)
        print(c)
except EOFError:
    f.close()