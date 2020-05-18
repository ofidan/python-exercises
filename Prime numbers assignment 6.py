# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 15:50:50 2020

@author: Oğuzhan

PRIME NUMBERS
"""

num = int(input("enter a number: "))
pn = []
for i in range(2, num + 1):
    if i == 2:
        pn.append(i)
    elif i == 3:
        pn.append(i)
    elif i == 5:
        pn.append(i)
    elif i == 7:
        pn.append(i)
    elif (i % 2 != 0) and (i % 3 != 0) and (i % 5 != 0) and (i % 7 != 0):
        pn.append(i)
print(pn)    