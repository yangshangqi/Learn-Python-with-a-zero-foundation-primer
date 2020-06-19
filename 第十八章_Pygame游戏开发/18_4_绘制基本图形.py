# autor: zhumenger

'''
    1.绘制矩形
        语句格式如下：
            rect(Surface, color, Rect, width = 0)
            该该方法用于在Sruface对象上面绘制一个矩形
            第一个参数指定矩形将绘制到哪个Surface对象上
            第二个参数指定颜色
            第三个参数指定矩形的范围(left, top, width, height)
            第四个参数指定矩形边框的大小(0表示填充矩形)
    2.绘制多边形：
        polygon(Surface, color, pointlist, width = 0)
            pointlist: 各个顶点坐标组成的列表, 必须按照顺序来写点的坐标
'''

# 18_4_1.py
#
# import pygame
# import sys
#
# from pygame.locals import *
#
# pygame.init()
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (0, 255, 0)
#
# size = width, height = 640, 480
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("绘制矩形")
#
# clock = pygame.time.Clock()
#
# points = [(200, 175), (300, 125), (400, 175), (450, 125), (450, 225), (400, 175), (300, 225)]
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     screen.fill(WHITE)
#
#     #绘制矩形
#     pygame.draw.rect(screen, BLACK, (50, 50, 150, 50), 0)
#     pygame.draw.rect(screen, BLACK, (250, 50, 150, 50), 1)
#     pygame.draw.rect(screen, BLACK, (450, 50, 150, 50), 10)
#
#     #绘制多边形
#     pygame.draw.polygon(screen, GREEN, points, 0)
#     pygame.display.flip()
#
#     clock.tick(10)

# ======================================================================================================================
''''''

'''
    3.绘制圆形
        circle(Surface, color, pos, radius, width = 0)
        pos: 指定圆心的位置
        radius: 指定半径的大小
    4.绘制椭圆
        ellipse(Surface, color, Rect, width = 0)
        利用第三个参数，根据指定的矩形来绘制, 如果矩形是正方形，那么画出来的就是圆
    5.绘制弧线
        arc(Surface, color, Rect, start_angle, stop_angle, width = 1)
        因为弧线不是全包围图形，因此width不能设为0
        rect参数表示一个矩形，
        start_angle，stop_angle用来设置弧形在矩形区域内的起始角度和结束角度
    6.绘制线段
        line(Surface, color, start_pos, end_pos, width = 1)
            用于绘制一条线段
        lines(Surface, color, closed, pointlist, width = 1)
            用于绘制多条线段, closed()方法表示收尾是否相连, 不能通过设置width = 0对图像进行填充
        aaline(Surface, color, startpos, endpos, blend = 1)
            用来实现锯齿状的功能 blend参数指定是否通过绘制混合背景的阴影来实现抗锯齿功能
        aaline(Surface, clolr, closed, pointlist, blend = 1)
'''

# 18-4-2.py
import pygame
import math
import sys
from pygame.locals import *


pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = width, height = 640, 480
screen = pygame.display.set_mode(size)
pygame.display.set_caption("绘制圆形")
clock = pygame.time.Clock()

position = width // 2, height // 2
moving = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #鼠标点击选中圆心
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                moving = True
        #鼠标松开
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                moving = False
    if moving:
        position = pygame.mouse.get_pos()

    screen.fill(WHITE)
    
    #绘制圆形
    pygame.draw.circle(screen, RED, position, 25, 1)
    pygame.draw.circle(screen, GREEN, position, 75, 1)
    pygame.draw.circle(screen, BLUE, position, 125, 1)
    #绘制椭圆
    pygame.draw.ellipse(screen, RED, (245, 215, 150, 50), 1)
    #绘制弧线
    pygame.draw.arc(screen, BLACK, (185, 100, 270, 50), 0, math.pi, 10)
    # 绘制线段
    pygame.draw.line(screen, BLACK, (50, 50), (50, 250), 5)
    pygame.draw.aaline(screen, BLACK, (100, 50), (100, 250), 1)
    pygame.draw.aaline(screen, BLACK, (150, 50), (150, 250), 0)
    pygame.display.flip()
    clock.tick(10)