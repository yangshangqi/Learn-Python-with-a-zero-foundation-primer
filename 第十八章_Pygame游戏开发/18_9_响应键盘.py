# autor: zhumenger

'''
    当小球变成绿色后，可以通过 w s a d 按键口直小球上下左右移动
    默认情况下，无论是按一下按键还是紧按着不松开，pygame只会发送一个键盘按下的事件
    可以通过设置key模块下的set_repeat()方法，来设置是否响应持续按下某个键
    set_repert(delay, interval)
        第一个参数为第一次发送事件的延迟时间
        第二个参数为重复发送事件的时间事件间隔
    
'''

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
    def __init__(self, grayball_image, greenball_image, position, speed, bg_size, target):
        # 初始化动画精灵
        pygame.sprite.Sprite.__init__(self)
        
        self.grayball_image = pygame.image.load(grayball_image).convert_alpha()
        self.greenball_image = pygame.image.load(greenball_image).convert_alpha()
        self.rect = self.grayball_image.get_rect()
        # 将小球放到指定位置
        self.rect.left, self.rect.top = position
        self.side = [choice([-1, 1]), choice([-1, 1])] # 表示方向
        self.speed = speed  # 表示速度
        self.width, self.height = bg_size[0], bg_size[1]
        self.radius = self.rect.width / 2
        self.target = target
        self.control = False
        self.collide = False # 检查是否发生碰撞
    
    # 实现左进右出，上进下出的效果
    def move(self):
        if self.control:
            self.rect = self.rect.move(self.speed)
        else:
            self.rect = self.rect.move((self.side[0] * self.speed[0], \
                                       self.side[1] * self.speed[1]))
        if self.rect.right <= 0:
            self.rect.left = self.width
        elif self.rect.left >= self.width:
            self.rect.right = 0
        elif self.rect.top >= self.height:
            self.rect.bottom = 0
        elif self.rect.bottom <= 0:
            self.rect.top = self.height

    # 检查鼠标移动产生的事件和该球的频率是否一样
    def check(self, motion):
        # 要求100%匹配是很难的，所以需要降低游戏难度
        if self.target - 2 < motion < self.target + 2:
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
    
    # 五个黑洞的范围, 100%命中率太难，所以在范围内即可
    # 每个元素(x1, x2, y1, y2)
    hole = [(117, 119, 199, 201), (225, 227, 390, 392), \
            (503, 505, 320, 322), (698, 700, 192, 194), \
            (906, 908, 419, 421)]

    # 存放要打印的消息
    msgs = []
    
    # 用来存放小球对象
    balls = []
    group = pygame.sprite.Group()

    # 创建五个小球
    for i in range(5):
        # 位置随机，速度随机
        position = randint(0, width - 100), randint(0, width - 100)
        # 此时速度不再有方向，所以要设成正数
        speed = [randint(1, 10), randint(1, 10)]
        ball = Ball(grayball_image, greenball_image, position, speed, bg_size, 5 * (i + 1))
        # 检查是否发生碰撞
        while pygame.sprite.spritecollide(ball, group, False, pygame.sprite.collide_circle):
            ball.rect.left, ball.rect.top = randint(0, width - 100), randint(0, height - 100)
        group.add(ball)
        balls.append(ball)

    # 用来记录鼠标在玻璃面板上产生的事件数量
    motion = 0
    
    # 自定义事件 1s检查一次摩擦
    MYTIMER = USEREVENT + 1
    pygame.time.set_timer(MYTIMER, 1000)  # 每1s执行一次

    # 持续按键重复响应，
    pygame.key.set_repeat(100, 100)
    
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 当音乐播放完时，便会发送一个GAMEOVER事件
            # 捕捉这个事件并退出游戏
            elif event.type == GAMEOVER:
                loser_sound.play()
                pygame.time.delay(3000)
                laugh_sound.play()
                running = False
            # 1 秒检查 1 次鼠标摩擦摩擦产生的事件数量
            elif event.type == MYTIMER:
                if motion:
                    for each in group:
                        if each.check(motion):
                            each.speed = [0, 0]
                            each.control = True
                    motion = 0
            # 当小球的 control 属性为 True 时
            # 可是使用按键 w、s、a、d 分别上、下、左、右移动小球
            elif event.type == MOUSEMOTION:
                motion += 1
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    for each in group:
                        if each.control:
                            each.speed[1] -= 1
                if event.key == K_s:
                    for each in group:
                        if each.control:
                            each.speed[1] += 1
                if event.key == K_a:
                    for each in group:
                        if each.control:
                            each.speed[0] -= 1
                if event.key == K_d:
                    for each in group:
                        if each.control:
                            each.speed[0] += 1
                # 判断小球是否在坑内
                if event.key == K_SPACE:
                    for each in group:
                        if each.control:
                            for i in hole:
                                if i[0] <= each.rect.left <= i[1] and i[2] \
                                    <= each.rect.top <= i[3]:
                                    hole_sound.play()
                                    each.speed = [0, 0]
                                    #从group中移出，这样其他的球就会忽视它
                                    group.remove(each)
                                    # 放到balls列表的最前面，也就是第一个绘制的球
                                    #这样当球在坑里时，其他的球就会从它上面过去
                                    temp = balls.pop(balls.index(each))
                                    balls.insert(0, temp)
                                    # 一个坑一个球
                                    hole.remove(i)
                            # 都填补完了，游戏结束
                            if not hole:
                                pygame.mixer.music.stop()
                                #播放胜利音乐
                                winner_sound.play()
                                pygame.time.delay(3000)
                                #打印
                                msg = pygame.image.load("image/win.png").convert_alpha()
                                msg_pos = (width - msg.get_width()) // 2, (height - msg.get_height()) //2
                                msgs.append((msg, msg_pos))
                                laugh_sound.play()
                                
                            
            
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
            if each.collide:
                each.speed = [randint(1, 10), randint(1, 10)]
                each.collide = False
            if each.control:
                screen.blit(each.greenball_image, each.rect)
            else:
                screen.blit(each.grayball_image, each.rect)
        
        for each in group:
            # 先从组移出当前球，
            group.remove(each)
            # 判断当前球是否与其他球发生了碰撞
            # 碰撞发生后首先修改的是方向
            if pygame.sprite.spritecollide(each, group, False, pygame.sprite.collide_circle):
                each.side[0] = -each.side[0]
                each.side[1] = -each.side[1]
                each.collide = True
                if each.control:
                    each.side[0] = -1
                    each.side[1] = -1
                    each.control = False
            # 再将当前球添加回组中
            group.add(each)
        for msg in msgs:
            screen.blit(msg[0], msg[1])
        pygame.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()