#!/usr/bin/python
#coding:utf-8#
"""
@author: Luo-Jianbiao
@contact: 1037487025@qq.com
@software: PyCharm
@file: Circulate.py
@time: 2020/5/25 15:18
"""
# 求1-100之间的偶数和
sum = 0
# 如果for循环中没有这样的{}块,我们如何知道for循环中的哪个代码块--那就是靠缩进来判别
for x in range(2,101,2):
    sum += x
print(sum)
index = 0
for x in range(1,101,1):
    if x % 2 == 0:
        index += x
print(index)

"""While循环的使用"""
# 使用while循环实现猜字游戏
import random
answer = random.randint(1, 100)
counter = 0
while True:
 counter += 1
 number = int(input('请输入:'))
 if number < answer :
  print('大一点')
 elif number > answer :
  print('小一点')
 else :
  print('恭喜你猜对了')
  break
print('你总共猜了%d'%counter)
if counter > 7 :
    print('智商明显不足')
# 打印九九乘法口诀
for i in range(1,10) :
    for j in range(1,i+1) :
        print('%d * %d = %d'%(i , j, i * j),end='\t')
    print()





