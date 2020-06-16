#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: IfBranch.py
@time: 2020/5/24 18:58
"""
username=input('用户名：')
password=input('密码:')
if username =='admin' and password == '123456':
    print('身份验证成功')
else:
    print('身份验证失败，请重新输入')


