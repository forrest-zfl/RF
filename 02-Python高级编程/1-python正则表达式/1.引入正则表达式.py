# 世界上最难懂三门语言:  中医开的药方      道士画的符    程序员写的正则表达式
'''
需求:
封装函数,判断手机号码是否合法?
a.长度是11位
b.数字1开头
c.手机号码的组成全部是数字
'''
def checkPhone(tel):
    if len(tel) != 11:
        return "手机号码的长度不符合要求"
    if tel[0] != "1":
        return "手机号码不是1开头"
    if not tel.isdigit():
        return "手机号码的组成不是全部是数字"
    return  "合法的手机号码"
# print(checkPhone('18617767027'))
# print(checkPhone('28617767027'))
# print(checkPhone('186177670a7'))
# 2. 使用正则表达式验证手机号码是否合法
import re   # 导入正则表达式相关的模块
result = re.search('^1\d{10}$','18617767027')
# print(result)
if result:
    print('手机号码合法')
else:
    print('手机号码不合法')
