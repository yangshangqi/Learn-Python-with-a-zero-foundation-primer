# autor: zhumenger

'''
    布局管理器：
        用于管理组件如何排列的工具
        有三个布局管理器，分别是pack, grid, place
        pack：是按添加顺序排列组件
            参数：
              fill: 表示组件填充的空间
                  BOTH表示同时向横向和纵向扩展
                  X表示横向
                  Y表示纵向
              expand = True: 表示将父组件的额外空间也填满
              side: 表示组件相对于父组件所在的位置
                TOP: 顶部
                BOTTOM：尾部
                LEFT：左部
                RIGHT：右部
            anchor:表示组件相对于所分配空间所在的位置
                值有: W S N E
        grid 是按行/列形式排列组件
            参数：
                row: 表示选定组件所在的行数
                column: 表示选定组件所在的列数
                rowspan: 表示跨行
                columnspan: 表示跨列
                sticky: 可以设置组件在网格中的位置(默认居中)
                    可以使用的值有：E W S N（表示东、西、南、北）以及他们的组合
        place 允许程序员指定组件的大小和位置
            relx, relx: 表示相对于父组件的位置, 范围是00-1.0 0.5表示正中间
            relwidth, relheight: 表示相对于父组件的尺寸
'''


# 17_9_1.py
#
# from tkinter import *
#
# root = Tk()
#
# #默认情况下pack将添加的组件纵向排列
# # Label(root, text = "red", bg = "red", fg = "white").pack(fill = X)
# # Label(root, text = "Green", bg = "Green", fg = "black").pack(fill = X)
# # Label(root, text = "Blue", bg = "blue", fg = "white").pack(fill = X)
#
# #通过设置side参数调整组件的位置，使组件横向挨着排列
# Label(root, text = "red", bg = "red", fg = "white").pack(side = LEFT)
# Label(root, text = "Green", bg = "Green", fg = "black").pack(side = LEFT)
# Label(root, text = "Blue", bg = "blue", fg = "white").pack(side = LEFT)
# mainloop()


#17_9_2.py
#
# from tkinter import *
#
# root = Tk()
#
# Label(root, text = "用户名").grid(row = 0)
# Label(root, text = "密码").grid(row = 1, sticky = W)
#
# Entry(root).grid(row = 0, column = 1)
# Entry(root, show = "*").grid(row = 1, column = 1)
#
# photo = PhotoImage(file = "dongman.gif")
# Label(root, image = photo).grid(row = 0, column = 2, rowspan = 2, padx = 5, pady = 5)
#
# Button(text = "提交", width = 10).grid(row = 2, columnspan = 3, pady = 5)
# mainloop()


# 17_9_3.py
#
# from tkinter import *
#
# root = Tk()
#
# Label(root, bg = "red").place(relx = 0.5, rely = 0.5, relwidth = 0.75, relheight = 0.75, anchor = CENTER)
# Label(root, bg = "yellow").place(relx = 0.5, rely = 0.5, relwidth = 0.5, relheight = 0.5, anchor = CENTER)
# Label(root, bg = "green").place(relx = 0.5, rely = 0.5, relwidth = 0.25, relheight = 0.25,anchor = CENTER)
#
# mainloop()


'''
    标准对话框：
        Tkinter提供了3种标椎对话框：messagebox, filedialog, colorchooser
        
'''

# 17_9_4.py 使用文件对话框打开文件,颜色对话框选择颜色
# import tkinter.filedialog
# import tkinter.colorchooser
# from tkinter import *
#
# root = Tk()
#
# def callback():
#     filename = filedialog.askopenfilename()
#     print(filename)
#
# def callback1():
#     filename = colorchooser.askcolor()
#     print(filename)
#
# Button(root, text = "打开文件", command = callback).pack()
# Button(root, text = "选择颜色", command = callback1).pack()
# mainloop()