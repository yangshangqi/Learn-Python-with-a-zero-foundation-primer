# autor: zhumenger

def Test():
    print("模块内部调用的方法")
def ha():
    print("模块外部调用的方法")
    
if __name__ == '__main__':
    Test()