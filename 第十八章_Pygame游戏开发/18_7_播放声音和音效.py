# autor: zhumenger

'''
    对于游戏，分为背景音乐和音效俩种
    pygame支持的声音格式十分有限，一般情况下使用ogg格式作为背景音乐，用无压缩的wav格式作为音效
    
    播放音效使用mixer模块，需要先生成一个Sound对象，调用play()方法播放
        play(): 播放
        stop(): 停止播放
        fadeout(): 淡出
        set_volume(): 设置音量
        get_volume(): 获得音量
        get_num_channels(): 计算该音效被播放了多少次
        get_length(): 获得该音效的长度
        get_raw(): 将该音效以二进制格式的字符串返回
    
    播放背景音乐用的music模块，使用pygame.mixer.music来调用
        load(): 载入音乐
        play(): 播放
        stop(): 停止播放
        rewind(): 重新播放
        pause(): 暂停播放
        uppause(): 恢复播放
        fadeout(): 淡出
        set_volume(): 设置音量
        get_volume(): 获得音量
        get_buy(): 检测音乐是否在播放
        set_pos(): 设置开始播放的位置
        get_pos(): 获取已经播放的时间
        queue(): 将音乐文件放入到待播放列表中
        set_endevent(): 在音乐播放完毕时发送事件
        get_endevent(): 获取音乐播放完毕时发送的事件类型
'''


#打开程序便播放背景音乐，单击播放猫叫，右击播放狗叫，空格暂停音乐
# 18-7-1.py
#
# import pygame
# import sys
# from pygame.locals import *
#
# pygame.init()
# #初始化混音器模块
# pygame.mixer.init()
#
# #加载背景音乐
# pygame.mixer.music.load("image/bg_music.ogg")
# pygame.mixer.music.set_volume(0.2)
# pygame.mixer.music.play()
#
# #加载音效
# cat_sound = pygame.mixer.Sound("image/cat.wav")
# cat_sound.set_volume(0.2)
# dog_sound = pygame.mixer.Sound("image/dog.wav")
# dog_sound.set_volume(0.2)
#
# bg_size = width, height = 300, 200
# screen = pygame.display.set_mode(bg_size)
# pygame.display.set_caption("播放音乐")
#
# pause = False
# pause_image = pygame.image.load("image/pause.png").convert_alpha()
# unpause_image = pygame.image.load("image/unpause.png").convert_alpha()
# pause_rect = pause_image.get_rect()
# pause_rect.left, pause_rect.top = (width - pause_rect.width) // 2, (height - pause_rect.height) // 2
#
# clock = pygame.time.Clock()
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         if event.type == MOUSEBUTTONDOWN:
#             if event.button == 1:
#                 cat_sound.play()
#             if event.button == 3:
#                 dog_sound.play()
#         if event.type == KEYDOWN:
#             if event.key == K_SPACE:
#                 pause = not pause
#
#     screen.fill((255, 255, 255))
#
#     if pause:
#         screen.blit(pause_image, pause_rect)
#         pygame.mixer.music.pause()
#     else:
#         screen.blit(unpause_image, pause_rect)
#         pygame.mixer.music.unpause()
#
#     pygame.display.flip()
#
#     clock.tick(30)




# 18-6-1.py 现在我们将音乐放入到我们的游戏中去
import pygame
import sys
from pygame.locals import *
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
    
    #添加魔性的背景音乐
    pygame.mixer.music.load("image/bg_music.ogg")
    pygame.mixer.music.play()
    
    #添加音效
    loser_sound = pygame.mixer.Sound("image/loser.wav")
    laugh_sound = pygame.mixer.Sound("image/laugh.wav")
    winner_sound = pygame.mixer.Sound("image/winner.wav")
    hole_sound = pygame.mixer.Sound("image/hole.wav")
    
    #音乐播放完游戏结束
    #这里我们创建一个自定义事件GAMEOVER，语法如下：
    GAMEOVER = USEREVENT
    pygame.mixer.music.set_endevent(GAMEOVER) # 当音乐播放完时，发送这个事件
    
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
            # 当音乐播放完时，便会发送一个GAMEOVER事件
            # 捕捉这个事件并退出游戏
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(3000)
                laugh_sound.play()
                running = False
        
        screen.blit(background, (0, 0))
        
        for each in balls:
            each.move()
            screen.blit(each.image, each.rect)
        
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