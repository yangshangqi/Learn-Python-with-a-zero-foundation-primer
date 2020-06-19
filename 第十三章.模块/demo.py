# autor: zhumenger

'''
    一.模块及程序：
        基本语法：import 模块名
        模块名即命名空间，调用该模块中的方法：模块名.方法()
        
        from 模块名 import 函数名:
            该语句将模块中的函数引入进来，我们就可以直接调用该方法名来执行函数，不需要加上命名空间了
            
        import 模块名 as 新名字：
            给命名空间替换一个新的名字，可以减少命名空间的代码量

'''
#3种导入模块的方法

import hello
hello.Hello()

from hello import Hello
Hello()

import hello as h
h.Hello()
print("=====================")

'''
    二.__name__ == '__main__'
        如果该模块内部调用了自己方法，当我们导入的时候，其内部调用的方法就会跟着执行，但这并不是我们想要的，
        所以我们需要让python知道，该模块是作为程序被调用还是导入到了其他的程序中
        
        此时我们便需要调用模块的__name__属性：
            当一个程序运行时，该程序的__name__属性的值是'__main__',
            而再导入模块的时候，这个值就是该模块的名字
'''
import test
test.ha()


'''
    三.搜索路径
        python在导入模块的时候，会在预定义好的搜索路径中去寻找要导入的模块文件，如果有，则导入；
        如果没有，则导入失败，搜索路径就是一个目录，可以通过sys模块中的path变量显示出来
        
        可以将模块所在的位置添加到所搜路径中去
        sys.path.appedn("")
'''

import sys
print(sys.path)
#import KNN 报错
sys.path.append("F:\代码文件集\python代码文件\小甲鱼入门学习\M1")
print(sys.path)
import hello #能够正常导入
hello.Hello()
'''
    四.包
        包即模块的集合：我们将功能相似的模块放在同一个文件夹中，这个文件夹就是一个包
        我们把模块分门类别的存放在不同的文件夹，然后把各个文件夹的位置告诉python, 创建一个包的具体操作:
            (1).创建一个文件夹，用来存放相关的模块，文件夹的名字就是包的名字;
            (2).在文件夹中创建一个__init__.py的模块文件，内容可以为空；也可以写一写初始化的代码。
                这个是python的规定，用来告诉python 将该目录当成一个包来处理。
            (3).将相关的模块放入文件夹中
'''

# 在程序中导入包的模块(包名.模块名):
sys.path.append("F:\代码文件集\python代码文件\小甲鱼入门学习")
import M1.hello as h
h.Hello()
print("=======================")

'''
    五.模块的使用
        1.可以通过调用__doc__属性，查看这个模块的简介
        2.使用dir()函数可以查询到该模块定义了哪些变量、函数和类
        3.使用__all__属性可以直接获得可供调用接口的信息
            注意：并不是所有的模块都有__all__属性
        4.__file__属性可以指明该模块的源代码位置
        5.help()函数的使用
'''
import timeit
print(timeit.__doc__)
print("=========================")
print(dir(timeit))

print(timeit.__all__)

print(timeit.__file__)
help(timeit)

