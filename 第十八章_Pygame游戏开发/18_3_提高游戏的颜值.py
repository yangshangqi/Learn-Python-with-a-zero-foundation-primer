# autor: zhumenger

'''
    一.显示模式
        pygame通过display模块的set_mode()方法来指定界面的大小，并返回一个Surface对象,
        
        set_mode()方法原型如下：
            set_mode(resolution = (0, 0), flags = 0, depth = 0) -> Surface
            第一个参数用于指定界面的大小，
            第二个参数flags用于指定扩展选项，可以用|分隔符选择多个选项
                FULLSCREEN: 全屏模式
                DOUBLEBUF: 双缓冲模式
                HWSURFACE: 硬件加速模式(只有在全屏模式下才能使用)
                RESIZEBLE: 使得窗口可以调整大小
                NOFRAME: 使得窗口没有边框和控制按钮
            第三个参数depth 用于指定颜色位数，pygame会自动根据当前操作系统设置最合适的颜色位数
        
        开始全屏并加上硬件加速器：
            screen = pygame.display.set_mode(640, 480), FULLSCREEN | HWSURFACE)
        由于全屏模式并不会自带退出键，所以我们需要自己设置
        
        调整窗口尺寸大小：
            set_mode()第二个参数，选择RESIZEBLE选项，开启窗口尺寸可修改模式，一旦用户调整窗口的尺寸，
            pygame就会发送一条带有最新尺寸的VIDEORESIZE事件到事件序列中去，此时，我们获取并重新设置width和height
'''


# p18_3_1.py 设置全屏模式，将F11键作为全屏快捷键,并使使窗口尺寸可变
#
# import pygame
# import sys
# # 将 pygame 的所有常量名导入
# from pygame.locals import *
#
# # 初始化Pygame
# pygame.init()
#
# fullscreen = False
#
# size = width, height = 600, 400
# bg = (255, 255, 255)
# speed = [0, 0]
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode(size, RESIZABLE)
# pygame.display.set_caption("初次见面，请大家多多关照！")
#
# turtle = pygame.image.load(r"image/turtle.png")
# position = turtle.get_rect()
#
# # 指定龟头的左右朝向
# l_head = turtle
# r_head = pygame.transform.flip(turtle, True, False)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()
#
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT:
#                 speed = [-1, 0]
#                 turtle = l_head
#             if event.key == K_RIGHT:
#                 speed = [1, 0]
#                 turtle = r_head
#             if event.key == K_UP:
#                 speed = [0, -1]
#             if event.key == K_DOWN:
#                 speed = [0, 1]
#             # 全屏（F11）
#             if event.key == K_F11:
#                 fullscreen = not fullscreen
#                 if fullscreen:
#                     screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
#                 else:
#                     screen = pygame.display.set_mode(size)
#         # 用户调整窗口尺寸
#         if event.type == VIDEORESIZE:
#             size = event.size
#             width, height = size
#             print(size)
#             screen = pygame.display.set_mode(size, RESIZABLE)
#
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         # 翻转图像
#         turtle = pygame.transform.flip(turtle, True, False)
#         # 反方向移动
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(bg)
#     screen.blit(turtle, position)
#     pygame.display.flip()
#
#     clock.tick(30)

''''''

#  =====================================================================================================================

'''
    二.图像的变换
        transform模块提供了一些只可以对图像做各种变幻动作的功能，并返回Surface对象:
            filp(): 上下左右翻转图像
            scale(): 缩放图像
            rotate(): 旋转图像
            rotozoom: 缩放并旋转图像
            scale2x: 快速放大一倍图像
            smoothscale: 平滑缩放图像
            chop：裁剪图像
'''

#2.1.利用smoothscale()方法实现图像的缩放， 第一个参数为图像，第二个参数为缩放后图像的长和宽
# 18_3_2.py


