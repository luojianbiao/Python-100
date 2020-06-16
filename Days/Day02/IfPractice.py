#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: IfPractice.py
@time: 2020/5/24 19:03
"""
# 判断输入的三角形能否构成三角形，如果能则计算三角形的周长和面积
a = float(input('a边:'))
b = float(input('b边:'))
c = float(input('c边:'))
if a+b>c and a+c>b and b+c>a :
    print('周长：%.2f'%(a+b+c))
    p = (a+b+c)/2
    area =(p*(p-a)*(p-b)*(p-c))**0.5
    print('面积：%.2f'%(area))
else:
    print('不能构成三角形，请重新输入')

# 百分制成绩转换为等级成绩
score = float(input('请输入成绩:'))
if score>=90:
    grade='A'
elif score>=80:
    grade='B'
elif score>=60:
    grade='C'
else:
    grade='垃圾还有脸来问'
    print('对应的等级是',grade)
