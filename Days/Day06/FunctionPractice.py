#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: FunctionPractice.py
@time: 2020/5/26 11:06
"""
# 判断一个数是否为素数
def is_prime(num) :
    for faction in range(2 , int(num**0.5)+1):
        if num % faction == 0 :
            return False
    return True  if num !=1 else False

# 判断一个数是不是回文数
def is_palindrome(num) :
    temp = num
    total = 0
    while temp >0 :
        total = total*10 + temp %10
        temp //= 10
    return total == num
if __name__ == '__main__':
    num = int(input('请输入正整数:'))
    if(is_prime(num) and is_palindrome(num)) :
        print('%d 是回文数'%num)
