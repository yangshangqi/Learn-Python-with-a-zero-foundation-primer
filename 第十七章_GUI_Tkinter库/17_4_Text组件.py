# autor: zhumenger
'''
    Text组件：
        1.文本组件，可以显示多行文本
        2.可用insert()方法给其插入内容:
            INSERT表示光标当前位置, END表示结尾位置
            
        3.支持image对象和window组件
'''

#17_4_1.py
#
# from tkinter import *
# root = Tk()
#
# text = Text(root, width = 30, height = 5)
# text.pack()
#
# text.insert(INSERT, "风浪没平息\n")
# text.insert(END, "我宣告奔跑的意义.")
#
# mainloop()


# 17_4_2.py 在文本框内添加按钮和背景图片
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 15)
# text.pack()
#
# text.insert(INSERT, "风浪没平息\n我宣告奔跑的意义.")
#
# photo = PhotoImage(file = "dongman.gif")
# text.image_create(END, image = photo)
#
# def show():
#     print("这不是叛逆\n我只是淋了一场雨.")
# b1 = Button(root, text = "下一句歌词", command = show)
# text.window_create(INSERT, window = b1)
#
# mainloop()


'''
    Indexes用法
        Indexes(索引)是用来指向Text组件中文本的位置, 与python的序列索引一样
        索引类型：
            line.column(行\列)：
                行号从1开始，列号从0开始
            line.end(某一行的末尾):
            
            INSERT: 对应插入光标的位置
            END: 文本缓冲区最后一个字符的下一个位置
            CURRENT：与鼠标最接近的位置
            
            user-defined marks：
                是对Text组件位置的命名,除了INSERT和END俩个事先命名好的Marks外，我们还可以自定义Marks
            user-defined tags:
                代表可以分配给Text组件的特殊事件绑定和风格
                tag.first tag.end 可以用来表示文本的范围
        
'''

# 17_4_3.py
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 3)
# text.insert(INSERT, "I LOVE YOU!")
#
# print(text.get(1.2, 1.6)) #LOVE 行.列
# print(text.get(1.2, "1.end")) #line.end


'''
    Mark用法：
        1.是嵌入到Text文本中的不可见对象, 停在字符间的光标
        2.可使用mark_set()方法创建和移动Mark
        3.如果Mark前面的内容发生改变，Mark的位置也会跟着移动
          实际上，Mark会紧跟着后面的"那家伙"
        4.如果Mark周围的文本被删除，Mark还会存在
        5.使用mark_unset()方法可以解除Mark
        6.在光标处插入文本，是插入到它的左侧，
          通过mark_gravity()方法可以将文本插入到光标的右侧
'''


# 17_4_4.py
#
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 3)
# text.pack()
# text.insert(INSERT, "I LOVE YOU!")
#
# text.mark_set("here", 1.2) #将光标移到第一行，第三列
# text.insert("here", "插") #在该光标处插入文本
#
# text.insert("here", "入")
#
# text.delete('1.0', END)
# # text.mark_unset("here")
# text.insert("here", "入")
# text.mark_gravity("here", LEFT)
# text.insert("here", "哈哈哈")
# text.insert("here", "你咋不笑啊")
# mainloop()


'''
    Tag用法:
        1.通常用于改变组件中内容的样式和功能，可以用来修改文本的字体，尺寸和颜色
          tag还允许将文本、嵌入的组件和图片与键盘和鼠标等事件相关联
        2.SEL：预定义的tag，表示对应的选中的内容
        3.可以自定义任意数量的Tag，Tag的名字由普通字符串组成，可以是除了空白以外的任何字符
        4.为指定文本添加tag，可以使用tag_add()方法, tag可以用来描述多个不同的文本内容
          tag_add("name", start, end) 分别表示Tag的名字，文本开始位置和结束位置
          如果只有start, 那么只会选中一个字符，支持多个start和end
        5.tag_config()可以设置Tag的样式:
            background()用来设置字体的背景颜色
            font:用来设置字体的大小
            foreground: 设置字体的颜色
            justify: 控制文本的对其方式 LEFT RIGHT CENTER
            underline:为选中的文本画上下划线
            overstrike；为选中的文本画一条删除线
            spacing1: 文本块中每一行与上一行的空白间隔
            spacing2: 文本块中自动换行的各行间的空白间隔
            spacing3: 文本块中每一行与下一行的空白间隔
        6.如果对同一范围内的文本设置多个Tag，那么新的Tag将会覆盖旧的Tag
        7.可以使用tag_raise()和tag_lower()方法来提高或降低某个Tag的优先级
        
        8.tag还支持事件绑定,绑定事件使用的是tag_bind()方法
'''

# 17_4_5.py 为指定文本添加tag
#
# from tkinter import *
#
# root = Tk()
# text = Text(root, width = 30, height = 8)
# text.pack()
#
# text.insert(INSERT, "风浪没平息,我宣告奔跑的意义,这不是叛逆,我只是淋了一场雨\n")
# text.tag_add("tag1", "1.7", "1.12")
# text.tag_config("tag1", background = "yellow", foreground = "red")
#
# text.tag_config("tag2", background = "yellow", foreground = "red")#旧的tag
# text.tag_config("tag3", background = "orange") #新的tag
# text.insert(INSERT, "风浪没平息,我宣告奔跑的意义,这不是叛逆,我只是淋了一场雨\n", ('tag2', "tag3")) #与调用顺序无关
#
# text.tag_config("tag4", background = "yellow", foreground = "red")
# text.tag_config("tag5", background = "orange")
# text.tag_lower("tag5")   #降低tag5的优先级
#
# text.insert(INSERT, "风浪没平息,我宣告奔跑的意义,这不是叛逆,我只是淋了一场雨\n", ("tag4", "tag5"))
# mainloop()


