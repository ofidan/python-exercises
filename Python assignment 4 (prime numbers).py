# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:51:14 2020

@author: 2019
"""


# num = int(input("enter a number: "))
num = 9
if num == 2 or num == 3 or num == 5 or num == 7:
    print("%d is a prime number" %num)
else:
    for i in range(2, num):
        if num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0:
            print("%d is not a prime number" %num)
            break
        else:
            print("%d is a prime number" %num)
            break
    
