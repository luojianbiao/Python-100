#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio:字符串、列表、元组、字典循环
@software: PyCharm
@file: usually_practice.py
@time: 2020/6/11 15:04
"""
"""字符串循环读取"""
def str_pracite():
    str_name = '原谅我这一生不羁放纵爱自由'

    for values in str_name:
        print(values)

"""列表的遍历读取"""
def list_practice():

    list_1 = [1,3,'luojianbiao','宋小'] #定义列表
    list_1.append('小孔') #添加元素，添加在末尾
    list_1.insert(2,'罗建明') #插入元素，需要表明插入位置
    print(list_1[2])
    list_1.remove('luojianbiao')#删除
    #遍历方法1
    for value in enumerate(list_1):#遍历输出包括下标，该种方法还可以遍历的起始位置
        print(value)
    #遍历方法2
    for value in list_1:#该方法只遍历值
        print(value)
    #遍历方法3
    for key ,value in enumerate(list_1):#该方法遍历值与下标分别存储
        print(key,value)

"""元组的遍历"""
def tuple_practice():

    tuple_1 = ('罗','kong','宋',['ni',2])#固定长度，所以无法添加
    for value in tuple_1:
        print(value)
    print(tuple_1[2])#可以使用下标进行访问

"""字典的遍历"""
def dict_practice():

    dict_1 = {'luo':'罗建彪','song':'宋非'}
    dict_1['song'] = '宋晓飞'#根据键添加
    del dict_1['luo']#根据键删除

    for key,value in dict_1.items():#遍历键和值
        print(key,value)
    for value in dict_1.values():#遍历值
        print(value)
    for key in dict_1.keys():#遍历键
        print(key)


def main():
   #str_pracite()
   list_practice()
   #tuple_practice()
   #dict_practice()

if __name__ == '__main__':
    main()