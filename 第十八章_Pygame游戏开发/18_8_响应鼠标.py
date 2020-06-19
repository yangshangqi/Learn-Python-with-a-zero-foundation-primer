# autor: zhumenger

'''
    现在我们还需要设置玻璃的图片，并限制鼠标只能在此区域内移动
    如何限制鼠标的移动范围：
        用mouse模块的get_pos()方法获取鼠标的当前位置，检测如果超过了玻璃面板的范围，则使用set_pos()修改它
    如何修改鼠标样式：
        先通过设置mouse模块中的set_visible()方法将原来的光标设置为“不可见”，然后在鼠标的当前位置上绘制小手的图片
'''
#
#
# # 18_8_1.py 创建玻璃类，
# import pygame
# import sys
# from pygame.locals import *
# from random import *
#
# # 创建玻璃类
# class Glass(pygame.sprite.Sprite):
#     def __init__(self, glass_image, mouse_image, bg_size):
#         pygame.sprite.Sprite.__init__(self)
#
#         self.glass_image = pygame.image.load(glass_image).convert_alpha()
#         self.glass_rect = self.glass_image.get_rect()
#         self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) // 2, (bg_size[1] - self.glass_rect.height)
#
#         self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
#         self.mouse_rect = self.mouse_image.get_rect()
#         self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top
#
#         #设置鼠标为不可见
#         pygame.mouse.set_visible(False)
# # Sprite模块提供了一个动画精灵的基类，可以实现碰撞效果
# # 球类继承Sprite类
# class Ball(pygame.sprite.Sprite):
#     def __init__(self, image, position, speed, bg_size):
#         # 初始化动画精灵
#         pygame.sprite.Sprite.__init__(self)
#
#         self.image = pygame.image.load(image).convert_alpha()
#         self.rect = self.image.get_rect()
#         # 将小球放到指定位置
#         self.rect.left, self.rect.top = position
#         self.speed = speed
#         self.width, self.height = bg_size[0], bg_size[1]
#         self.radius = self.rect.width / 2
#
#     # 实现左进右出，上进下出的效果
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#
#         if self.rect.right < 0:
#             self.rect.left = self.width
#         if self.rect.left > self.width:
#             self.rect.right = 0
#         if self.rect.top > self.height:
#             self.rect.bottom = 0
#         if self.rect.bottom < 0:
#             self.rect.top = self.height
#
#
# def main():
#     pygame.init()
#
#     ball_image = "image/gray_ball.png"
#     bg_image = "image/background.png"
#     glass_image = "image/glass.png"
#     mouse_image = "image/hand.png"
#     running = True
#
#     # 添加魔性的背景音乐
#     pygame.mixer.music.load("image/bg_music.ogg")
#     pygame.mixer.music.play()
#
#     # 添加音效
#     loser_sound = pygame.mixer.Sound("image/loser.wav")
#     laugh_sound = pygame.mixer.Sound("image/laugh.wav")
#     winner_sound = pygame.mixer.Sound("image/winner.wav")
#     hole_sound = pygame.mixer.Sound("image/hole.wav")
#
#     # 音乐播放完游戏结束
#     # 这里我们创建一个自定义事件GAMEOVER，语法如下：
#     GAMEOVER = USEREVENT
#     pygame.mixer.music.set_endevent(GAMEOVER)  # 当音乐播放完时，发送这个事件
#
#     # 根据背景图片指定游戏界面尺寸
#     bg_size = width, height = 1024, 681
#     screen = pygame.display.set_mode(bg_size)
#     pygame.display.set_caption("实现球的运动")
#
#     background = pygame.image.load(bg_image).convert_alpha()
#     # 生成用于“摩擦摩擦”的玻璃面板
#     area = Glass(glass_image, mouse_image, bg_size)
#
#     # 用来存放小球对象
#     balls = []
#     group = pygame.sprite.Group()
#
#     # 创建五个小球
#     for i in range(5):
#         # 位置随机，速度随机
#         position = randint(0, width - 100), randint(0, width - 100)
#         speed = [randint(-10, 10), randint(-10, 10)]
#         ball = Ball(ball_image, position, speed, bg_size)
#         # 检查是否发生碰撞
#         while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
#             ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
#         group.add(ball)
#         balls.append(ball)
#
#     clock = pygame.time.Clock()
#
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
#             # 当音乐播放完时，便会发送一个GAMEOVER事件
#             # 捕捉这个事件并退出游戏
#             elif event.type == GAMEOVER:
#                 loser_sound.play()
#                 pygame.time.delay(3000)
#                 laugh_sound.play()
#                 running = False
#
#         screen.blit(background, (0, 0))
#         screen.blit(area.glass_image, area.glass_rect)
#
#         #获取鼠标当前位置, 并设置代替光标的图片
#         area.mouse_rect.left, area.mouse_rect.top = pygame.mouse.get_pos()
#         # 限制鼠标只能在玻璃内移动
#         if area.mouse_rect.left < area.glass_rect.left:
#             area.mouse_rect.left = area.glass_rect.left
#         if area.mouse_rect.left > area.glass_rect.right - area.mouse_rect.width:
#             area.mouse_rect.left = area.glass_rect.right - area.mouse_rect.width
#         if area.mouse_rect.top < area.glass_rect.top:
#             area.mouse_rect.top = area.glass_rect.top
#         if area.mouse_rect.top > area.glass_rect.bottom - area.mouse_rect.height:
#             area.mouse_rect.top = area.glass_rect.bottom - area.mouse_rect.height
#         # 绘制玻璃面板
#         screen.blit(area.mouse_image, area.mouse_rect)
#
#         for each in balls:
#             each.move()
#             screen.blit(each.image, each.rect)
#
#         for each in group:
#             # 先从组移出当前球，
#             group.remove(each)
#             # 判断当前球是否与其他球发生了碰撞
#             if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
#                 each.speed[0] = -each.speed[0]
#                 each.speed[1] = -each.speed[1]
#             # 再将当前球添加回组中
#             group.add(each)
#
#         pygame.display.flip()
#         clock.tick(30)
#
# if __name__ == '__main__':
#     main()
    
    
    
