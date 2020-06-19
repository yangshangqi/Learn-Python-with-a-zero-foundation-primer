# autor: zhumenger

'''
    定制一个计时器的类
'''
import time as t
class MyTimer:
    def __init__(self):
        self.unit = ['年', '月', '天', '小时', '分钟', '秒']
        self.prompt = "未开始计时"
        self.lasted = []
        self.begin = 0
        self.end = 0
    def __str__(self):
        return self.prompt
    def __repr__(self):
        return self.prompt
    def start(self):
        self.begin = t.localtime()
        self.prompt = "提示：请先调用stop()结束计时"
        print("计时开始^_^")
    def stop(self):
        if not self.begin:
            print("提示：请先调用stop（）开始计时")
        else:
            self.end = t.localtime()
            self._calc()
            print("计时结束")
    def _calc(self):
        self.lasted = []
        self.prompt = "总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted[index]:
                self.prompt += (str(self.lasted[index])) + self.unit[index]
        self.begin = 0
        self.end = 0
    def __add__(self, other):
        prompt = "总共运行了"
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index])) + self.unit[index]
        return prompt
t1 = MyTimer()
print(t1)
t1.stop()
t1.start()
for i in range(100000000):
    l = i
t1.stop()
print(t1)

t2 = MyTimer()
t2.start()
for i in range(70000000):
    l = i
t2.stop()
print(t2)
print(t1 + t2)