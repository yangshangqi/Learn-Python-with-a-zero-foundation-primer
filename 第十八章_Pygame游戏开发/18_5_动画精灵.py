# autor: zhumenger

# 18-5-1.py

import pygame
import sys
from random import *
from random import *

#Sprite模块提供了一个动画精灵的基类，可以实现碰撞效果
#球类继承Sprite类
class Ball(pygame.sprite.Sprite):
    def __init__(self, image, position, speed, bg_size):
        #初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        # 将小球放到指定位置
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
    
    #实现左进右出，上进下出的效果
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
    
    #根据背景图片指定游戏界面尺寸
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("实现球的运动")
    
    background = pygame.image.load(bg_image).convert_alpha()
    
    #用来存放小球对象
    balls = []
    
    
    #创建五个小球
    for i in range(5):
        #位置随机，速度随机
        position = randint(0, width - 100), randint(0, width - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(ball_image, position, speed, bg_size)
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
        
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    