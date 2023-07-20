import re
'''
1.边界符:
^: 行首匹配(以指定字符开头)  和 [^] 不是一个含义
$: 行尾匹配(以指定字符结束)
^文本$: 表示精准匹配

print(re.search('^world','world'))  # <re.Match object; span=(0, 5), match='world'>
print(re.search('^world','aworld'))  # None
print(re.search('world$','world'))  # <re.Match object; span=(0, 5), match='world'>
print(re.search('world$','worldsf')) # None
print(re.search('^world$','world'))  # <re.Match object; span=(0, 5), match='world'>
print(re.search('^world$','wo12rlf3d'))   # None
'''

'''
2. 
\ 表示转义字符,作用是让符号失去原有的意义
. 在正则表达式表示匹配除了换行\n之外的任意字符,  \.这个时候,这个.就是一个普通的符号了

| 表示或者, 正则表达式1 | 正则表达式2  只要满足其中的一个正则表达式即可


print(re.search('goog.le','googlle'))  # <re.Match object; span=(0, 7), match='googlle'>
print(re.search('goog\.le','goog.le'))  # <re.Match object; span=(0, 7), match='goog.le'>

print(re.search('cd|ef','123cd87878'))  # <re.Match object; span=(3, 5), match='cd'>
print(re.search('cd|ef','8765ef434'))   # <re.Match object; span=(4, 6), match='ef'>
'''

'''
3.词边界(了解)
\b: 匹配一个单词的边界,也就是单词和空格之间的位置
\B: 对\b进行取反
'''
print(re.search(r'google\b',"123google hello world"))  # <re.Match object; span=(3, 9), match='google'>
print(re.search(r'google\B',"123google hello world"))  # <re.Match object; span=(3, 9), match='google'>   # None
