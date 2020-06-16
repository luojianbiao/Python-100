#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio:面向对象进阶
@software: PyCharm
@file: ObjectStrength.py
@time: 2020/5/27 15:54
"""
# @Property装饰器
class Person(object) :
    def __init__(self,name,age):
        self._name = name
        self._age = age
    # @Property装饰器
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @name.setter
    def age(self,age):
        self._age = age
    @age.setter
    def name(self,name) :
        self._name = name

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋。'%self._name)
        else:
            print('%s正在玩斗地主.'% self._name)
def main():
    person = Person('宋小非',13)
    person.play()
    person.age = 22
    person.play()

# __slots__魔法:限定自定义类型的对象只能绑定某些属性
class Animal(object) :
    # 限定Animal对象只能绑定_name,_age,_gender属性
    __slots__ = ('_name','_age')
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(selfs,age):
        selfs._age =age
    def play(self):
        if self._name == '东北虎' :
            print('小心点会吃人')
        else:
            print('怂个软')

"""静态方法
静态方法属于类，而不属于对象的，那么我们可以通过类去调用，而不必实例化对象出来
"""
from math import sqrt
class Triangle(object) :
    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    @staticmethod
    def is_valid(a,b,c):#判断是否构成三角形
        return a+b>c and b+c>a and a+c>b
    def perimeter(self):#三角形周长
        return self._a+self._b+self._c
    def area(self):# 三角形面积
        half = self.perimeter() / 2
        return sqrt(half*(half-self._a) * (half-self._b) * (half-self._c))

"""继承
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，所以，子类比父类拥有更多的功能
"""
class Person(object) :
    """定义人"""
    def __init__(self,name,age):
        self._name = name
        self._age = age
    @property
    def name(self):
        return self._name
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self):
        self._age = age
    def play(self):
        print('%s正在愉快的玩耍'%self._name)
    def watch_av(self):
        if self._age >= 18 :
            print('%s正在看爱情动作片'%self._name)
        else:
            print('%s只能看熊出没'%self._name)
class Student(Person):#继承，需要把父类传进去
    """学生"""
    def __init__(self,name,age,grade):
        super().__init__(name,age) #需要调用父类的构造函数
        self._grade = grade
    @property
    def grade(self):
        return self._grade
    @grade.setter
    def grade(self,grade):
        self._grade = grade
    def study(self,course):
        print('%s的%s正在学习%s'%(self._grade,self._name,course))

"""多态
通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，当我们调用这个经过子类重写的方法时，
不同的子类对象会表现出不同的行为，这个就是多态
"""
from abc import ABCMeta,abstractmethod

class Pet(object,metaclass=ABCMeta):#类名按照驼峰原则,
    """宠物"""
    def __init__(self,nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):#抽象方法，不需要具体实现
        pass
class Dog(Pet):
    def make_voice(self):
        print('%s正在汪汪叫'%self._nickname)
class Cat(Pet):
    def make_voice(self):
        print('%s正在喵喵的叫' % self._nickname)


if __name__ == '__main__':
   # main()
    annimal = Animal('东北虎',12)
    annimal.play()
    a,b,c = 3,4,5
    if Triangle.is_valid(3,4,5):
        t = Triangle(a,b,c)
        print('三角形面积：'+str(t.perimeter()))
    stu = Student('罗建彪',16,'初三')
    stu.study('数学')
    stu.watch_av()

    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()


