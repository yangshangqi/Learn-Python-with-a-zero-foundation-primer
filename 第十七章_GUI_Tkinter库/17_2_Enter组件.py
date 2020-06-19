# autor: zhumenger
# autor: zhumenger
'''
    Enter组件：
        1.即输入框, 可通过inster()和delete()方法更改输入框中的内容
          可以使用get()方法获取输入框中的信息
        2.设计密码框, 将show参数的属性改为'*' 表示以指定的字符显示
'''

# 17_2_1.py
#
# from tkinter import *
#
# root = Tk()
#
# e = Entry(root)
# e.pack(padx = 20, pady = 20)
# e.delete(0, END)
# e.insert(0, "要想练就绝世武功！")
# mainloop()


# 17_2_2.py
#
# from tkinter import *
#
# root = Tk()
#
# #Tkinter总共提供了3中组件布局的方法:pack() grid(), place()
# #gird()方法允许用表格的方式来管理组件的位置
# #row 表示行, column 表示列
#
# Label(root, text ="作品").grid(row = 0)
# Label(root, text ="作者").grid(row = 1)
#
# e1 = Entry(root)
# e2 = Entry(root)
# e1.grid(row = 0, column = 1, padx=10, pady=5)
# e2.grid(row = 1, column = 1, padx = 10, pady = 5)
#
# def show():
#     print("作品：《%s》" % e1.get())
#     print("作者：%s" % e2.get())
#     e1.delete(0, END)
#     e2.delete(0, END)
#
# #对于表格，使用sticky来设置组件的位置，N W S E ..
# Button(root, text = "获取信息", width = 10, command = show).grid(row = 3, column = 0, sticky=W, padx = 10, pady = 5)
# Button(root, text = "退出", width = 10, command = root.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
# mainloop()


# 17_2_3.py 设置密码框
#
# from tkinter import *
#
# root = Tk()
#
# Label(root, text ="账号").grid(row = 0)
# Label(root, text ="密码").grid(row = 1)
#
# v1 = StringVar()
# v2 = StringVar()
#
# e1 = Entry(root, textvariable = v1)
# e2 = Entry(root, textvariable = v2, show = "*")
# e1.grid(row = 0, column = 1, padx=10, pady=5)
# e2.grid(row = 1, column = 1, padx = 10, pady = 5)
#
# def show():
#     print("账号：%s" % v1.get())
#     print("密码：%s" % v2.get())
#     e1.delete(0, END)
#     e2.delete(0, END)
#
# #对于表格，使用sticky来设置组件的位置，N W S E ..
# Button(root, text = "芝麻开门", width = 10, command = show).grid(row = 3, column = 0, sticky=W, padx = 10, pady = 5)
# Button(root, text = "退出", width = 10, command = root.quit).grid(row = 3, column = 1, sticky = E, padx = 10, pady = 5)
# mainloop()


'''
        3.Enter组件支持验证输入内容的合法性, 通过设置组件的事件以及触发函数
            validate参数:
                        facus: 失去或获得焦点时验证
                        facusin: 获得焦点时验证
                        facusout: 失去焦点时验证
                        key: 输入框被编辑时验证
                        none: 默认值，关闭验证功能
            validatecommand: 指定一个验证的函数，只能返回True或false
            invalidatecommand: 只有在validatecommand返回值为false时才会被调用
'''


# 17_2_4.py Enter组件支持验证输入内容的合法性
# from tkinter import *
#
# root = Tk()
#
# def test():
#     if e1.get() == "小甲鱼":
#         print("正确！")
#         return True
#     else:
#         print("错误！")
#         e1.delete(0, END)
#         return False
#
# v = StringVar()
#
# e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=test)
# e2 = Entry(root)
# e1.pack(padx=10, pady=10)
# e2.pack(padx=10, pady=10)
#
# mainloop()


'''
    4.Tkinter为验证函数提供了一些额外的选项:
        %p:输入框中的内容
        %v:该组件当前的validate选项的值
        %W:该组件的名字
        
        用法：validatecommand = (f, s1, s2, s3, ...)
        f为验证函数, s1, s2, s3为额外的选项, 这些选项会作为参数依次传给f
        在此之前，要使用 register()方法 将验证函数封装起来
'''

# 17_2_5.py
# from tkinter import *
#
# root = Tk()
#
# v = StringVar()
#
# def test(content, reason, name):
#     if content == "小甲鱼":
#         print("正确！")
#         print(content, reason, name)
#         return True
#     else:
#         print("错误！")
#         print(content, reason, name)
#         return False
#
# testCMD = root.register(test)
# e1 = Entry(root, textvariable=v, validate="focusout", validatecommand=(testCMD, '%P', '%v', '%W'))
# e2 = Entry(root)
# e1.pack(padx=10, pady=10)
# e2.pack(padx=10, pady=10)
#
# mainloop()