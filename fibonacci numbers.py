# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 15:08:42 2020

@author: Oğuzhan
"""
# fibo = [1, 1]
# for i in range(0, 8):
#     fibo.append(fibo[i] + fibo[i + 1])
#     print(fibo)

fibo = [1, 1]
i = 0
a = 0
while a < 55:
    fibo.append(fibo[i] + fibo[i + 1])
    i += 1
    a = int(fibo[i + 1])
    print(fibo)