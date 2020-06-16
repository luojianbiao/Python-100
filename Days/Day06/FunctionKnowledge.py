#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: FunctionKnowledge.py
@time: 2020/5/25 16:14
"""
"""
# 利用函数求阶乘
def fac(num):
    result = 1
    for n in range(1 , num + 1):
        result *= n
    return result
m = int(input('请输入要计算的阶乘:'))
n = int(input('请输入要计算的阶乘:'))
# 调用函数
print(fac(m),fac(n),fac(m-n))
"""
# 在pyton中，函数参数可以有默认值，也支持可变参数
from random import randint
# 默认该函数有初始值
def roll_dice(n=2) :
  """摇色子"""
  total = 0
  # for _ in range(n)中_占位符 表示不在意变量的值 只是用于循环遍历n次，无法打印变量值。
  for _ in range(n) :
      total += randint(1 , 6)
  return total
# 三个数相加
def add(a = 0 , b = 0 , c = 0):
    return a+b+c
# 如果没有指定参数那么使用默认值摇两颗色子
print(roll_dice())
# 要三次色子
print(roll_dice(3))
# 没有指定参数相加
print(add())
# 两个数相加
print(add(34,23))
"""虽然可以传递可变参数，但是必须<=参数设定的数量，如超过，则运行会冒错
print(add(23,43,32,32))
"""
# 设定可变参数的函数
def _add(*args) :
    total = 0
    for val in args :
        total += val
    return total
# 调用add时可以传入0或者多个参数
print(_add(1))
print(_add(3,4,5))
"""用模块管理python函数
# 由于python没有重载的概念，如果定义了两个同名的函数，那么后面的定义会覆盖之前的定义，也就意味着两个同名函数只有一个存在
为避免该问题，通过import关键字导入指定的模块(.py就是一个模块)就可以区分到底使用哪个模块，例如
# 方法1
moudle1.py
def foo():
    Print('goodbye ,world')
    
module2.py
def foo():
    print('goodbye ,world')

test.py
from module1 import foo
foo()这里调用的就是module1的函数
from module2 import foo
foo() 这里调用的就是module2的函数

# 方法2
test.py
import module1 as m1
import module2 as m2
m1.foo()
m2.foo()
"""

"""重点：如果我们导入的模块除了定义函数之外还有可以执行代码（相当于c语言中的main函数）,
那么python解释器导入这个模块时候就会执行这些代码，事实上我们可以并不希望如此。
因此入股我们在模块中编写了这些代码，最好将这些代码防盗如下所示条件中，这样的话除非直接运行该模块
moudle2.py
    def foo():
    print('helloword')
#    _name_是python中一个隐含变量，它代表了模块的名字，而只有被Python解释器直接执行的模块名字才是_main_
if _name_ == '_main_'
    print('call foo()')
    foo()
    
test.py
    # 导入module2得时候，不会执行module模块中if条件成立时的代码，因为模块名字是module3而不是_main_
    import module2
    
"""