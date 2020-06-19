# autor: zhumenger

'''
    一.事件绑定
        1.对于每个组件，可以通过bind()方法将函数或方法绑定到具体的事件上,
'''

# 17_8_1.py
#
# from tkinter import *
#
# root = Tk()
#
# def callback(event):
#     print("单击的位置是", event.x, event.y)
#
# frame = Frame(root, width = 200, height = 200)
# frame.bind('<Button-1>', callback)
# frame.pack()
#
# mainloop()


# p17_8_2.py
# 捕获键盘事件
# from tkinter import *
#
# root = Tk()
#
# def callback(event):
#     print("敲击位置：", repr(event.char))
#
# frame = Frame(root, width=200, height=200)
# frame.bind("<Key>", callback)
# frame.focus_set()
# frame.pack()
#
# mainloop()


# p17_8_3.py
# from tkinter import *
#
# root = Tk()
#
# def callback(event):
#     print("当前位置：", event.x, event.y)
#
# frame = Frame(root, width=200, height=200)
# frame.bind("<Motion>", callback)
# frame.pack()
#
# mainloop()

'''
    二.事件序列
        1.事件序列以字符串的形式表示，可以表示一个或多个相关联的事件
        2.事件序列语法描述：<modifier-type-detail>
          
          modifier部分的内容是可选的，它通常用于描述组合键，如：ctrl+c, ctrl + v, shift + 单击
          type部分是最重要的，通常用于描述普通的事件类型，如鼠标单击，键盘点击等
          detail部分内容是可选的，通常用于描述具体的按键，如：Button-1表示鼠标左键
          
          事件序列语法示例：
            <Button-1> 表示用户单击
            <KeyPress-H> 表示用户单击H按键
            <Control-Shift-KeyPress-H> 表示用户同时单击ctrl+shift+H
 
        3.type部分常用关键字：
            
            Activate:当事件从"未激活"到"激活"时触发事件
            Button:当用户单击鼠标时触发事件
                <Button-1>: 鼠标左键
                <Button-2>:鼠标中键
                <Button-3>:鼠标右键
                <Button-4>:滚轮上滚
                <Button-5>:滚轮下滚
            Enter：当鼠标进入组件时
            FocusIn: 当组件获得焦点时,
            FocusOut:当组件失去焦点时
            KeyPress: 当用户按下键盘时触发事件
            KeyRelease: 当用户释放键盘时
            Leave:当鼠标指针离开组件时
            Motion:鼠标在组件中移动的整个过程均为触发事件
            MouseWhell:当滚轮滚动时触发事件
        4.modifier部分常用关键字:
            Alt: 按下Alt键
            Any:表示任何类型的按键
            Control：按下ctrl键
            Double: 将后续俩个事件连续触发时触发事件
            Lock:当打开大写字母键时
            Shift：当按下shift键时
            Triple:当后续三个事件被连续触发时触发事件
'''


'''
    三.Event对象
        1.将Event对象作为某个事件触发时所调用函数的参数
        2.Enent对象的属性:
            widget: 产生改事件的组件
            x, y: 当前鼠标位置坐标(相当于窗口左上角，以像素为单位)
            x_root, y_root: 当前鼠标位置的坐标(相当于屏幕左上角，以像素为单位)
            char: 按键对应的字符(键盘事件专属)
            keysym: 按键名(键盘事件专属)
            keycode: 按键码(鼠标事件专属)
            num: 按钮数字(鼠标事件专属)
            width,height: 组件的新尺寸
            type: 改事件类型
'''