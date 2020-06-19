# autor: zhumenger

'''
    所谓游戏，事实上就是一个死循环，而事件正是pygame干预游戏的机制
    事件随时发生，pygame的做法就是把所有的事件都放入到事件队列里，通过for循环语句迭代出每一个事件
'''

# 18_2_1.py 将程序运行期间产生的所有事件记录并存放到一个文件中
#
# import pygame
# import sys
#
# pygame.init()
#
# size = width, height = 600, 400
#
# screen = pygame.display.set_mode(size)
#
# pygame.display.set_caption("你好啊！")
#
# f = open("recode.txt", 'w')
#
# while True:
#     for event in pygame.event.get():
#         f.write(str(event) + '\n')
#         if event.type == pygame.QUIT:
#             f.close()
#             sys.exit()



'''
    将这些事件显示在画面上：
        这就要涉及在屏幕上显示文字的功能，但pygame没有办法直接在一个surface对象上显示文字，
        因此需要调用font模块的render()方法将文字活生生渲染成一个Surface对象
        这样就可以调用blit()方法将一个Suiface对象放到上面
'''

# 18_2_2.py 将这些事件显示在画面上
#
# import pygame
# import sys
#
# pygame.init()
#
# size = width, height = 600, 400
# bg = (0, 0, 0)
#
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("你好啊！")
#
# #要在pygame上使用文本，必须创建font对象
# #第一个参数指定文体，第二个参数指定字体的尺寸
#
# font = pygame.font.Font(None, 20)
#
# #调用get_linesize()方法获得每行文本的高度
# line_height = font.get_linesize()
#
# position = 0
# screen.fill(bg)
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#
#         #render()方法将文本渲染成Surface对象
#         #第一个参数是待渲染的文本
#         #第二个参数指定是否消除锯齿
#         #第三个参数指定文本的颜色
#         screen.blit(font.render(str(event), True, (0, 255, 0)), (0, position))
#         position += line_height
#
#         #满屏时清屏
#         if position > height:
#             position = 0
#             screen.fill(bg)
#     pygame.display.flip()


# 18_2_3.py 手动控制小甲鱼的移动方向

import pygame
import sys
#将pygame的所有常量名导入
from pygame.locals import *

pygame.init()

size = width, height = 600, 400
bg = (255, 255, 255)
speed = [0, 0]

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("初次见面，请大家多多关照！")

turtle = pygame.image.load("image/turtle.png")
position = turtle.get_rect()

#指定龟头的左右朝向
l_head = turtle
r_head = pygame.transform.flip(turtle, True, False)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                speed = [-2, 0]
                turtle = l_head
            if event.key == K_RIGHT:
                speed = [2, 0]
                turtle = r_head
            if event.key == K_UP:
                speed = [0, -2]
            if event.key == K_DOWN:
                speed = [0, 2]
    position = position.move(speed)
    
    if position.left < 0 or position.right > width:
        #翻转图像
        turtle = pygame.transform.flip(turtle, True, False)
        speed[0] = -speed[0]
    if position.left < 0 or position.right > width:
        speed[1] = -speed[1]
    
    screen.fill(bg)
    screen.blit(turtle, position)
    pygame.display.flip()
    
    clock.tick(30)