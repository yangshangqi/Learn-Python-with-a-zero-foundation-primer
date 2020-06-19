# autor: zhumenger

'''
    碰撞检测：
        原理就是检查俩个精灵之间是否存在重叠的部分
        
        这里我们使用pygame自带的碰撞精灵模块 Sprite模块的碰撞检测方法：
        pygame.sprite.spritecollide(sprite, group, dokill, collided = None):
        第一个参数为单个被检测精灵
        第二个参数为一组精灵，有sprite.Group()生成
        第三个参数如何为True表示发生一次碰撞之后就会失去精灵的身份，不再发生碰撞效果
        第四个参数用于自定义碰撞的检测方法，如果为None, 则默认是检测精灵之间的rect是否产生重叠
        
'''

# 18-6-1.py
import pygame
import sys
from random import *
from random import *


# Sprite模块提供了一个动画精灵的基类，可以实现碰撞效果
# 球类继承Sprite类
class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        # 将小球放到指定位置
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2

    # 实现左进右出，上进下出的效果
    def move(self):
        self.rect = self.rect.move(self.speed)
        
        if self.rect.right < 0:
            self.rect.left = self.width
        if self.rect.left > self.width:
            self.rect.right = 0
        if self.rect.top > self.height:
            self.rect.bottom = 0
        if self.rect.bottom < 0:
            self.rect.top = self.height


def main():
    pygame.init()
    
    ball_image = "image/gray_ball.png"
    bg_image = "image/background.png"
    
    running = True

    # 根据背景图片指定游戏界面尺寸
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("实现球的运动")
    
    background = pygame.image.load(bg_image).convert_alpha()

    # 用来存放小球对象
    balls = []
    group = pygame.sprite.Group()
    
    # 创建五个小球
    for i in range(5):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, width - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
        
        # 检查新创建的这个球是否与其他创建的球发生碰撞，如果发生碰撞，重新设置球的位置,否则会出现卡死的现象
        # 这里使用精灵模块 sprite 中的碰撞检查方法 spritecollide() 检查单个精灵与组中精灵之间是否发生碰撞关系
        # 我们知道图形是方形的，当四个角发生碰撞时，由于spritecollide()默认根据rect是否覆盖进行检测，所以显得并不合理
        # 通过设置第四个参数，以半径来检测碰撞范围，需要在精灵对象中设置一个radius(半径)属性才行
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        group.add(ball)
        balls.append(ball)
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        screen.blit(background, (0, 0))
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
        
        for each in group:
            # 先从组移出当前球，
            group.remove(each)
            #判断当前球是否与其他球发生了碰撞
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            # 再将当前球添加回组中
            group.add(each)
        
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()






