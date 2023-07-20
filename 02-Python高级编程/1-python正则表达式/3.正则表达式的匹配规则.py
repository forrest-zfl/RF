import re
'''  
以下匹配规则只能匹配一个字符
. : 表示除了换行符以外的所有的字符
[] :表示的是一个范围
- : 表示的是一个区间
[0123456789]: []表示集合,表示匹配[]中的任意一个字符
[a-z]: 匹配任意的一个小写字母
[A-Z]: 匹配任意的一个大写字母
[0-9a-zA-Z]:匹配任意的数字和字母
[^0-9]: 匹配任意的一个非数字字符
\d: 表示匹配0-9之间任意的数字 等同于 [0-9]
\D: 表示对\d进行取反,匹配任意的非数字字符  等同于 [^0-9]
\w: 表示匹配任意的数字 字母 和下划线  等同于 [0-9a-zA-Z_]
\W: 表示对\w进行取反,匹配数字 字母 下划线之外任意字符
\s: 表示匹配任意的空白符(空格  换行  回车  制表符)  等同于[\r\t\n\f]
\S: 表示对\s进行取反

print(re.search("he[0-9]llo","he87llo"))  # None 因为 [0-9]只能匹配一个数字
print(re.search("he[0-9]llo","he8llo"))   # <re.Match object; span=(0, 6), match='he8llo'>

print(re.search("98[a-z]76","98f76"))   # <re.Match object; span=(0, 5), match='98f76'>
print(re.search("98[A-Z]76","98H76"))   # <re.Match object; span=(0, 5), match='98H76'>
print(re.search("apple\d","apple9"))    # <re.Match object; span=(0, 6), match='apple9'>
print(re.search("8765\D","8765f"))      # <re.Match object; span=(0, 5), match='8765f'>
print(re.search("banana\D","banana5"))  # None
print(re.search("good\w","good4"))      # <re.Match object; span=(0, 5), match='good4'>
print(re.search("322\w","322k"))        # <re.Match object; span=(0, 4), match='322k'>
print(re.search("785\w","785_"))        # <re.Match object; span=(0, 4), match='785_'>
print(re.search("785\W","785@"))        # <re.Match object; span=(0, 4), match='785@'>
print(re.search("785\W","785s"))        # None

'''
# 模式修正符: 主要是用于修饰正则表达式
'''
re.S:可以让正则表达式匹配换行   \n表示换行
re.I: 可以让正则表达式忽略字母大小写

print(re.search('shenzhen.','shenzhen875ds'))   # <re.Match object; span=(0, 9), match='shenzhen8'>
print(re.search('shenzhen.','shenzhen\n'))    # None
print(re.search('shenzhen.','shenzhen\n',re.S))  # <re.Match object; span=(0, 9), match='shenzhen\n'>

print(re.search("98765[a-z]","98765asw"))  # <re.Match object; span=(0, 6), match='98765a'>
print(re.search("98765[a-z]","98765DGH"))  # None
print(re.search("98765[a-z]","98765DGH",re.I))  # <re.Match object; span=(0, 6), match='98765D'>
'''

# 匹配多个字符:
'''
? :表示匹配前面的字符出现0次或者1次
+ :表示匹配前面的字符出现1次或者多次    贪婪模式
* :表示匹配前面的字符出现0次或者多次    贪婪模式
{} :表示匹配前面的字符可以出现指定的次数或者出现指定范围内的次数,   贪婪模式
{4}: 表示前面的字符只能出现4次
{4,9}:表示前面的字符可以出现4-9次
{4,}: 表示前面的字符至少出现4次
{,4}: 表示前面的字符最多可以出现4次
'''
print(re.search("face?book","facebook"))  # <re.Match object; span=(0, 8), match='facebook'>   e出现1次的情况
print(re.search("face?book","facbook"))   # <re.Match object; span=(0, 7), match='facbook'>   e出现0次情况
print(re.search("face+book","facebook"))  # <re.Match object; span=(0, 8), match='facebook'>  e出现1次的情况
print(re.search("face+book","faceeeeeebook"))  # <re.Match object; span=(0, 13), match='faceeeeeebook'>    e出现多次的情况

print(re.search("face*book","facbook"))   # <re.Match object; span=(0, 7), match='facbook'>  e出现0次的情况
print(re.search("face*book","faceeeebook"))  # <re.Match object; span=(0, 11), match='faceeeebook'>  e出现多次的情况
print(re.search("face{4}book","faceeeebook"))   # <re.Match object; span=(0, 11), match='faceeeebook'>    e出现4次的情况
print(re.search("face{4}book","faceeeeeeebook"))  # None   e出现不是4次的情况
print(re.search("face{4,9}book","faceeeeeeebook"))  # <re.Match object; span=(0, 14), match='faceeeeeeebook'>  e出现4-9次的情况
print(re.search("face{4,9}book","faceeebook"))  # None    e出现不是4-9次的情况
print(re.search("face{4,}book","faceeeeeebook"))  # <re.Match object; span=(0, 13), match='faceeeeeebook'>  e出现至少4次的情况
print(re.search("face{,4}book","faceebook"))   # <re.Match object; span=(0, 9), match='faceebook'>   e最多出现4次的情况

