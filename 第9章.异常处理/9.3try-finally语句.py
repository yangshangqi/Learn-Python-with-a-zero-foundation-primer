# autor: zhumenger
'''
    如果使用open()打开一个已经存在的文件,但在执行文件关闭函数close()函数之前出现了异常，便会执行except语句
也就是说文件打开了,但并没有执行关闭文件的命令。
    为了实现像这种“就算出现了异常，也要执行收尾工作”，python引入了finally来扩展try
'''

#9.3.1

try:
    f = open("F:\代码文件集\python代码文件\小甲鱼入门学习\第9章.异常处理\存在的文档.txt")
    print(f.read())
    sum = 1 + '1'
except (OSError, TypeError) as reason:
    print("出错啦\n出错的原因是" + str(reason))
finally:
    f.close()

#9.3.2 raise语句 使代码自动抛出一个异常
#raise ZeroDivisionError("除数不能为0")

#9.3.3 丰富的else语句

try:
    sum = 1 + 1
except:
    print("出错了")
else:
    print(sum)
    
'''
9.3.4简洁的with语句,基本语法如下：
    with expression [as target]:
        执行
    expression：是一个需要执行的表达式；
    arget：是一个变量或者元组，存储的是expression表达式执行返回的结果
    
    with语句的工作原理：
        紧跟with后面的语句会被求值，对象的__enter__()方法被调用，这个方法的返回值将被赋值给as关键
        字后面的变量，当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
'''

try:
    with open('存在的文档.txt') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了' + str(reason))
    
try:
    with open('不存在的文档.txt') as f:
        for each_line in f:
            print(each_line)
except OSError as reason:
    print('出错了' + str(reason))