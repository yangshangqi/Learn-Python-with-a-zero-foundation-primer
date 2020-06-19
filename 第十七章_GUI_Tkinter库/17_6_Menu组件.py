# autor: zhumenger

'''
    一.Menu组件：
        1.用于实现顶级菜单、下拉菜单和弹出菜单(如:编辑、帮助、退出等菜单)
        2.可使用add_command()方法为菜单实例添加内容
        3.可以通过add_cascade()为顶级菜单添加多级菜单
        
        4.还可以创建一个弹出的菜单，需要使用post()方法明确的显示出来
        5.通过设置tearoff为True, 可以为菜单内部添加单选按钮和多按按钮
'''

# 17_6_1.py
#
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("我被调用了")
#
# #创建一个顶级菜单
# menubar = Menu(root)
# menubar.add_command(label = "Hello", command = callback)
# menubar.add_command(label = "Quit", command = root.quit)
#
# root.config(menu = menubar)
#
# mainloop()


# 17_6_2.py 创建下拉菜单
#
# from tkinter import *
#
# root = Tk()
#
# #创建一个顶级菜单
# menubar = Menu(root)
#
# def callback():
#     print("我被调用了")
#
# #创建一个下拉菜单文件, 然后将它添加到顶级菜单中
# filemenu = Menu(menubar, tearoff = False) #tearoff = True表示可以通过点击打开这个菜单
# filemenu.add_command(label = "打开", command = callback)
# filemenu.add_command(label = "保存", command = callback)
# filemenu.add_separator() # 表示添加一个分隔符
# filemenu.add_command(label = "退出", command = root.quit)
# menubar.add_cascade(label = "文件", menu = filemenu)
#
# #创建另一个下拉菜单"编辑", 然后将它添加到顶级菜单中
# editmenu = Menu(menubar, tearoff = False)
# editmenu.add_command(label = "剪切", command = callback)
# editmenu.add_command(label = "拷贝", command = callback)
# editmenu.add_command(label = "粘贴", command = callback)
# menubar.add_cascade(label = "编辑", menu = editmenu)
#
# root.config(menu = menubar)
# mainloop()


# 17_6_3.py
#
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("我被调用了")
#
# #创建一个弹出菜单
# menu = Menu(root, tearoff = False)
# menu.add_command(label = "撤销", command = callback)
# menu.add_command(label = "重做", command = callback)
#
# frame = Frame(root, width = 512, height = 512)
# frame.pack()
#
# def popup(event):
#     menu.post(event.x_root, event.y_root) #在鼠标点击的位置处弹出
#
# #绑定鼠标右键
#
# frame.bind("<Button-3>", popup)
#
# mainloop()


# 17_6_4.py
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("~被调用了~")
#
# # 创建一个顶级菜单
# menubar = Menu(root)
#
# # 创建 checkbutton 关联变量
# openVar = IntVar()
# saveVar = IntVar()
# exitVar = IntVar()
#
# # 创建一个下拉菜单“文件”，然后将它添加到顶级菜单中
# filemenu = Menu(menubar, tearoff=True)
# filemenu.add_checkbutton(label="打开", command=callback, variable=openVar)
# filemenu.add_checkbutton(label="保存", command=callback, variable=saveVar)
# filemenu.add_separator()
# filemenu.add_checkbutton(label="退出", command=root.quit, variable=exitVar)
# menubar.add_cascade(label="文件", menu=filemenu)
#
# # 创建 radiobutton 关联变量
# editVar = IntVar()
# editVar.set(1)
#
# # 创建另一个下拉菜单“编辑”，然后将它添加到顶级菜单中
# editmenu = Menu(menubar, tearoff=True)
# editmenu.add_radiobutton(label="剪切", command=callback, variable=editVar, value=1)
# editmenu.add_radiobutton(label="拷贝", command=callback, variable=editVar, value=2)
# editmenu.add_radiobutton(label="粘贴", command=callback, variable=editVar, value=3)
# menubar.add_cascade(label="编辑", menu=editmenu)
#
# # 显示菜单
# root.config(menu=menubar)
#
# mainloop()


'''
    二.Menubutton组件：
        1.该组件是一个与Menu相关联的按钮, 它可以放在窗口的任意位置, 再被按下按钮时弹出下拉菜单
          常用于希望将菜单按钮出现在其他位置的时候
'''


# 17_6_5.py
#
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     print("我被调用了")
#
# #relief表示浮雕样式：FLAT:平的, RAISED: 凹陷的，RIDGE:凸起的 ...
# mb = Menubutton(root, text = "点我", relief = RAISED)
# mb.pack()
#
# filemenu = Menu(mb, tearoff = False)
# filemenu.add_checkbutton(label = "打开", command = callback, selectcolor = "yellow")
# filemenu.add_command(label = "保存", command = callback)
# filemenu.add_separator()
# filemenu.add_command(label = "退出", command = root.quit)
# mb.config(menu = filemenu)
#
# mainloop()


'''
    三.OptionMenu组件
        选项菜单组件：能够显示选中的那个选项
        可以使用get()方法获得用户选择的选项
        
        如果有很多的选项，可以将选项都写入到列表中去，在选项菜单组件中引入该列表的解包即可
'''

# 17_6_6.py
#
# from tkinter import *
#
# root = Tk()
#
# variable = StringVar()
# variable.set("one")
#
# def callback():
#     print(variable.get())
#
# w = OptionMenu(root, variable, "one", "two", "three")
# w.pack()
#
# Button(root, text = "点我", command = callback).pack()
# mainloop()


# 17_6_7.py
#
# from tkinter import *
#
# root = Tk()
#
# OPTIONS = [
#     "one",
#     "two",
#     "three",
#     "four",
#     "five",
#     "six"
# ]
#
# variable = StringVar()
# variable.set(OPTIONS[0])
# mb = OptionMenu(root, variable, *OPTIONS)
# mb.pack()
#
# def callback():
#     print(variable.get())
#
# Button(root, text = "点我", command = callback).pack()
#
# mainloop()