#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: CirculatePractice.py
@time: 2020/5/25 16:01
"""
from math import sqrt
# 判断一个数是否为素数
num = int(input('请输入一个正整数:'))
end = int(sqrt(num))
is_prime = True
for x in range (2,end +1) :
    if num % x == 0 :
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' %num)
else:
    print('%d不是素素'%num)