# 17_4_6.py 为鼠标设置点击事件以及改变鼠标的形态
#
# from tkinter import *
# import webbrowser
#
# root = Tk()
#
# text = Text(root, width = 30, height = 5)
# text.pack()
#
# text.insert(INSERT, "I LOVE FishC.com!")
#
# text.tag_add("tag1", "1.7", "1.16")
# text.tag_config("tag1", foreground = "blue", underline = True)
#
# def show_arrow_cursor(event):
#     text.config(cursor = "arrow") # 将鼠标改为箭头形态
# def show_xterm_cursor(event):
#     text.config(cursor = "xterm") # 将鼠标改为终端形态
# def click(event):
#     webbrowser.open("https://www.baidu.com")
#
# text.tag_bind("tag1", "<Enter>", show_arrow_cursor) #设置进入事件
# text.tag_bind("tag1", "<Leave>", show_xterm_cursor) #设置离开事件
# text.tag_bind("tag1", "<Button-1>", click)
#
# mainloop()


'''
    Text组件使用时的技巧：
    (1).判断内容是否发生变化：
        当关闭程序时，如果文本内容发生变化, 需要提醒用户保存
        可以使用Text组件中文本的MD5摘要来判断内容是否发生变化
'''


# 17_4_7.py
#
# from tkinter import *
# import hashlib #导入哈希库
#
# root = Tk()
#
# text = Text(root, width = 30, height = 5)
# text.pack()
#
# text.insert(INSERT,"风浪没平息\n我宣告奔跑的意义.\n")
# contents = text.get(1.0, END)
#
# def getSig(contents): #得到该字符串的哈希值
#     m = hashlib.md5(contents.encode())
#     return m.digest()
#
# sig = getSig(contents)
#
# def check():
#     contents = text.get(1.0, END)
#     if sig != getSig(contents):
#         print("内容发生改变")
#     else:
#         print("风平浪静")
# Button(root, text = "检查", command = check).pack()
#
# mainloop()


'''
    (2).查找操作:
        使用search()方法可以搜索Text组件中的内容, 也可以用Tcl格式的正则表达式进行搜索(需设置 regexp为 True)
        第一个参数表示要查找的目标，第二个参数表示搜索的起始位置，第三个参数stopindex表示搜索的结束位置
        如果没有写stopindex,则默认的文本的末尾结束
        
        设置backwards选项为True, 修改搜索的方向（变为向前搜索，此时start应该为END, stopindex应该为1.0）
'''

# 17_4_8.py
#
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 5)
# text.pack()
#
# text.insert(INSERT, "I love FishC.com!")
#
# #将任何格式的索引号统一为元组(行,列)的格式输出
# def getIndex(text, index):
#     return tuple(map(int, str.split(text.index(index), '.'))) #将行和列分开输出
# start = 1.0
#
# while True:
#     pos = text.search('o', start, stopindex =  END) #查询字母'o' 开始位置是start, 结束位置是stopindex
#     if not pos:
#         break
#     print("找到了,位置是:", getIndex(text, pos))
#     start = pos + "+1c" #将start指向下一个字符
# mainloop()


'''
    (3).Text组件还支持"恢复"和"撤销功能"
        通过设置undo选项为True，可以开启Text组件的撤销功能, 然后使用edit_undo()方法
        实现"撤销操作"，用edit_redo()方法实现"恢复"操作
        
        Text组件内部有一个栈专门记录内容的每次变动,
        所以每一次撤销操作就是一次弹栈操作，恢复就是入栈操作
        
        默认情况下，一次完整的操作都会放入栈中，一次撤销操作就是将一次完整的操作内容删除
        我们也可以自定义分隔符，如希望插入一个字符就算一次完整的操作,每次点击删除只去掉一个字符
        
        用过设置autoseparators选项设置为False(该选项默认为True，即一次完整的操作便会放入栈中)
        然后绑定键盘事件, 每次有输入就用edit_separator()方法人为地插入一个分隔符
'''


# 17_4_9.py 实现撤销操作
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 5, undo = True)
# text.pack()
#
# text.insert(INSERT, "I LOVE YOU!")
#
# def show():
#     text.edit_undo()
# def huifu():
#     text.edit_redo()
# Button(root, text = "撤销", command = show).pack(side =LEFT, padx = 30)
# Button(root, text = "恢复", command = huifu).pack(side = RIGHT, padx = 30)
#
# mainloop()


# 17_4_10.py
#
# from tkinter import *
#
# root = Tk()
#
# text = Text(root, width = 30, height = 5, undo = True, autoseparator = False, maxundo = 10)
# text.pack()
#
# text.insert(INSERT, "I LOVE YOU!")
#
# def callback(event):
#     text.edit_separator()
# text.bind('<Key>', callback)
#
# def show():
#     text.edit_undo()
# def huifu():
#     text.edit_redo()
# Button(root, text = "撤销", command = show).pack(side = LEFT, padx = 30)
# Button(root, text = "恢复", command = huifu).pack(side = RIGHT, padx = 30)
#
# mainloop()