# autor: zhumenger

'''
    pygame:
        用于游戏开发的库
'''

# import pygame as p
# print(p.ver) #打印版本

# p18_1.py
import pygame
import sys

# 初始化Pygame
pygame.init()

size = width, height = 600, 400 # size是一个元组
speed = [-2, 1]
bg = (255, 255, 255)

# 创建指定大小的窗口
screen = pygame.display.set_mode(size) #创建一个Surface对象，在这里最为画布
# 设置窗口标题
pygame.display.set_caption("初次见面，请大家多多关照！")

turtle = pygame.image.load(r"image/turtle.png")

# 获得图像的位置矩形
position = turtle.get_rect()

print(position)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # 移动图像
    position = position.move(speed)
    
    if position.left < 0 or position.right > width:
        # 翻转图像
        turtle = pygame.transform.flip(turtle, True, False) #第二个参数表示水平翻转,第三个表示垂直翻转
        # 反方向移动
        speed[0] = -speed[0]
    
    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]
    
    # 填充背景
    screen.fill(bg)
    # 更新图像
    screen.blit(turtle, position) #重新将移动后的图片放上去
    # 更新界面
    pygame.display.flip()
    # 延迟10毫秒
    pygame.time.delay(10) #10毫秒刷新一次界面
''''''

'''
  代码解读
    pygame：
        就是一个包, 里面包含很多不同功能的模块, pygame.init()用于初始化这些模块
    display,set_mode()方法创建一个surface对象，
    
    如何退出游戏：
        用户的一切行为都会变成一个个的时间，我们只需要迭代查找所有的事件，如果有退出事件发生，就退出程序
    如何修改方向：
        判断移动后的矩形区域是否到达边界，如果达到边界，就将移动的方向改变一下即可
    pygame.display.filp()：
        该方法用于实现图像的翻转,第一个参数表述图像，第二个参数表示水平翻转，第三个参数表示垂直翻转
    screen.fill(): 用于填充画布颜色，每移动一次都需要填充一次，用于刷去上一次的图像，
    screen.bile()：用于在画布上添加图像，
    screen.display.flip():该方法用于刷新界面，python采用的是双缓冲模式，需要将缓冲好的画面一次性的刷新到显示器上
    
    双缓冲：即在内存中创建一个与屏幕绘图区域一致的对象，我们进行的操作，都是讲图形先绘制到内存中的这个对象上
            在一次性的刷新到屏幕上，大大加快了绘图的速度
    pygame.time.delay():该方法决定了程序多长时间刷新一次，
    Surface对象：
        1.surface对象就是pygame用来表示图像的对象，surface对象即图像
        2.Surface对象的blit()方法是将一个图像绘制到另一个图像上面，实际上是修改了像素
    图像移动：
        帧频：即1s可以移动多少次图像，python支持40-200帧，也就是一秒能切换40-200次图像
        通过调用rect对象的move方法，可以实现修改矩形的位置，
'''