# autor: zhumenger

'''
如果需要写入文件,请以'w' 或'a'模式打开
使用write(str)函数向文件中写入文字
'''

f1 = open("write.txt", 'w')
print(f1.write("~~~^_^~~~")) #返回文件指针的位置

# writelines(seq)向文件中写入字符串序列seq,seq应该是一个返回字符串的可迭代对象
f1.writelines(["123", 'abc'])
f1.close()