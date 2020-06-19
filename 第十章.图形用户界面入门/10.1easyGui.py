# autor: zhumenger
'''
    一.GUI（Graphical user interface）:图形用户界面
        带有按钮、文本、输入框的窗口的编程
        调用 easygui 的 egdemo() 函数可以尝试easygui拥有的各种功能
'''
#10.1.1py easygui的简单使用
#import easygui as g
#import sys
# g.msgbox("嗨,大家好TvT", '介绍', '你好')
# while 1:
#     g.msgbox("嗨，欢迎进入第一个界面小游戏")
#     msg = "请问你希望在鱼c工作室学习到什么知识呢？"
#     title = "小游戏活动"
#     choices = ["谈恋爱","编程", "demo", "琴棋书画"]
#     choice = g.choicebox(msg, title, choices)
#     g.msgbox("你的选择是" + str(choice), "结果")
#
#     msg = "你希望重新开始小游戏吗？"
#     title = "请选择"
#     if g.ccbox(msg, title):
#         pass;
#     else:
#         sys.exit(0)
# autor: zhumenger

#10.1.2.py
# print(g.egdemo())
# g.msgbox("你好啊！", "嘻嘻")

# 如何跳过第二个参数，直接设置第三个参数：使用关键字参数即可
# choices = ['愿意', '不愿意', '有钱的时候愿意']
# g.choicebox("你愿意玩吗？", choices = choices)


'''
    二.使用按钮组件
        对于Easygui的所有对话框而言，前俩个参数都是消息主体和对话框标题
        1.msgbox组件:
            msgbox(msg='(Your message goes here)', title=' ', ok_button='OK', image=None, root=None)
            第一个参数为文本信息，第二个参数为标题，第三个参数为按钮的信息

        2、ccbox()组件:
            ccbox(msg='Shall I continue?', title=' ', choices=('Continue', 'Cancel'), image=None)
            ccbox() 提供一个选择：Continue 或者 Cancel，并相应的返回 1（选中Continue）或者 0（选中Cancel）

        3.choicebox()组件：
            choicebox(msg='Pick something.', title=' ', choices=())
        4.buttonbox():自定义一组按钮,并返回所选的内容信息
          indexbox()；返回所选按钮的索引值，第一个按钮为0，第二个按钮为1
          boolbox():若第一个按钮被选中返回True，否则返回false
'''

#10.2.1.py 在buttonbox里边显示图片，图片格式为gif或png
# g.buttonbox('好漂亮的小姐姐！', image = 'preview10.jpg', choices = ('哇，好美啊!', '哇, 我好喜欢'))

'''
    三.让用户输入消息
        1).enterbox(msg = "Enter something.", title = '', default = '', strip = True, image = None, root = None):
            该组件提供一个简单的输入框，会自动去掉首位空格，如果需要保留，则将strip参数设为false
        2).integerbox(msg = "", title = '', default = None, lowerbound = 0, upperbound = 99, image = None, root = None):
            用户只能在指定范围内输入的信息
        3).multenterbox(msg, title, fields = [], values = [], callback = None, run = True):
            为用户提供多个简单的输入框：
            1.如果用户没有将所有的选项填完，则将用空字符串替代
            2.如果用户取消操作，则返回域中列表的值或者None值
            3.fields 为输入框的提示信息 values 为输入框中的默认信息
'''

#10.3.1.py
#import easygui as g
# msg = g.enterbox("你有什么话想对我说嘛？")
# print(msg)

# import random
# g.msgbox("嗨, 欢迎进入第一个界面小游戏^_^")
# secret = random.randint(1, 10)
# msg = "不妨猜一下我现在想的是哪个数字(1 ~ 10)"
# title = "小游戏"
# guess = g.integerbox(msg, title, lowerbound = 1, upperbound = 10)
# while True:
#     if(guess == secret):
#         g.msgbox("太厉害了！,看来我们是心有灵犀啊^V^")
#         break
#     else:
#         if(guess > secret):
#             g.msgbox("猜大了")
#         else:
#             g.msgbox("猜小了")
#         guess = g.integerbox(msg, title, lowerbound = 1, upperbound = 10)
# g.msgbox("游戏结束")



