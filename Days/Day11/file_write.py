#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio: python写入文件
@software: PyCharm
@file: file_write.py
@time: 2020/6/2 11:25
"""
from math import sqrt

"""例子演示：将1-9999之间的素数分别写入三个文件中"""

def is_prime(n):
    """判断是否为素数的函数"""
    assert n > 0 # assert 用于判断一个表达式，如果表达式条件为false的时候出发异常
    for factor in range(2,int(sqrt(n)+1)) :
        if n % factor == 0:
            return  False
    return True if n != 1 else False

def main():
    filenames = ('a.txt','b.txt','c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename,'w',encoding='utf-8')) # 如果写入的文件不存在会自动创建文件而不会引发异常
        for number in range(1,10000):
            if is_prime(number):
                if number <100:
                    fs_list[0].write(str(number)+'\n')
                elif number <1000:
                    fs_list[1].write(str(number)+'\n')
                else:
                    fs_list[2].write(str(number)+'\n')
    except IOError as ex:
        print(ex)
        print('写入文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')
"""读写二进制文件"""
def writejpg():
    try:
        with open('2019.jpg','rb') as fsjpg:
            data = fsjpg.read()
            print(type(data))
        with open('2020.jpg','wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('指定文件无法打开')

if __name__ == '__main__':
    main()
    writejpg()