'''
    2.让小球响应光标的移动频率，当鼠标的移动速度符合某个频率段时，小球将停下来并变成绿色
      鼠标移动会不停的产生事件，我们只需要让小球相应1s时间内不同数量的事件
      
      做法如下：
        (1) 为每个小球设定一个不同的目标
        (2) 创建一个motion变量来记录鼠标每1s产生的事件数量
        (3) 为小球添加一个check()方法，用于判断鼠标在1s时间内产生的事件数量是否匹配此目标
        (4) 添加一个自定义事件，每1s触发一次。调用每个小球的check()检测的是motion的值是否
            匹配某一个小球的目标，并将motion重新初始化，以便记录1s内鼠标事件的数量
        (5) 小球应该添加一个control属性，用于记录当前的状态(绿色：玩家控制，或者灰色:随机移动)
        (6) 通过检查control属性决定绘制什么颜色的小球
'''

# 18_8_2.py
import pygame
import sys
from pygame.locals import *
from random import *


# 创建玻璃类
class Glass(pygame.sprite.Sprite):
    def __init__(self, glass_image, mouse_image, bg_size):
        # 初始化
        pygame.sprite.Sprite.__init__(self)

        self.glass_image = pygame.image.load(glass_image).convert_alpha()
        self.glass_rect = self.glass_image.get_rect()
        self.glass_rect.left, self.glass_rect.top = (bg_size[0] - self.glass_rect.width) // 2, (
                    bg_size[1] - self.glass_rect.height)
        
        self.mouse_image = pygame.image.load(mouse_image).convert_alpha()
        self.mouse_rect = self.mouse_image.get_rect()
        self.mouse_rect.left, self.mouse_rect.top = self.glass_rect.left, self.glass_rect.top

        # 设置鼠标为不可见
        pygame.mouse.set_visible(False)


