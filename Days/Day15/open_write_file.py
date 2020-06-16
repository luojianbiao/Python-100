#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio:
@software: PyCharm
@file: open_write_file.py
@time: 2020/6/15 15:22
"""
def read_file1():

    """open('文件路径'，‘读取方式’，‘读取编码’)"""
    # 读取方式 r:以只读方式读取，如果文件不存在会报错
    readfile1 = open('E:\K-机器学习\K1_PythonCode\Python-100\Days\Day15\helloword.txt','r',encoding='utf-8')
    print(readfile1.read())# read() 表示一次读取文件中所有内容
    readfile1.close()
def read_file2():
    """为保证文件无论如何都能被关闭，可以使用try...finally来实现"""
    try:
        readfile2 = open('E:\K-机器学习\K1_PythonCode\Python-100\Days\Day15\helloword.txt', 'r', encoding='utf-8')
        print(readfile2.read())
        num = 10/0
    finally:
        if readfile2:
            readfile2.close()
def read_file3():
    with open('E:\K-机器学习\K1_PythonCode\Python-100\Days\Day15\helloword.txt', 'r', encoding='utf-8') as f:
        list = f.readlines()#一次读取全部内容，返回一个list
        for readlist in list:
            print(readlist.rstrip())#读取文件每一行的默认都有换行符，使用rstrip()避免print方法造成的换行
#read_file1()
#read_file2()
read_file3()