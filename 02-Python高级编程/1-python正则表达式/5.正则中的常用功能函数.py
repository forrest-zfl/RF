import re
'''
1.re.compile()  编译正则表达式,用于提高正则匹配的效率
'''
string = "010-87458345"
com = re.compile('(\d{3})-(\d{8})')  # 编译正则表达式
print(com.findall(string))   #  [('010', '87458345')]

# 2.re.split()  按照指定的正则表达式拆分
print(re.split('\d','hello12world35boy'))  # ['hello', '', 'world', '', 'boy']

# 3.匹配中文
chinese = "[\u4e00-\u9fa5]+"
print(re.search(chinese,'hello 你好 world 世界 girl 女孩'))  # <re.Match object; span=(6, 8), match='你好'>

# 4.re.sub 和 re.subn()  替换字符中正则匹配到内容为指定字符
# re.subn() 会显示替换的总次数
str1 = "下周 大家就开始 进入年假 模式,提前祝大家 新春快乐"
print(re.sub("\s+",'.......',str1))  # 下周.......大家就开始.......进入年假.......模式,提前祝大家.......新春快乐
print()
print(re.subn("\s+",'.......',str1))  # ('下周.......大家就开始.......进入年假.......模式,提前祝大家.......新春快乐', 4)

