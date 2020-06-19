# autor: zhumenger
'''
使用pickle模块可以将列表、字典这类复杂数据结构类型存储为文件,
'''

import pickle
my_list = [123, 3.14, '小甲鱼', ['anther list']]
pickle_file = open("F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理\my_list.pkl", 'wb')
pickle.dump(my_list, pickle_file)
pickle_file.close()

'''
    用二进制的形式打开文件，使用dump方法向文件中保存该列表信息
    使用的时候只需要用二进制模式打开，然后用load把数据加载进来
'''
pickle_file = open("F:\代码文件集\python代码文件\小甲鱼入门学习\第8章.文件处理\my_list.pkl", 'rb')
my_list = pickle.load(pickle_file)
print(my_list)