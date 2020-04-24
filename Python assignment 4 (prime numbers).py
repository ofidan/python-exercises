# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:51:14 2020

@author: 2019
"""


num = int(input("enter a number: "))
if num == 2:
    print("%d is a prime number" %num)
elif num == 3:
    print("%d is a prime number" %num)
else:
    for i in range(2, num -1):
        if num % 2 == 0 or num % 3 == 0:
            print("%d is not a prime number" %num)
            break
        else:
            print("%d is a prime number" %num)
            break
    
