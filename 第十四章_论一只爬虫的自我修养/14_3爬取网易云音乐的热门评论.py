# autor: zhumenger

# 14_3_1.py 将网易云音乐网页内容存到本地
# import requests as r
# def get_url(url):
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
#     res = r.get(url, headers = headers)
#     return res
# def main():
#     url = input("请输入链接地址")
#     res = get_url(url)
#     with open("res.txt", 'w', encoding = 'utf-8') as f:
#         f.write(res.text)
# if __name__ == '__main__':
#     main()


'''
    可能由于网页加密的原因，通过上面的代码，我们无法得到用户具体的评论内容
    我们可以通过缓慢的加载网页来得到我们想要的信息，通过调查发现，我们需要的信息是一个post文件，
    必须向服务器提供一些必要的数据才能得到我们想要的内容(具体内容，从from data中查找)
    
    通过以下的代码我们就可以得到我们想的评论内容了
'''

# 14_3_2.py 通过向网页提交post请求来得到我们想要的信息
#
# import requests as r
#
# def get_comments(url):
#     headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
#     params = "SL + M + KTSTk0s / X3PooyztLfuit48aKGMar6BU9r7vrU + zhV7bX / vnorI2vX2joc4PREI9o9LLfiQGxNrYKHiWb7Jya2jTX8FTxU33urwIyD1wcu5mDDbzSimk + e3ZDiVeI9D4axjcvAqr + OiRji021ukrMAeJ61aJogXz5vpNw + 20egZlZiYdeBMGrfHFf9H"
#     encSecKey = "3bb4d5bf1f1ff3757c433177256f227d60af50aa5d31ce5d78b829416ae645f702ecdb9f596d1f9aa8ec2ba139ae1ffc05501768ffbfb4afe0019a1020c12ea53c165d6293623ea17453619655ed38daee1b67ab8dcef23dacfc0ae84d2379459460ae221692f5dc614ef1e662ffc27a7412eb171df6d613804e3b132d2a27fe"
#     data = {
#         "params": params,
#         "encSecKey": encSecKey
#     }
#
#     #得到网页链接的ID??
#     name_id = url.split('=')[1]
#
#     #得到该post文件的url??
#     target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
#     res = r.post(target_url, headers = headers, data = data)
#     return res
#
# def main():
#     url = input("请输入链接地址")
#     res = get_comments(url)
#     with open("data1.txt", 'w', encoding = 'utf-8') as f:
#         f.write(res.text)
# if __name__ == '__main__':
#     main()


'''
    接下来就是提取关键数字的阶段，data1.txt文件中的数据是JSON格式，JSON是一种轻量级的数据交换格式,
    使用字符串python的数据结构给封装起来了，操作JSON格式的数据，通常有json.loads和json.dumps方法
    
    将字符串变为python的数据结构
    commetns_json = json.loads(res.text)
    
    完整的代码如下：
'''

# 14_3_3.py

import requests as r
import json

def get_hot_commetns(res):
    comments_json = json.loads(res.text)
    hot_comments = comments_json['hotComments']
    with open("data2.txt", 'w', encoding = 'utf-8') as f:
        for each in hot_comments:
            f.write(each['user']['nickname'] + ': \n\n')
            f.write(each['content'] + '\n')
            f.write("--------------------------\n")

def get_comments(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'}
    params = "SL + M + KTSTk0s / X3PooyztLfuit48aKGMar6BU9r7vrU + zhV7bX / vnorI2vX2joc4PREI9o9LLfiQGxNrYKHiWb7Jya2jTX8FTxU33urwIyD1wcu5mDDbzSimk + e3ZDiVeI9D4axjcvAqr + OiRji021ukrMAeJ61aJogXz5vpNw + 20egZlZiYdeBMGrfHFf9H"
    encSecKey = "3bb4d5bf1f1ff3757c433177256f227d60af50aa5d31ce5d78b829416ae645f702ecdb9f596d1f9aa8ec2ba139ae1ffc05501768ffbfb4afe0019a1020c12ea53c165d6293623ea17453619655ed38daee1b67ab8dcef23dacfc0ae84d2379459460ae221692f5dc614ef1e662ffc27a7412eb171df6d613804e3b132d2a27fe"
    data = {
        "params": params,
        "encSecKey": encSecKey
    }

    #得到网页链接的ID??
    name_id = url.split('=')[1]

    #得到该post文件的url??
    target_url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token=".format(name_id)
    res = r.post(target_url, headers = headers, data = data)
    return res

def main():
    url = input("请输入链接地址")
    res = get_comments(url)
    get_hot_commetns(res)
if __name__ == '__main__':
    main()