# import pygame
# import sys
# from pygame.locals import *
# pygame.init()
#
# fullscreen = False
#
# size = width, height = 600, 400
# bg = (255, 255, 255)
# speed = [0, 0]
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode(size, RESIZABLE)
# pygame.display.set_caption("初次见面，请大家多多关照！")
#
# # 设置大小、缩放比率
# ratio = 1.0
#
# oturtle = pygame.image.load("image/turtle.png")
# turtle = oturtle
# oturtle_rect = oturtle.get_rect()
# position = turtle_rect = oturtle_rect
#
# # 指定龟头的左右朝向
# l_head = turtle
# r_head = pygame.transform.flip(turtle, True, False)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()
#
#         if event.type == KEYDOWN:
#             if event.key == K_LEFT:
#                 speed = [-1, 0]
#                 turtle = l_head
#             if event.key == K_RIGHT:
#                 speed = [1, 0]
#                 turtle = r_head
#             if event.key == K_UP:
#                 speed = [0, -1]
#             if event.key == K_DOWN:
#                 speed = [0, 1]
#             # 全屏（F11）
#             if event.key == K_F11:
#                 fullscreen = not fullscreen
#                 if fullscreen:
#                     screen = pygame.display.set_mode((1920, 1080), FULLSCREEN | HWSURFACE)
#                 else:
#                     screen = pygame.display.set_mode(size)
#             # 放大、缩小小乌龟(=, -), 空格恢复原始尺寸
#             if event.key == K_EQUALS or event.key == K_MINUS or event.key == K_SPACE:
#                 #最大只能放大一倍，缩小50%
#                 if event.key == K_EQUALS and ratio < 2:
#                     ratio += 0.1
#                 if event.key == K_MINUS and ratio > 0.5:
#                     ratio -= 0.1
#                 if event.key == K_SPACE:
#                     ratio = 1
#                 turtle = pygame.transform.smoothscale(oturtle, (int(oturtle_rect.width * ratio), int(oturtle_rect.height * ratio)))
#
#                 #相应的修改龟头俩个朝向的Surface对象, 否则一单击移动就会打回原形
#                 l_head = turtle
#                 r_head = pygame.transform.flip(turtle, True, False)
#
#                 #获得小乌龟缩放后的新尺寸
#                 turtle_rect = turtle.get_rect()
#                 position.width, position.height = turtle_rect.width, turtle_rect.height
#         # 用户调整窗口尺寸
#         if event.type == VIDEORESIZE:
#             size = event.size
#             width, height = size
#             print(size)
#             screen = pygame.display.set_mode(size, RESIZABLE)
#
#     position = position.move(speed)
#
#     if position.left < 0 or position.right > width:
#         # 翻转图像
#         turtle = pygame.transform.flip(turtle, True, False)
#         # 反方向移动
#         speed[0] = -speed[0]
#
#     if position.top < 0 or position.bottom > height:
#         speed[1] = -speed[1]
#
#     screen.fill(bg)
#     screen.blit(turtle, position)
#     pygame.display.flip()
#
#     clock.tick(30)


# ======================================================================================================================

#2.2.通过rotate()方法让小乌龟实现贴边行走，第一个参数为图像，第二个参数为逆时针旋转的角度
# p18_3_3.py


# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
#
# size = width, height = 640, 480
# bg = (255, 255, 255)
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("FishC Demo")
#
# turtle = pygame.image.load(r"image/turtle.png")
# position = turtle_rect = turtle.get_rect()
#
# # 小乌龟顺时针行走
# speed = [5, 0]
# turtle_right = pygame.transform.rotate(turtle, 90)
# turtle_top = pygame.transform.rotate(turtle, 180)
# turtle_left = pygame.transform.rotate(turtle, 270)
# turtle_bottom = turtle
#
# # 刚开始走顶部
# turtle = turtle_top
#
# while True:
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()
#
#     position = position.move(speed)
#
#     if position.right > width:
#         turtle = turtle_right
#         # 变换后矩形的尺寸发生改变
#         position = turtle_rect = turtle.get_rect()
#         # 矩形尺寸的改变导致位置也有变化
#         position.left = width - turtle_rect.width
#         speed = [0, 5]
#
#     if position.bottom > height:
#         turtle = turtle_bottom
#         position = turtle_rect = turtle.get_rect()
#         position.left = width - turtle_rect.width
#         position.top = height - turtle_rect.height
#         speed = [-5, 0]
#
#     if position.left < 0:
#         turtle = turtle_left
#         position = turtle_rect = turtle.get_rect()
#         position.top = height - turtle_rect.height
#         speed = [0, -5]
#
#     if position.top < 0:
#         turtle = turtle_top
#         position = turtle_rect = turtle.get_rect()
#         speed = [5, 0]
#
#     screen.fill(bg)
#     screen.blit(turtle, position)
#     pygame.display.flip()
#
#     clock.tick(30)


# ======================================================================================================================


'''
    2.3.裁剪图像:
        使用chop()方法裁剪图像，会将所选中的区域进行裁剪，被指定的区域直接去掉
        剩余的区域将会重新拼凑在一起，并返回一个Surface对象
        
        我们可以通过设置鼠标点击事件来实现真正的裁剪功能:
            1.第一次鼠标点击确定裁剪范围
            2.第二次拖动左键裁剪范围内的图像
            3.第三次点击表示重新开始
'''

