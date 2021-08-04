#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 08:09:16 2021

@author: kavi
"""
import csv
csv.register_dialect('m',delimiter ='|',skipinitialspace=True)
with open("Writecsv.csv","r") as fh:
    sreader = csv.DictReader(fh,dialect='m')
    print("File contains:")
    for rec in sreader:
        print(rec)