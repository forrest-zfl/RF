import re
# \d: 表示 0-9之间的任意数字
# +: 表示前面的内容可以出现1次或者多次

'''
1.re.match(正则表达式,要验证的字符串,可选参数(修饰符))
作用: 匹配字符串是否以指定的正则内容开头,若匹配成功,返回对象,若匹配失败,返回None
'''
#print(re.match('\d+','123dsdg678'))  # <re.Match object; span=(0, 3), match='123'>
#print(re.match('\d+','dshjhj123dsdg678'))   # None

'''
2.re.search(正则表达式,要验证的字符串,可选参数(修饰符))
作用: 匹配字符串是否包含指定的正则内容,若匹配成功,返回对象,若匹配失败,返回None
'''
# print(re.search('\d+','123dsdg678'))   # <re.Match object; span=(0, 3), match='123'>
# print(re.search('\d+','dshjhj123dsdg678'))  # <re.Match object; span=(6, 9), match='123'>

'''
3.re.findall(正则表达式,要验证的字符串)
作用: 使用正则表达式获取匹配成功的数据,返回的是一个列表
'''
print(re.findall('\d+','hsjdhsj134243dshkdhks9877dhsjh5665dsd54778'))   # ['134243', '9877', '5665', '54778']