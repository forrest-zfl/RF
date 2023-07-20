import xlwt
import random

# 创建工作簿对象
wb = xlwt.Workbook()

# 创建工作表对象
sheet = wb.add_sheet("python-2107班级")
# 定义学生姓名
students = ["刘备","关羽","张飞","黄忠","马超","赵云"]

# 通过列表生成式的方式生成语文  数学  英语 三科的成绩 结果是二维列表
scores = [[random.randrange(50,101) for i in range(3)] for j in range(6)]
# print(scores)

# 创建表头数据
titles = ["姓名","语文","数学","英语"]
for index,title in enumerate(titles):
    # print(index,title)
    # 第一个参数表示行  第二个参数表示列  第三个参数表示具体的内容
    sheet.write(0,index,title)

# 将学生的姓名和成绩写入到工作表中去
for row in range(len(scores)):
    # print(row)
    sheet.write(row+1,0,students[row])  # 从第二行开始写入学生相关的数据信息
    for col in range(len(scores[row])):
        sheet.write(row+1,col+1,scores[row][col])  # 从第二行第二列开始填充成绩数据

# 将工作表数据保存到工作簿中去
wb.save("考试成绩.xls")
         


