# autor: zhumenger

'''

OS模块中关于文件/目录常用的函数使用方法
'''

import os
#1.getcwd() 返回当前工作目录

print(os.getcwd())

#2.chdir(path) 改变工作目录

os.chdir("F:/")
print(os.getcwd())

#3.listdir(path = '.') 列举指定目录中的文件名('.'表示当前目录，'..'表示上一级目录)

print(os.listdir())
print(os.listdir('F:/代码文件集/python代码文件'))

#4.mkdir(path) 创建单层目录, 如果该目录已存在则抛出异常

os.mkdir('test')

print(os.listdir())

#5.makedirs(path) 递归创建多层目录，如果该目录已存在则抛出异常

os.makedirs('a/b/c')


#在给文件夹下创建一个txt文本

cur_path = os.getcwd()

full_path = cur_path + "wenben.txt"
file = open(full_path, 'w')
file.close()

'''
6.remove(path) 删除指定的文件
    rmdir(path)删除空的单层目录
    removedirs(path) 递归删除多层目录，如果不为空则抛出异常
'''
os.remove('wenben.txt')

os.rmdir('test')

os.removedirs('a/b/c')
print(os.listdir())

#7.rename(old, new) 用于重命名文件或文件夹
os.chdir('F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理')
os.rename('rename.txt', '8.4.txt')
os.rename('8.4.txt', 'rename.txt')

#8.system(command) 运行系统的shell命令

#os.system('calc') #打开计算器

#9.walk(top) 遍历top参数指定路径下的所有子目录,并将结果返回一个三元组(路径，[包含目录], [包含文件])
for i in os.walk('F:\web作业'):
    print(i)
    
'''
    os.curdir 表示当前目录
    os.pardir 表示上一级目录
    os.sep 表示路径的分隔符
    os.linesep 表示当前平台使用的行终止符
    os.name表示当前使用的操作系统
'''
print(os.curdir)
print(os.pardir)
print(os.sep)
print(os.name)

