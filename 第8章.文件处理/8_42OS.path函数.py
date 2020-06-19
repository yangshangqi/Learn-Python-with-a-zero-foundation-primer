'''
autor: zhumenger
    OS.path主要完成一些针对路径名的操作
'''

import os

#1.basename(path)去掉目录路径，单独返回文件名
#2.dirname(path) 去掉文件名，单独返回目录路径
print(os.path.basename('F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理\\text.txt'))
print(os.path.dirname('F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理\\text.txt'))

#3.join(path2[, path2[, ..]) 将path1和path2各部分组成一个路径名

print(os.path.join("F:/代码文件集/python代码文件/小甲鱼入门学习"), "第8章.文件处理/text.txt")

#4.split(path) 分割文件名和路径 如果都是目录，也还会将最后一个目录作文文件名分离
#   splitext(path)用于分割文件名和扩展名
print(os.path.split('F:/代码文件集/python代码文件/小甲鱼入门学习/第8章.文件处理/text.txt'))
print(os.path.splitext('F:/代码文件集/python代码文件/小甲鱼入门学习/第8章.文件处理/text.txt'))

#5.getsize(file) 获取文件的大小，以字节为单位

os.chdir("F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理")
print(os.path.getsize('test.txt'))

#6.getatime() getctime() getmtime() 分别获得文件的最近访问时间、创建时间和修改时间
#   返回值是浮点型秒数, 可用time模块的gmtime()和localtime()函数换算

import time

temp = time.localtime(os.path.getatime('test.txt'))
print("文件被访问的时间是", time.strftime("%d %b %Y %H %M %S"), temp)

