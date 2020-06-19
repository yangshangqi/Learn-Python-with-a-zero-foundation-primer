# autor: zhumenger
'''
    一.类中的内置函数：
        1.__init__方法的返回值一定是None，否则会报错
        2.__new__(cls[, ...])是一个对象被实例化的时候第一个被调用的方法，
            cls参数为一个类，该方法返回的是一个对象
        3.__del__(self)：
            当对象将要被销毁时，这个方法便会被调用
'''

'''
    二.算术运算：
        1.工厂函数：其实就是一个类对象，包括 int() float() str() list() tuple()
        2.对象可以用来计算，通过其内部的魔法方法实现:
            __add__(self, onther) 定义加法的行为：+
            __sub__(self, onther) 定义减法的行为：-
            __mul__(self, onther) 定义乘法的行为：*
            __truediv__(self, onther) 定义真除法的行为：/
            __floordiv__(self, onther) 定义整除的行为：//
            __mod__(self, onther) 定义取模的行为：%
            .....
        3.反运算：在算术运算符前面多了一个'r' 如：
            __add__()就对应__radd()__
        作用：比如计算 a + b 如果a的add调用失败了，就会调用b的__radd__方法 保证计算的正确执行
        
        4.python支持增量赋值运算：
            a = a + b可以写成 a += b
        5.一元操作符：
            __neg__():表示正号的行为
            __pos__():表示负号的行为
            __abs__():表示取绝对值
            __invert__():按位取反
'''

#2.1.py
print(type(len)) #<class 'builtin_function_or_method'> 表示内置函数
print(type(int)) #<class 'type'> 表示类对象


#下面我们实现将加减法互换
#2.2.py
class New_int(int):
    def __add__(self, other):
        return int.__sub__(self, other)
    def __sub__(self, other):
        return int.__add__(self, other)
a = New_int(5)
b = New_int(6)
print(a + b)
print(a - b)

#2.3.py
class Nint(int):
    def __radd__(self, other):
        return int.__sub__(self, other)
    
a = Nint(5)
b = Nint(3)
print(a + b) # 结果为8，因为a的__add__方法被调用了
print(1 + b) # 结果为2，因为数字1没有__add__()方法，所以就执行了b的__radd__()方法

print("=====================")

'''
    三.属性访问：
        类也可以通过魔法方法对其属性进行访问：
            __getattr__(self, name): 定义当用户属兔获取一个不存在的属性时的行为
            __getattribute__(self, name): 定义当该类的属性被访问时的行为
            __setattr__(self, name value): 定义一个属性被设置时的行为
            __delattr__(self, name): 定义一个属性被删除时的行为
'''

#3.1.py
class C:
    def __init__(self):
        self.x = 'X-man'
c = C()
print(c.x)
print(getattr(c, 'x', '木有这个这个属性'))
print(getattr(c, 'y', '木有这个这个属性'))

setattr(c, 'y', 'Yellow')
print(getattr(c, 'y', '木有这个属性'))
delattr(c, 'y')
#print(c.y)

print("====================")
class C:
    def __init__(self, size = 10):
        self.size = size
    def getSize(self):
        return self.size
    def setSize(self, value):
        self.size = value
    def delSize(self):
        del self.size
    x = property(getSize, setSize, delSize) #property返回size属性, x相当于size
c = C()
print(c.x)
c.x = 12
print(c.x)
del c.x #这里删除x，就相当于删除了size属性
#print(c.size)  报错

print("====================")

'''
    四.定制序列
         序列类型：列表、元组、字符串，映射类型：字典，都属于容器
         定制容器：即自己定制一个容器，需要了解一些相关的协议：
         __len__(self)；调用len()方法时的行为
         __getitem__(self): 调用获取指定元素的行为
         __setitem__(self):调用设置指定元素的行为
         
'''

#4.1.py

class CountList:
    def __init__(self, *args):
        self.values = [x for x in args]
        self.count = {}.fromkeys(range(len(self.values)), 0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self, key):
        self.count[key] += 1
        return self.values[key]
c1 = CountList(1, 3, 5, 7, 9)
c2 = CountList(2, 4, 6, 8, 10)
print(c1[1])
print(c2[1])
print(c1[1] + c2[1])
print(c1.count)
print(c2.count)

print("====================")
'''
    五.迭代器
        每一次重复的过程被称为一次迭代的过程，没每一次迭代得到的
        结果会被用来作为下一次迭代的初始值
        通常接触的迭代器有：序列(列表，元组，字符串)还有字典，都支持迭代的操作
        
        对于迭代，python提供了俩个BIF：
            iter():对一个容器调用iter()就得到它的迭代器
            next()：调用next()迭代器就会返回下一个值,如果没有值了，便会抛出StopIteration异常
        迭代器的魔法方法：
            __iter()__:用于返回迭代器自身
            __next()__：决定了迭代的规则
'''

#字符串也是一个迭代器
for i in 'FishC':
    print(i)

string = 'FishC'
it = iter(string)
print(next(it))
print(next(it))
print(next(it))

class Fibs:
    def __init__(self, n = 20):
        self.a = 0
        self.b = 1
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a  > self.n:
            raise StopIteration
        return self.a
fibs = Fibs()
for each in fibs:
    print(each)
print("====================")

'''
    六.生成器与推导式
        1.生成器：生成器是迭代器的一种实现
                在普通的函数内部加上 yield 语句便构成了迭代器
                可以暂时挂起函数，并保留函数的局部变量等数据，然后在再次调用它的时候
                从上次暂停的位置继续执行下去
        2.推导式：
            有列表推导式、字典推导式、集合推导式、生成器推导式，函数参数推导式，不存在字符串推导式和元组推导式
            
        
        
'''
#6.1.py
#定义一个生成器，其本身是一个迭代器
def myGen():
    print("生成器被执行了")
    yield 1
    yield 2
myg = myGen()
print(next(myg))
print(next(myg))
#next(myg) 抛出StopIteration异常

#通过for循环迭代
for i in myGen():
     print(i)
print("=====================")

#6.2.py

#通过列表推导式得到能够被2整除，不能够被3整数的数
a = [i for i in range(10) if not(i % 2) and i % 3]
print(a)

#字典推导式

b = {i:i % 2 == 0 for i in range(10)}
print(b)

#集合推导式

c = {i for i in [1, 1, 2, 2, 3, 3]}
print(c)

#生成器推导式
e = (i for i in range(10) if i % 2)
for each in e:
    print(each)
#函数参数推导式

print(sum(i for i in range(100) if i % 2))