# autor: zhumenger

'''
一.类与对象：
    1.类的命名以大写字母开头
    2.类中的变量为该类的属性
    3.类中的方法为该类的行为
    
    4self即实例对象本身
'''

#定义乌龟类
class Turtle:
    # 属性：
    color = "green"
    weight = 10
    legs = 4
    shell = True
    mouth = "大嘴"
    
    # 行为：
    def climb(self):
        print("我正在努力的向前爬...")
    def run(self):
        print("我正在飞快的向前跑")
    def eat(self):
        print("有的吃，真满足^_^")
    def bite(self):
        print("咬死你咬死你！！")
    def sleep(self):
        print("困了，睡了，晚安，Zzzz")
    def setName(self, name):
        self.name = name
    def getName(self):
        print("我是一只有名字的小乌龟: I'm " + self.name)
tt = Turtle()
tt.climb()
tt.eat()
tt.sleep()

tt.setName("小王8")
tt.getName()


'''
    二.构造方法：
        python中的构造方法为__init__(),在实例化对象的时候便会自动调用
        我们可以通过重新改构造方法，实现不同的功能
'''

class Potato:
    def __init__(self, name):
        self.name = name;
    def getName(self):
        print("我是一个有名字的土头，I 'm " + self.name)
p = Potato("pp")
p.getName()

print("===========================")
'''
    三.共有和私有：
        1.类中的共有变量，即可以通过类名.属性的方式进行访问，
          私有变量，即不可以通过类名.属性的方式进行访问
        
        2.在python内部采用了一种叫name mangling(名字改编)的方法
          定义私有变量只需要在变量名或函数名前加上"__"俩个下划线，
          那么这个变量就会变成私有的了
        
        3.想要访问私有变量必须内部访问
        
        4.python只是对双横线开头的变量的名字进行了改变，实际上在外部
         可以采用_类名__变量名的方式访问私有变量
'''

class Person:
    __name = "小甲鱼"
    
    def __init__(self, name):
        self.__name = name
    def getName(self):
        return self.__name
p = Person("哈哈")
#p.__name  会报错

print(p.getName())

print("===========================")

'''
    四.继承：
        现有一个鱼类，对鱼类细分还可以分成金鱼，鲤鱼，草鱼，鲨鱼等，
        他们的属性和行为虽然很相似，但都不大相同，但他们都属于鱼类，
        所以我们可以先创建一个鱼类，然后通过继承的方式去继承鱼类共有的行为和属性
        在继承的基础上，添加、修改属性和行为进而得到每一种的鱼的具体信息
        
        基本语法：
            class 类名(被继承的类)：
                ...
        被继承的类又称为父类, 继承者称为子类, 一个子类可以继承父类的所有属性和方法
'''
class Parent:
    def hello(self):
        print("父类中的方法")
class Child(Parent):
    def hello(self):        # 如果子类中定义与父类同名的方法和属性，则会自动翻盖父类对应的属性和方法
        print("子类中的方法")
p = Parent()
p.hello()

c = Child()
c.hello()


print("===========================")


import random as r
class Fish:
    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)
    def move(self):
        self.x -= 1
        print("我的位置是：", self.x, self.y)

class GoldFish(Fish):
    pass

class Carp(Fish):
    pass

class Salmon(Fish):
    pass
#上面三个类都是食物，不需要个性，直接继承父类

#下边定义鲨鱼类
class Shark(Fish):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有吃的^_^")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")
fish = Fish()
fish.move()
shark = Shark()
shark.eat()
shark.eat()
# shark.move() 报错，因为重写了Fish类中的__init__方法

'''
    有俩种解决方法:
        1.调用未绑定的父类方法:
        2.使用super函数:
            不需要给出父类的名字，它会自动找出所有基类以及对应的方法
'''
#1.调用未绑定的父类方法:
class Shark(Fish):
    def __init__(self):
        Fish.__init__(self) #这里的self代表的是子类Shark的实例对象
        self.hungry = True
shark = Shark()
shark.move()

#2.使用super函数
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry = True
shark = Shark()
shark.move()

print("========================")

'''
    五.多重继承：
        可以同时继承多个父类的属性和方法
        
        基本语法：
            class 类名(父类1，父类2，父类3，...)
'''
class Base1:
    def foo1(self):
        print("我是foo1,我在Base1中...")
class Base2:
    def foo2(self):
        print("我是foo2,我在Base2中...")
class C(Base1, Base2):
    pass
c = C()
c.foo1()
c.foo2()
print("========================")

'''
    六.组合：
        我们现在有鱼类，乌龟类，现在要求定义一个类，类中有乌龟和鱼，
        我们只需要在水池类中，实例化乌龟类和鱼类的对象即可
        
        在类内实例化其他类的对象叫做组合
'''
class Turtle1:
    def __init__(self, x):
        self.num = x
class Fish1:
    def __init__(self, x):
        self.num = x
class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle1(x)
        self.fish = Fish1(y)
    def print_num(self):
        print("水池里一共有乌龟 %d 只，小鱼 %d 条！" % (self.turtle.num, self.fish.num))
pool = Pool(1, 10)
pool.print_num()

print("========================")

'''
    七.类、类对象和实例对象:
        1.类中定义的是静态变量,类的属性是与类对象进行绑定，并不会依赖任何其他的实例对象
        2.实例对象引入的是类对象的属性，如果对类对象的属性进行改变，实例化对象也会跟着改变
        3.如果对实例化对象的属性值进行改变，那么该实例化对象的属性值将会覆盖类对象的属性值
        4.如果属性的名字跟方法名相同，属性会覆盖方法
'''
class Test:
    count = 0
a = Test()
b = Test()
c = Test()
print(a.count, b.count, c.count)

c.count = 10

print(a.count, b.count, c.count)

Test.count = 100

print(a.count, b.count, c.count)

c.count += 100
Test.count += 20
print(a.count, b.count, c.count)

class Test1:
    def num(self):
        print("哈哈")
a = Test1()
a.num()
a.num = 1
print(a.num)

print("=======================")

'''
    八.（BIF）内置函数：

'''
