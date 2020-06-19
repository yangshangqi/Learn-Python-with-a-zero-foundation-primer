# autor: zhumenger

'''
    一.Message组件:
        是Label组件的变体, 用于显示多行文本消息
        可以自动换行，并调整文本的尺寸
'''

# 17_7_1.py
#
# from tkinter import *
#
# root = Tk()
#
# w1 = Message(root, text = "这是一则消息", width = 100)
# w1.pack()
#
# w2 = Message(root, text = "我祈祷拥有一颗透明的心灵和会流泪的眼睛", width = 100)
# w2.pack()
#
# mainloop()


'''
    二.Spinbox组件：
        是Enter组件的变体，用于从固定的值中选取一个，
        可以通过范围或元组指定用户输入想内容
'''

# 17_7_2.py
#
# from tkinter import *
#
# root = Tk()
#
# # 设置范围
# w1 = Spinbox(root, from_ = 0, to = 10)
# w1.pack()
#
# #通过元组设置内容
# w2 = Spinbox(root, value = ("one", "two", "three"))
# w2.pack()
# mainloop()


'''
    三.PanedWindow组件
        是一个空间管理组件，与frame组件类似,都是为组件提供一个框架
        不过PanedWindow允许让用户调整应用程序的空间划分
'''

# 17_7_3.py
#
# from tkinter import *
#
# m = PanedWindow(orient = VERTICAL) #设置方向为垂直方向
# m.pack(fill = BOTH, expand = 1)
#
# top = Label(m, text = "top pane")
# m.add(top)
#
# bottom = Label(m, text = "bottom pane")
# m.add(bottom)
#
# mainloop()


# 17_7_4.py 创建一个3个窗格的PanedWindow组件
#
# from tkinter import *
#
# #各个窗格之间实际上是有一条看不见的线
# #可以通过设置showhandle = True让其显示出来
# m1 = PanedWindow(showhandle = True, sashrelief = SUNKEN)
# m1.pack(fill = BOTH, expand = 1)
#
# left = Label(m1, text = "left pane")
# m1.add(left)
#
# m2 = PanedWindow(orient = VERTICAL, showhandle = True, sashrelief = SUNKEN)
# m1.add(m2)
#
# top = Label(m2, text = "top pane")
# m2.add(top)
#
# bottom = Label(m2, text = "bottom pane")
# m2.add(bottom)
#
# mainloop()


'''
    四.Toplevel组件
        1.独立的顶级窗口组件，类似与frame组件，但该组件拥有标题栏，边框等部件
          该组件通常用在显示额外的窗口、对话框和其他弹出窗口中
        2.可以通过设置attribute()这个方法，用于设置和获取窗口属性
          如果只给出选项名，那么将返回当前窗口该选项的值
          选项不支持关键字参数，需要在选项前加横线(-)，并用字符串表示
          用逗号(,)隔开选项和值
'''


# 17_7_5.py 创建一个顶级窗口
#
# from tkinter import *
#
# root = Tk()
#
# def create():
#     top = Toplevel()
#     top.title("I LOVE YOU!")
#     top.attributes('-alpha', 0.5) #将窗口设置为50%透明度
#
#     msg = Message(top, text = "I LOVE MYSELF!!!")
#     msg.pack()
#
# Button(root, text = "创建顶级窗口", command = create).pack()
#
# mainloop()