# 18_3_4.py 实现裁剪功能
#
# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
#
# size = width, height = 800, 600
# bg = (255, 255, 255)
#
# clock = pygame.time.Clock()
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("实现图片的裁剪功能")
#
# turtle = pygame.image.load("image/turtle.png")
#
# # 0 -> 未选择，1 -> 选择中, 2 -> 完成选择
# select = 0
# select_rect = pygame.Rect(0, 0, 0, 0)
# # 0 -> 未拖动, 1 -> 拖动中, 2 -> 拖动完成
# drag = 0
#
# position = turtle.get_rect()
# position.center = width // 2, height // 2
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         elif event.type == MOUSEBUTTONDOWN:
#             #左键点击
#             if event.button == 1:
#                 # 第一次点击, 选择范围
#                 if select == 0 and drag == 0:
#                     pos_start = event.pos
#                     select = 1
#                 # 第二次单击，拖动图像
#                 elif select == 2 and drag == 0:
#                     capture = screen.subsurface(select_rect).copy()
#                     cap_rect = capture.get_rect()
#                     drag = 1
#                 elif select == 2 and drag == 2:
#                     select = 0
#                     drag = 0
#         elif event.type == MOUSEBUTTONUP:
#             if event.button == 1:
#                 # 第一次释放，结束选择
#                 if select == 1 and drag == 0:
#                     pos_stop = event.pos
#                     select = 2
#                 elif select == 2 and drag == 1:
#                     drag = 2
#     screen.fill(bg)
#     screen.blit(turtle, position)
#
#     #实时绘制选择框
#     if select:
#         mouse_pos = pygame.mouse.get_pos()
#         if select == 1:
#             pos_stop = mouse_pos
#
#         select_rect.left, select_rect.top = pos_start
#         select_rect.width, select_rect.height = pos_stop[0] - pos_start[0], pos_stop[1] - pos_start[1]
#         pygame.draw.rect(screen, (0, 0, 0), select_rect, 1)
#
#     #拖动裁剪的图像
#     if drag:
#         if drag == 1:
#             cap_rect.center = mouse_pos
#         screen.blit(capture, cap_rect)
#     pygame.display.flip()
# clock.tick(30)


# ======================================================================================================================

'''
    3.转换图片：
        图像是特定像素的组合，Surface对象是Pygame对对象的描述，在Pygame中到处都是Surface
        image.load()载入图片后将返回一个Surface对象, 这种效率较低，
        可以使用convert()方法对图片的像素格式进行转换，使Pygame尽可能高效的处理图片:
            background = pygame.image.load("image.jpg").convert()
        还有一个是convert_alpha(),一般情况下用RGB来描述一个颜色，在游戏开发中用到的是RGBA
        多出来的A指的是alpha通道，用于表示透明度, 他的值为0~255, 0表示完全透明，255表示完全不透明
        对于包含alpha通道的图片，使用convert_alpha()转换格式,否则使用convert()
'''


'''
    4.透明度分析
        Pygame支持三种类型的透明度设置：colorkeys、surface alphas 和 pixel alphas
        colorkeys: 指定一种颜色，使其变为透明
        surface alphas: 是整体设置一个图片的透明度
        pixel alphas: 为每一个像素增加一个alpha通道
        
        convert()方法转换的Surface对象支持colorkeys 和surface alphas设置透明度，并且可以混合使用
        convert_alpha()方法转换后支持pixel alphas， 这个图片每个像素都自带alpha通道
        当载入一个带alpha通道的图片时，可以看到该图片部分部位是透明的
        
        还可以通过使用get_at()方法获取单个像素的颜色，并用set_at()方法来修改透明度
        get_at()方法会返回一个RGBA列表，[a, b, c, d] a, b, c表示颜色， d表示透明度
'''


# 18_3_5.py

import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
bg = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("实现图片透明化")

turtle = pygame.image.load("image/turtle.png") # turtle.png这个图片自带alpha通道，并且背景被设置为透明
#turtle = pygame.image.load("image/turtle.jpg").convert()
background = pygame.image.load("image/background.jpg").convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

#turtle.set_colorkey((255, 255, 255)) # 将选定的颜色变为透明
#turtle.set_alpha(200) # 用来设置整个图片的透明度

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(background, (0, 0))
    screen.blit(turtle, position)
    
    pygame.display.flip()
    clock.tick(30)
    
    
''''''

# p18_12.py 将整个小乌龟的透明度调整为2000
import pygame
import sys
from pygame.locals import *

pygame.init()

size = width, height = 640, 480
bg = (0, 0, 0)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("FishC Demo")

turtle = pygame.image.load("image/turtle.png").convert_alpha()
background  = pygame.image.load("image/background.jpg").convert()
position = turtle.get_rect()
position.center = width // 2, height // 2

def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert() # 创建一个与小乌龟尺寸和位置相同且不带alpha通道的图像
    temp.blit(target, (-x, -y )) # 将背景图覆盖上去
    temp.blit(source, (0, 0))    # 将小乌龟覆盖上去
    temp.set_alpha(opacity)      # 通过设置这个图像的整体透明度从而实现将小乌龟整体透明度设置为200
    target.blit(temp, location)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    screen.blit(background, (0, 0))
    blit_alpha(screen, turtle, position, 200)

    pygame.display.flip()
    clock.tick(30)