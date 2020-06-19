# autor: zhumenger

'''

    Canvas组件：
        1.画布组件，通常用于显示和编辑图形，可以用它来绘制直线，圆形，多边形甚至是绘制其他组件
        2.在Canvas组件上绘制对象，可以用create_xxx()方法(xxx表示对象类型，例如直线line，矩形rectangle和文本text等)
        3.可以使用coords()、itemconfig()方法和move()方法来移动画布上的对象，使用delete()方法删除
        4.还可以在Canvas上显示文本, 使用create_text()方法
        5.使用create_oval()方法绘制椭圆, 参数为一个限定矩形，Tkinter会自动在这个矩形内绘制椭圆
          要想绘制圆形，只需要将限定矩形设置为正方形即可
        6.绘制多边形，可以使用create_polygon()方法
        
        7.Canvas并没有提供画"点"的方法,但是我们可以用超小的椭圆,通过"鼠标左键按住拖动"事件(<B1-Motion>)
          在鼠标拖动的同时获取鼠标的实时位置，进而实现画图
'''

# 17_5_1.py
#
# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width = 300, height = 100)
# w.pack()
#
# #画一条黄色的横线
# line1 = w.create_line(0, 50, 200, 50, fill = "yellow") #设置直线的起始坐标和终点坐标
# #画一条红色的竖线
# line2 = w.create_line(100, 0, 100, 100, fill = "red", dash = (4, 4)) #设置为虚线
# #中间画一个蓝色的矩形
# rect = w.create_rectangle(50, 25, 150, 75, fill = "blue") #设置左上角的坐标以及右下角的坐标
# #添加文本信息
# w.create_text(100, 50, text = "I LOVE YOU!")
#
# #移动、改变、删除
# w.coords(line1, 0, 25, 200, 25)
# w.itemconfig(rect, fill = "red")
# w.delete(line2)
#
# mainloop()


# 17_5_2.py #绘制椭圆
#
# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width = 300, height = 100)
# w.pack()
#
# w.create_rectangle(40, 20, 160, 80, dash = (4, 4))
# w.create_oval(40, 20, 160, 80, fill = "pink")
# w.create_text(100, 50, text = "I LOVE YOU!")
#
# mainloop()


# 17_5_3.py 绘制五角星
#
# from tkinter import *
# import math as m
#
# root = Tk()
#
# w = Canvas(root, width = 200, height = 100, background = "red")
# w.pack()
#
# center_x = 100
# center_y = 50
# r = 50
#
# points = [
#     #左上点
#     center_x - int(r * m.sin(2 * m.pi / 5)),
#     center_y - int(r * m.cos(2 * m.pi / 5)),
#     #右上点
#     center_x + int(r * m.sin(2 * m.pi / 5)),
#     center_y - int(r * m.cos(2 * m.pi / 5)),
#     #左下点
#     center_x - int(r * m.sin(m.pi / 5)),
#     center_y + int(r * m.cos(m.pi / 5)),
#     #顶点
#     center_x,
#     center_y - r,
#     #右下点
#     center_x + int(r * m.sin(m.pi / 5)),
#     center_y + int(r * m.cos(m.pi / 5)),
# ]
#
# w.create_polygon(points, outline = "green", fill = "yellow")
#
# mainloop()


# 17_5_4.py 实现画板功能
#
# from tkinter import *
#
# root = Tk()
#
# w = Canvas(root, width = 400, height =200)
# w.pack()
#
# def paint(event):
#     x1, y1 = (event.x - 1), (event.y - 1)
#     x2, y2 = (event.x + 1), (event.y + 1)
#     w.create_oval(x1, y1, x2, y2, fill = "red")
# w.bind("<B1-Motion>", paint)
#
# Label(root, text = "按住鼠标左键并移动，开始绘制你的理想蓝图吧...").pack(side = BOTTOM)
#
# mainloop()