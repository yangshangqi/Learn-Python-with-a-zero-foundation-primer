# autor: zhumenger

'''
    基本语法：
        try:
            检测
        except Exception[as reason]:
            出现异常之后的处理代码
'''
#9.2.1

try:
    f = open("F:/ceshi.txt")
    print(f.read())
    f.close()
except OSError:
    print('文件在打开的过程中出错了T_T')

# 打印出具体的原因

try:
    f = open("F:/ceshi.txt")
    print(f.read())
    f.close()
except OSError as reason:
    print('文件在打开的过程中出错了T_T\n错误的原因是' + str(reason))
    
print("==========")
#9.2.2 一个try语句还可以和多个except语句搭配, 分别与对应的异常进行处理

try:
    sum = 1 + '1'
    f = open('一个不存在的文档'.txt)
    print(f.read())
    f.close()
except OSError as reason:
    print('文件在打开的过程中出错了T_T\n错误的原因是' + str(reason))
except TypeError as reason:
    print('类型出错啦T_T\n出错的原因是' + str(reason))
    
print("==========")
#9.2.3 对多个异常同一处理
try:
    f = open("一个不存在的文档.txt")
    sum = 1 + '1'
    print(f.read())
    f.close()
except (OSError, TypeError) as reason:
    print('出错了T_T\n错误的原因是：' + str(reason))

print("==========")