#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio: 面向对象知识点
@software: PyCharm
@file: ObjectTest.py
@time: 2020/5/27 15:29
"""
# Python对象定义
class Student(object):
    # 初始化操作
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self,cource_name):
        print('%s正在学习%s'%(self.name,cource_name))
    def watch_movie(self):
        if self.age < 18 :
            print('%s 只能看熊出没'%self.name)
        else:
            print('%s正在观看爱情动作片'%self.name)
def main():
        # 创建学生对象并指定姓名和年龄
    stu1 = Student('罗建彪',25)
    stu1.study('Pyuthon程序设计')
    stu1.watch_movie()
    stu2 = Student('宋小非',27)
    stu2.study('党的指导思想')
    stu2.watch_movie()
if __name__ == '__main__':
    main()
