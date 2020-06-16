#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: StringPractice.py
@time: 2020/5/26 16:37
"""
# 在屏幕上显示跑马灯文字
import os
import time
import random

def main1() :
    content = '全国最有实力的养猪厂长罗先生发来贺电'
    while True :
        # 清理屏幕上输出
        os.system('cls')
        print(content)
        # 休眠20毫秒
        time.sleep(2000)
        content = content[1:]+content[0]
# 生成指定长度的验证码
def generate_code(code_len = 4) :
     all_chars = '0123456789abcdefghijklmnopqrstuvwsyz'
     last_pos = len(all_chars)-1
     code = ''
     for _ in range(code_len) :
         index = random.randint(0,last_pos)
         code += all_chars[index]
     return code
# 指定年月日是一年中的第几天
def is_leap_year(year) :
    return year % 4 == 0 and year % 100 !=0 or year % 400 == 0
def which_day(year,month,date) :
    day_of_month = [[31,28,30,31,30,31,31,30,31,30,31],[31,29,30,31,30,31,31,30,31,30,31]][is_leap_year(year)]
    total = 0
    for index in range(month-1) :
        total += day_of_month[index]
    return total+date
if __name__ == '__main__':
    # main1()
    print(generate_code(6))
    print(which_day(2020,5,26))