# autor: zhumenger

'''
    Listbox组件：
        内容以列表的形式显示出来, 并支持滚动条操作,
        使用insert()方法添加文本
        ACTIVE表示当前被选中的项目
'''

# p17_3_1.py
# from tkinter import *
#
# root = Tk()
#
# # 创建一个空列表
# theLB = Listbox(root)
# theLB.pack()
#
# # 往列表里添加数据
# for item in ["钢铁侠", "蜘蛛侠", "绿灯侠", "神奇女侠"]:
#     theLB.insert(END, item)
#
#为这个按钮设置一个点击事件
# theButton = Button(root, text="删除", command=lambda x=theLB: x.delete(ACTIVE))
# theButton.pack()
#
# mainloop()

'''
    Scrollbar组件
        滚动条组件，常与其他组件配合使用
        
        安装垂直滚动条：
            (1).设置该组件的yscrollcommand选项为Scrollbar组件的set()方法
            (2).设置Scrollbar组件的command选项为该组件的yview()方法
'''

# 17_3_2.py
#
# from tkinter import *
#
# root = Tk()
# sb = Scrollbar(root)
# sb.pack(side = RIGHT, fill = Y)
# lb = Listbox(root, yscrollcommand = sb.set)
# for i in range(100):
#     lb.insert(END,i)
#
# lb.pack(side = LEFT, fill = X)
# sb.config(command = lb.yview)
# mainloop()

'''
    Scale组件：
        1.能创建一个可以显示指定范围的滚动条组件
         只需要指定它的from_和to俩个参数指定范围即可
         滚动条默认为垂直方向，可设置orient参数为HORIZONTAL设置为水平方向
        
        2.使用get方法可获取当前滚动条的位置
        
        3.还可以通过resolution选项控制分辨率(步长)，通过tickinterval选项设置刻度
        
        
'''

# 17_3_3.py
#
# from tkinter import *
#
# root = Tk()
#
# Scale(root, from_ = 0, to = 42).pack()
# Scale(root, from_ = 0, to = 200, orient = HORIZONTAL).pack()
#
# mainloop()


# 17_3_4.py使用get方法可获取当前滚动条的位置
#
# from tkinter import *
#
# root = Tk()
# s1 = Scale(root, from_ = 0, to = 40)
# s1.pack()
# s2 = Scale(root, from_ = 0, to = 200, orient = HORIZONTAL)
# s2.pack()
# def show():
#     print(s1.get(), s2.get())
# Button(root, text = "获取位置", command = show).pack()
#
# mainloop()


# 17_3_5.py 还可以通过resolution选项控制分辨率(步长)，通过tickinterval选项设置刻度
#
# from tkinter import *
#
# root = Tk()
#
# Scale(root, from_ = 0, to = 42, tickinterval = 5, length = 200, resolution = 5).pack()
# Scale(root, from_ = 0, to = 200, tickinterval = 10, length = 600, orient = HORIZONTAL).pack()
#
# mainloop()

