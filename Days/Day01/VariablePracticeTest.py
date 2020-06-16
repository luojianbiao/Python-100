#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: VariablePracticeTest.py
@time: 2020/5/24 18:39
"""
# 将华氏温度转换为摄氏温度
f = float(input('请输入华氏温度：'))
c =(f-32)/1.8
print('%.1f华氏度=%.2f摄氏度'%(f,c))

# 输入圆的半径计算周长和面积
radius = float(input('请输入圆的半径'))
perimeter = 2*3.14*radius
area = 3.14*radius*radius
print('周长：%.2f'%perimeter)
print('面积:%.2f'%area)

# 输入年份判断是不是闰年
year = int(input('输入年份:'))
# 如果代码太长不便于阅读，可以使用\对代码进行折行
is_leap = year % 4 ==0 and year % 100 !=0 or\
          year % 400 == 0
print(is_leap)