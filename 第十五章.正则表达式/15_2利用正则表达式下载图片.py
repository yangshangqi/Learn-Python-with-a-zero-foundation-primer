# autor: zhumenger

'''

    利用正则表达式爬取魁拔评论壁纸
    目标url：https://tieba.baidu.com/p/2129062551#!/l/p1
'''

import requests as r
import re

def open_url():
    url = "https://tieba.baidu.com/p/2129062551#!/l/p1"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"}
    res = r.get(url, headers = headers)
    html = res.text
    return html
def get_img(html):
    
    # 下面这种方法得到的是<img>这个标签的信息，我们需要的是图片的链接
    # p = r'<img class="BDE_Image".*?src="[^"]*\.jpg".*?>'
    # imglist = re.findall(p, html)
    # for each in imglist:
    #     print(each)

    # 使用子组的方式, 只会返回小括号中的正则表达式, 从而得到我们想要的内容
    p = r'<img class="BDE_Image".*?src="([^"]*\.jpg)".*?>'  # 正则表达式，
    imglist = re.findall(p, html)
    i = 0
    for each in imglist:
        imgtext = r.get(each)
        with open("魁拔%d.jpg" % i, 'wb') as f:
            f.write(imgtext.content)
            i += 1
if __name__ == '__main__':
    html = open_url()
    get_img(html)