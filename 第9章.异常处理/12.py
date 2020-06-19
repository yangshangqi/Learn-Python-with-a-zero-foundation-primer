# autor: zhumenger
class Yichang(Exception):
    def __init__(self, flag):
        self.flag = flag


def jianfa(a, b):
    try:
        if (a < b):
            raise Yichang(a < b)
        else:
            print(a - b)
    except Yichang:
        print("被减数不能小于减数")


jianfa(2, 1)