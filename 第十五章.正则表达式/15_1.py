# autor: zhumenger
'''
    正则表达式：
        用于查找符合某些复杂规则的字符串

        1.re模块：
            python通过re模块来实现正则表达式

            search(): 用于在字符串中搜索正则表达式模式下第一次出现的位置
                      第一个参数为正则表达式模式,即搜索规则，
                      字符串下标从0开始，如果没有找到则返回None
        2.通配符:
            在python中可以使用通配符('.')来匹配任意一个字符(除换行符外)
            如：.txt, 可以寻找所有以txt结尾的字符串
                doc. 可以寻找所有以doc开头的字符串
        3.反斜杠:
            1).如果就是想寻找一个'.'字符本身，我们可以在它前面加上反斜杠，消除它的特殊功能
            2).如果想要匹配一个数字, 可以使用反斜杠加上小写字母d(\d)
'''

# 15_1.py
import re

print(re.search('FishC', 'I love FishC.com!'))
print(re.search('haha', 'xixi'))

#通配符
print(re.search(r'.txt', 'hahahha hulalatxt'))
print(re.search(r'ha...', "hahahahahaha lala"))

#反斜杠
print(re.search('\.', 'haha.xixi'))

#匹配数字
print(re.search(r'\d\d\d', 'I love 521 you'))
#匹配一个IP地址
print(re.search(r'\d\d\d.\d\d\d.\d\d\d.\d\d\d', 'other198.168.111.253other'))

print('====================')

'''
    4.字符类
        1).用来表示一个字符的范围,使用中括号将任何内容包起来就是一个字符类
           只要匹配到这个字符类中的任何字符，结果就算做匹配成功
        2).可以使用小横杠来表示范围
        
'''

#匹配元音字母
print(re.search(r'[aeiou]', 'I love you!'))

#使用小横杠来表示字符范围
print(re.search(r'[a-z]', 'TVT I LOVE you'))

#使用小横杠来表示数字范围
print(re.search(r'[0-9][0-9][0-9]', 'I love 521 you'))
print("======================")

'''
    5.重复匹配
        匹配个数问题：使用大括号这对元字符来实现重复匹配的功能
'''

#重复匹配
print(re.search(r'ab{3}c', 'abbbc'))

#重复的次数也可以是一个范围
print(re.search(r'ab{3,5}c', 'abbbc'))
print(re.search(r'ab{3,5}c', 'abbbbbc'))

#多个字符重复匹配,将需要查询的多个字符用()括起来
print(re.search(r'(ab){3}c', 'abababc'))

#匹配0-255这个范围的数字
print(re.search(r'[0-1]\d\d|2[0-4]\d|25[0-5]', '188'))

#匹配IP地址:
print(re.search(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])', 'other192.168.10.1other'))

print("=========================")

'''
    6.元字符
        . ^ $ * + ? {} [] \ | () 这些都是元字符
        点号(.)：表示匹配除换行符外的任何字符
        |:表示逻辑或
        ^:表示匹配字符串的开始位置, 只有目标字符串出现在开头才会匹配
        $:匹配字符串的结束位置，只有目标字符串出现在末尾才会匹配
        \:将一个普通字符变成特殊字符：
            如果后面跟着的数字是1~99，那么它表示引用序号对应的子组所匹配的字符串
            如果后面跟着的是数字0或者是三位数字，那么它是一个八进制数
            被()括起来的正则表达式称为一个子组
        []:字符集合，被它包围在里边的字符都失去了特殊功能，除了几个特殊的字符：
            1).小横杠(-):用来表示范围
            2).反斜杠(\):用于字符串转义,如\n
            3).脱节符(^):表示取反
        {}：匹配多次
        在正则表达式中，空格不能随便使用
            如：匹配多次{1,3}, 写成{1, 3} 就会失效
        星号(*) 相当于{0,}
        加号(+) 相当于{1,}
        问号(?) 相当于{0,1}
'''

#逻辑或
print(re.search('Fish(C|D)','FishC'))

#从开始位置匹配字符串
print(re.search('^FishC', 'FishC I love'))
print(re.search('^FishC', 'I love FishC'))

#从结尾位置匹配字符串
print(re.search('FishC$', 'FishC I love'))
print(re.search('FishC$', 'I love FishC'))

#对子组的引用, \1表示引用前面序号为1的子组，所以r"FishC\1" == "FishCFishC"
print(re.search(r'(FishC)\1', 'FishCFishC'))

#通过八进制数匹配, 060在ASCII码的数字为0
print(re.search(r"(FishC)\060", "FishCFishC0"))

#[]里面的字符都是普通的字符
print(re.search('[.]', 'abc.'))
#脱节符(^)表示取反
print(re.findall(r'[^a-z]', 'I Love You!!'))

'''
    7.贪婪与非贪婪
        在正则表达式中默认启用的是贪婪的匹配方式
        即在符合条件的情况下，尽可能多的去匹配
        
'''

s = "<html><head>你好啊！</head></html>"
#由于贪婪模式的原因，它直接匹配了整个字符串
print(re.search(r'<.+>', s))
#希望在第一个'>'的时候就停下来
print(re.search(r'<.+?>', s))

'''
    8.反斜杠+普通字母=特殊含义
        \b:匹配一个单词的边界
        \w:匹配Unicode单词字符
'''
print(re.findall(r"\byou\b", 'youyou you you'))
print(re.findall(r'\w', '我喜欢你!! 521 I love you'))
print("============================")

'''
    9.编译正则表达式
        如果需要重复使用某个匹配规则，我们可以先将该正则表达式编译成模式对象
        使用re.compile()方法
        
        使用编译模式匹配字符串时,可以选择起始和结束位置
        
        当我们使用search()方法匹配字符串时，得到的是一个匹配对象
        可以通过使用group()方法得到匹配的字符串
        start():返回匹配的开始位置
        end():返回匹配的结束位置
        
        span():返回匹配的范围
'''

p = re.compile("[A-Z]")
print(p.search("I Love You"))
s = "I Love You"
print(p.search(s, 6, len(s)))

res = re.search("[A-Z]", "I Love You")
print(res.group())
print(res.start())
