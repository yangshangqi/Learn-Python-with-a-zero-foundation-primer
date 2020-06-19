# autor: zhumenger

'''
1.lambda表达式:
    lambda表达式的语法非常精简,基本语法是在冒号：左边放原函数的参数，可以有多个参数，用逗号(,) 隔开即可
    冒号右边是返回值
    在写python脚本的时候，使用lambda可以省下定义函数的过程，代码更加简洁
'''

g = lambda x : 2 * x + 1;
print(g(5))

'''
2.filter():
    filter有俩个参数,第一个参数为函数，第二参数集合里面的元素可作为函数的参数进行计算,
    把返回为True的值筛选出来，如果第一个参数为None，则直接将第二个参数中为True的值筛选出来
'''

temp = filter(None, [1, 0, False, True])
print(list(temp))
# [1, True]

#一行代码筛选10以内的奇数
print(list(filter(lambda x : x % 2, range(10))))

'''
3.map():
    map是映射的意思,有俩个参数，仍然是一个函数和一个可迭代序列，将序列中的每一个元素作为函数的参数
    进行运算加工，直到可迭代序列每个元素都加工完毕，返回所有加工后的元素构成的新序列
'''

print(list(map(lambda x : x * 2, range(10))))