#10.3.2.py 实现一个账号资料登记程序
#
# import easygui as g
# msg = "请填写以下联系方式"
# title = "账号中心"
# fieldNames = ['*用户名', '*真实姓名', ' 固定电话', '*手机号码', ' QQ', '*E-mail']
# fieldValues = []
# fieldValues = g.multenterbox(msg, title, fieldNames)
# while 1:
#     if fieldValues == None:
#         break;
#     errmsg = ''
#     for i in range(len(fieldNames)):
#         option = fieldNames[i].strip()
#         if fieldValues[i].strip() == '' and option[0] == '*':
#             errmsg += ('[%s]为必填项.\n\n'%fieldNames[i])
#     if errmsg == '':
#         break
#     fieldValues = g.multenterbox(errmsg, title, fieldNames, fieldValues)
# print("用户资料如下：%s" % str(fieldValues))

'''
    四.让用户输入密码：
        1).passwordbox(msg = "", title = '', default = '', image = None, root = None)
            用户输入的内容用*表示
        2).mulpasswprdboxx(msg, title, fields = [], values = [], callback = None, run = True)
            多个输入框，最后一个输入框用*表示
'''

#10.4.1.py
# import easygui as g
# g.passwordbox("请输入密码")
# g.multpasswordbox("请输入用户名和密码", title = "登录", fields = ['用户名', '密码'])


'''
    五.显示文本
        1).testbox(msg, title, text = '', codebox = False, callback = None, run = True)
            参数callback设置字体宽度,
'''

#10.5.1.py
# import easygui as g
# file = open('text.txt', 'rb')
# g.textbox('文件text.txt的内容如下:', text = file.read().decode('utf-8'))


'''
    六.目录与文件：
        1).diropenbox(msg, title, default = None)
            用于提供一个对话框，返回用户选择的目录名，如果用户选择Cancle,则返回None
        2).fileopenbox(msg, title, default = '*', filetypes = None, multiple = False)
            提供一个对话框，用于返回用户选择的文件名, 如果用户选择Cancel,则返回None
        关于default参数的设置方法：
            (1).指定一个默认的路径，通常包括一个或多个通配符
            (2).default默认的参数是'*'，即匹配所有格式的文件，例如：
                default = 'c/fishc/*.py' 就会显示c/fishc文件夹下所有的.py源文件
                default = 'c/fishc/test*.py' 就会c/fishc文件夹下所有名字以test开头的文件
        3).filesavebox(msg, title, default, filetypes = None)
            提供一个对话框，用于选择文件需要保存的路径,
            default 参数应该包含一个文件名.
'''
# import easygui as g
# g.fileopenbox(default = 'F:\python代码文件\小甲鱼入门学习\第十章.图形用户界面入门/*.py',multiple = False)


'''
    七.捕捉异常
        使用exceptionbox()会将堆栈追踪显示在一个codebox()中
'''

# import easygui as g
# try:
#     print("TVT")
#     int('asd')
# except:
#     g.exceptionbox()


'''
    八.记住用户的设置
        python中提供了一个名为EgStore的类, 可以以对用户的设置进行存储和恢复
'''

#10.8.1.py
#from easygui import EgStore
#
#定义一个名为Settings的类，继承自EgStore类
# class Settings(EgStore):
#     def __init__(self, filename):
#         self.author = ""
#         self.book = ""
#
#         self.filename = filename
#         self.restore()
# settingsFilename = 'settings.txt'
# settings = Settings(settingsFilename)
# author = "小甲鱼"
# book = "《零基础入门学习python》"
#
# settings.author = author
# settings.book = book
#
# settings.store()#保存完毕
# print("保存完毕")
#
# #取回之前设置的参数,只需要再次实例化对象即可：
# settingsFilename = 'settings.txt'
# settings = Settings(settingsFilename)
# print(settings.author)

