# autor: zhumenger

'''
    一.入门：
        python通过调用 urllib 库访问互联网，url即网址，lib是library(库)的缩写
        
        通过调用 urllib.request.urlopen()函数就可以访问网页了
'''

#1.1.py
# import urllib.request
#
# response = urllib.request.urlopen('https://www.baidu.com/?tn=62095104_19_oem_dg') #打开百度网址，该函数将会返回一个类
# print(type(response)) #class类型
# html = response.read() #读取该网页的html信息，爬取的内容是以 utf-8 编码的bytes对象
# print(html) #打印的时候字符串前面有个 b，表示这是一个bytes对象
#
# #要还原成带中文的html代码，需要对其进行解码，将它变成Unicode编码
# html = html.decode("utf-8")
# print(html)
# print("=======================")

'''
    二.更好的选择：python requests库
        requests 是python所有模块中最受欢迎的一个，全世界最优秀的程序员都在使用它
        使用它的get方法就可以从服务器上下载网页, 但下载下来的是网页的源代码，不利于检索需要的数据，
        
        因此我们可以使用beautifulSoup4对网页进行解析
        Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,每个节点都是Python对象,
        beautifulSoup4库详解：https://www.jb51.net/article/65287.htm
        
        requests库详解：
            requests.request() 构造一个请求，支撑以下各方法的基础方法
            requests.get() 获取HTML网页的主要方法，对应于HTTP的GET   返回一个Response对象
            requests.head() 获取HTML网页头信息的方法，对应于HTTP的HEAD
            requests.post(）向HTML网页提交POST请求的方法，对应于HTTP的POST
            requests.put(）向HTML网页提交PUT请求的方法，对应于HTTP的PUT
            requests.patch() 向HTML网页提交局部修改请求，对应于HTTP的PATCH
            requests.delete() 向HTML页面提交删除请求，对应于HTTP的DELETE
            
            response对象的属性：
                r.status_code HTTP请求的返回状态，200表示连接成功，404表示失败
                r.text        HTTP响应内容的字符串形式，即，url对应的页面内容
                r.encoding    从HTTP header中猜测的响应内容编码方式
                r.apparent_encoding 从内容中分析出的响应内容编码方式（备选编码方式）
                r.content     HTTP响应内容的二进制形式
'''

# 2_1.py
# import requests as r
# import bs4
# headers = {"user-agent": "Mizilla/5.0"}   #这个网站设置了反爬取措施，可以手动更改user-agent的值
# res = r.get("https://movie.douban.com/top250", headers = headers)
# #print(res.text)
# soup = bs4.BeautifulSoup(res.text, "html.parser")
#
# #通过查看网页的源代码，我们发现电影的名字全部在<div class = 'hd'>中，具体路径为 .a.span.text
# targets = soup.find_all("div", class_ = 'hd')
# for each in targets:
#     print(each.a.span.text)