# Sprite模块提供了一个动画精灵的基类，可以实现碰撞效果
# 球类继承Sprite类
class Ball(pygame.sprite.Sprite):
    def __init__(self, grayball_image, green_image, position, speed, bg_size, target):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)

        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.green_image = pygame.image.load(green_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        # 将小球放到指定位置
        self.rect.left, self.rect.top = position
        self.speed = speed
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2
        self.target = target
        self.control = False
    
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
    
    #检查鼠标移动产生的事件和该球的频率是否一样
    def check(self, motion):
        #要求100%匹配是很难的，所以需要降低游戏难度
        if self.target -  2 < motion < self.target + 2:
            return True
        else:
            return False

def main():
    pygame.init()
    
    greenball_image = "image/green_ball.png"
    grayball_image = "image/gray_ball.png"
    bg_image = "image/background.png"
    glass_image = "image/glass.png"
    mouse_image = "image/hand.png"
    running = True
    
    # 添加魔性的背景音乐
    pygame.mixer.music.load("image/bg_music.ogg")
    pygame.mixer.music.play()
    
    # 添加音效
    loser_sound = pygame.mixer.Sound("image/loser.wav")
    laugh_sound = pygame.mixer.Sound("image/laugh.wav")
    winner_sound = pygame.mixer.Sound("image/winner.wav")
    hole_sound = pygame.mixer.Sound("image/hole.wav")
    
    # 音乐播放完游戏结束
    # 这里我们创建一个自定义事件GAMEOVER，语法如下：
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER)  # 当音乐播放完时，发送这个事件
    
    # 根据背景图片指定游戏界面尺寸
    bg_size = width, height = 1024, 681
    screen = pygame.display.set_mode(bg_size)
    pygame.display.set_caption("实现球的运动")
    
    background = pygame.image.load(bg_image).convert_alpha()
    # 生成用于“摩擦摩擦”的玻璃面板
    area = Glass(glass_image, mouse_image, bg_size)
    
    # 用来存放小球对象
    balls = []
    group = pygame.sprite.Group()
    
    # 创建五个小球
    for i in range(5):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, width - 100)
        speed = [randint(-10, 10), randint(-10, 10)]
        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i + 1))
        # 检查是否发生碰撞
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        group.add(ball)
        balls.append(ball)
    
    #用来记录鼠标在玻璃面板上产生的事件数量
    motion = 0
    
    # 自定义事件 1s检查一次摩擦
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000) # 每1s执行一次
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # 当音乐播放完时，便会发送一个GAMEOVER事件
            # 捕捉这个事件并退出游戏
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(3000)
                laugh_sound.play()
                running = False
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 1
            elif event.type == MOUSEMOTION:
                motion += 1
            
        screen.blit(background, (0, 0))
        screen.blit(area.glass_image, area.glass_rect)

        # 获取鼠标当前位置, 并设置代替光标的图片
        area.mouse_rect.left, area.mouse_rect.top = pygame.mouse.get_pos()
        # 限制鼠标只能在玻璃内移动
        if area.mouse_rect.left < area.glass_rect.left:
            area.mouse_rect.left = area.glass_rect.left
        if area.mouse_rect.left > area.glass_rect.right - area.mouse_rect.width:
            area.mouse_rect.left = area.glass_rect.right - area.mouse_rect.width
        if area.mouse_rect.top < area.glass_rect.top:
            area.mouse_rect.top = area.glass_rect.top
        if area.mouse_rect.top > area.glass_rect.bottom - area.mouse_rect.height:
            area.mouse_rect.top = area.glass_rect.bottom - area.mouse_rect.height
        # 绘制玻璃面板
        screen.blit(area.mouse_image, area.mouse_rect)
        
        for each in balls:
            each.move()
            if each.control:
                screen.blit(each.green_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)
            
        for each in group:
            # 先从组移出当前球，
            group.remove(each)
            # 判断当前球是否与其他球发生了碰撞
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.speed[0] = -each.speed[0]
                each.speed[1] = -each.speed[1]
            # 再将当前球添加回组中
            group.add(each)
        
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()