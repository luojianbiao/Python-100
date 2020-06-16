#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@Descriptio:
@software: PyCharm
@file: file_read.py
@time: 2020/6/2 10:37
"""
# 读取文本文件时，需要在使用open函数指定好带路径得文件，并设置文件模式设置，以及指定编码，默认值None
def main():
    """基本得读取文件操作
    缺陷：当文件不存在或者无法打开时，将引发异常状况导致程序崩溃，因此需要对异常进行处理
    详情请见def fileexception函数
    """
    f = open('E:\\hello.txt','r',encoding='utf-8')# 注意路径得写法,这是一次性读取文件所有内容
    print(f.read()) #
    f.close()# 记得关闭

def fileexception():
    f = None
    try :
        f = open('E:\\hello.txt','r',encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')
    finally: #无论try语句中得代码是否运行正常，都会执行到。如果不想使用finally，还可以使用with关键字指定文件对象得上下文环境
        #并在离开上下文环境时释放资源,如下函数filewith
        if f:
            f.close()
def filewith():
    try:
        with open('e:\\hello.txt','r',encoding='utf-8') as f :
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定文件')
    except LookupError:
        print('指定了未知编码')
    except UnicodeDecodeError:
        print('读取文件时解码错误')

# 逐行读取,使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中
import time
def file_forin():
    # 一次性读取整个文件内容
    with open('e:\\hello.txt','r',encoding='UTF-8') as f:
        print(f.read())
#     通过for-in循环逐行读取
    with open('e:\\hello.txt','r',encoding='utf-8') as f:
        for line in f:
            print(line,end='')
            time.sleep(1)
    print()

    # 读取文件按行读取到列表中
    with open('e:\\hello.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
    fileexception()
    filewith()
    file_forin()