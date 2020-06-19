# autor: zhumenger

'''
读取文件的方法：
    1.使用read(size = -1)函数从文件中读取 size 个字符, 当未给定size值，或者size值为-1时,读取剩余的所有的字符返回
        它是以字节为单位读取
    2.readline()从文件中读取一整行字符串
    3.readlines()从文件中读取每一行字符串并生成一个列表
    4.可以通过tell()方法返回文件指针当前在文件中的位置
'''
f = open("hello.txt", 'r')
print(f.read())
print(f.tell())

'''
seek(offset, from)在文件中移动文件指针, 从from(0表示文件起始位置，1代表当前位置，2代表文件末尾)
   偏移offset个字节
   可以使用该方法将文件指针设置到文件的起始位置
'''
print(f.seek(0, 0))

print(f.readline())

print(f.readlines())
f.seek(0, 0)

#将f文件中的信息存入列表中
print(list(f))

#文件本身支持迭代,可直接用for语句将内容迭代读出来即可：
f.seek(0, 0)

for each_line in f:
    print(each_line)
f.close()