# autor: zhumenger
'''
    官方御用GUI工具包：Tkinter
'''


# 17_1.py Tkinter初体验
#import tkinter as tk
#
#root = tk.Tk()             #创建一个主窗口, 用于容纳整个GUI程序
#root.title("I Love You")   #设置主窗口对象的标题栏
#
# #添加一个Label组件, Label组件是GUI程序中最常用的组件之一
# #Label组件可以显示文本、图标或者图片
# #在这里让它显示文本
# theLabel = tk.Label(root, text = "我的第二个窗口程序")
# #该方法用于自动调节组件自身的尺寸
#theLabel.pack()
#进入主事件循环
#root.mainloop()



# 17_2.py 封装成类的写法
#
# import tkinter as tk
#
# class App:
#     def __init__(self, root):
#         #在主窗口里面添加一个框架
#         frame = tk.Frame(root)
#
#         #修改pack()方法中的side参数，可以改变该按钮框架在主窗口中的位置
#         #side参数可以设置为LEFT RIGHT TOP BOTTOM 四个方位, 默认side = thinter.TOP
#
#         #使用pack()方法的padx 和pady 参数自定义按钮的偏移位置,
#         #设置bg即background 背景色
#         frame.pack()
#
#         #在框架里创建一个按钮组件, fg就是foreground的缩写, 设置前景色的意思
#         self.hi_there = tk.Button(frame, text = "打招呼", bg = "black", fg = "white", command = self.say_hi)
#         self.hi_there.pack()
#     def say_hi(self):
#         print("互联网的广大朋友们大家好, 我是小甲鱼!")
# #创建主窗口
# root = tk.Tk()
# app = App(root)
# root.mainloop()

'''
    3.Lable组件
'''

# 17_3_1.py Lable组件用于在界面上输出描述的标签
#
# import tkinter as tk
#
# root = tk.Tk()
#
# #文字默认左对齐居中, 可用jusity设置文字向左对齐，并用pdax设置与左边框的距离
# textLabel = tk.Label(root, text = "风浪没平息\n我宣告奔跑的意义\n这不是叛逆\n我只是淋了一场雨.",  padx = 10, justify = tk.LEFT)
# textLabel.pack(side = tk.LEFT)
#
# #创建一个图像Label对象
# #用PhotoImage实例化一个图片对象(仅支持gif格式的图片)
# photo = tk.PhotoImage(file = "dongman.gif")
# imgLabel = tk.Label(root, image = photo)
# imgLabel.pack(side = tk.RIGHT)
# root.mainloop()


#17_3_2.py Label组件 将图片作为背景，文字显示在图片上面
#
# from tkinter import *
#
# root = Tk()
# photo = PhotoImage(file = "dongman.gif")
# theLabel = Label(root,
#                  text = "风浪没平息\n我宣告奔跑的意义.",
#                  image=photo,
#                  compound=CENTER,   #设置文本和图像混合模式
#                  font=("华康少女字体", 20), #设置字体和字号
#                  fg = "white")   #设置文本颜色
# theLabel.pack()
# mainloop()


'''
    4.Button组件:
        Button按钮组件, 可以接收用户选择的信息
        有一个command参数，用于指定一个函数，当用户点击这个按钮时, Tkinter就会自动调用这个函数
        
        我们在使用界面编程的时候，有些时候是需要跟踪变量的值的变化，以保证值的变更随时可以
        显示在界面上。由于python无法做到这一点，所以使用了tcl的相应的对象，
        也就是StringVar、BooleanVar、DoubleVar、IntVar所需要起到的作用
'''

# 17_4_1.py
#
# from tkinter import *
#
# def callback():
#     var.set("我才不信呢！")
#
# root = Tk()
#
# frame1 = Frame(root)
# frame2 = Frame(root)
#
# #创建一个文本Label对象
# var = StringVar()
# var.set("您所下载的影片含有未成年人限制内容, \n请满18岁后在单击观看！")
# textLabel = Label(frame1, textvariable = var, justify = LEFT)
# textLabel.pack(side = LEFT)
#
# #创建一个图像Label对象
# #用PhotoImage实例化一个对象
# photo = PhotoImage(file = "dongman.gif")
# imgLabel = Label(frame1, image=photo)
# imgLabel.pack(side = RIGHT)
#
# #添加一个按钮
# theButton = Button(frame2, text = "已满18周岁", command = callback)
# theButton.pack()
#
# frame1.pack(padx = 10, pady = 10)
# frame2.pack(padx = 10, pady = 10)
# mainloop()


'''
    5.Checkbutton组件：
        多选按钮, RadiobuttonWie单选按钮
        如果选中，值为1，否则值为0
'''

# 17_5_1.py
#
# from tkinter import *
#
# root = Tk()
#
# #用来查看按钮是否被选
# v = IntVar()
#
# c = Checkbutton(root, text = "点我啊!", variable = v)
# c.pack()
#
# #为了查看效果，使用Label标签显示
# label = Label(root, textvariable = v)
# label.pack()
# mainloop()


# 17_5_2.py
#
# from tkinter import *
#
# root = Tk()
#
# GIRLS = ["西施", "王昭君", "貂蝉","杨玉环"]
# v = []
#
# for girl in GIRLS:
#     v.append(IntVar())
#     b = Checkbutton(root, text = girl, variable = v[-1])
#
#     #可以通过设置anchor参数的属性值，调整组件的对其方式, 有N NE E ES S SW W WN(指南针) 和 CENTER 9种方向
#     b.pack(anchor = W)
# mainloop()


'''
    6.Radiobutton组件
        多个按钮实现单选效果
        同一组的所有按钮只能共享一个variable选项
        并且需要设置不同的value选项
'''

# 17_6_1.py
#
# from tkinter import *
#
# root = Tk()
# v = IntVar()
#
# Radiobutton(root, text = "One", variable = v, value = 1).pack(anchor=W)
# Radiobutton(root, text = "Two", variable = v, value = 2).pack(anchor=W)
# Radiobutton(root, text = "Three", variable = v, value = 3).pack(anchor=W)
#
# mainloop()


# 17_6_2.py 如果有多个选项，可用循环实现, 高效简洁
#
# from tkinter import *
#
# root = Tk()
#
# LANGS = [
#     ("python", 1),
#     ("Per1", 2),
#     ("Ruby", 3),
#     ("Lua", 4)]
# v = IntVar()
# v.set(1)
#
# for lang, num in LANGS:
#
#     #将indicatoron设为false可去掉前面的小圆圈,转化为按钮的形式
#     b = Radiobutton(root, text = lang, variable = v, value = num, indicatoron = False)
#     b.pack()
# mainloop()


'''
    7.LabelFrame组件
        该组件是Label组件的升级版, 即添加了frame框架的Label
'''

# 17_7_1.py 可以将按钮都添加到LabelFrame框架中去
# from tkinter import *
#
# root = Tk()
#
# group = LabelFrame(root, text = "风浪没平息\n我宣告奔跑的意义.", padx = 5, pady = 5)
# group.pack(padx = 10, pady = 10)
#
# LANGS = [
#     ("python", 1),
#     ("Per1", 2),
#     ("Ruby", 3),
#     ("Lua", 4)]
# v = IntVar()
# v.set(1)
#
# for lang, num in LANGS:
#     b = Radiobutton(group, text = lang, variable = v, value = num)
#     b.pack(anchor=W)
# mainloop()