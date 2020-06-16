#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: StringTest.py
@time: 2020/5/26 15:11
"""
# 单引号或双引号
s1 = 'hello,world'
s2 = 'luojianbiao'
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
宋非
金安安
"""
print(s1,s2,s3,end='')
# \表示转义，和C语言中转义字符一个样
# 可以使用*运算符来重复一个字符串内容
s4 = 'hello'*4 # 结果hello hello hello hello
# 可以使用+运算符来实现字符串的拼接
s5 = s1 + s2
print(s5)
# 可以使用 in 和 not in 来判断一个字符串是包含另外一个字符串
print('hello' in s1) #True
print('luojianbiao' not in s4) #False
s7 = '原谅我这一生不羁放纵爱自由'
# 从字符串中取出指定位置的字符[]
print(s7[1]) #谅
# 字符串切片,字符串[开始索引:结束索引:步长],缺省情况下步长为1
print(s7[2:5])
print(s7[2:])
print(s7[2::2])
print(s7[::2])
print(s7[::-1])
print(s7[-3:-1])#截取倒数第三位与倒数第一位之间的字符串
a , b = 5 ,10
print(f'{a}*{b}={a*b}')

"""使用列表,本质上和java中数组差不多.是一种结构化的,非标量类型,它的值是有序序列
每个值都可以用索引进行标识,定义列表可以将列表的元素放在[]中,多个元素用,进项分隔,可以用for循环对列表元素进行遍历
也可以使用[][:]运算负去除列表中一个或多个元素
"""
list1 = [1,2,3,4,5,6,7,8,9]
for index in range(len(list1)) :
    print(list1[index])
"""
元组:可以用一个变量(对象)来存储多个数据,不同之处在于元组的元素不能修改.顾名思义,多个元素合在一起就形成了一个元组
"""
# 定义元组
t = ('宋小非',89,'云南昆明')
for member in t :
    print(member)
# 元组和列表可以互相转换
person = list(t)
print(person)
fruit_list = tuple(person)
print(fruit_list)

"""
字典:字典是另一种可变容器模型,可以存储任意类型对象,字典中每一个元素都是由一个键和一个值组成的键值对,键和值用:分开
"""
# 创建字典
scores = {'宋小非':85,'程一多':89}
print(scores)
print(scores['程一多']) #通过键盘获得值
# 只获取键
for key in scores :
    print(key,'值',scores[key])
#     对键值遍历
for key ,value in scores.items() :
    print(key,':',value)
