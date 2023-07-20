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

# 给表头数据添加样式   颜色设置为红色
header_style = xlwt.XFStyle()
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
# 0-黑色  1-白色 2-红色 3-绿色 4-蓝色 5-黄色 6-粉色 7-青色
pattern.pattern_fore_colour = 2
header_style.pattern = pattern

# 设置字体
font = xlwt.Font()
font.name = "华文楷体"
# 字体大小(20是基准单位  18表示18px)
font.height = 20 * 18

# 是否使用粗体
font.bold = True
# 是否使用斜体
font.italic = True
# 字体颜色
font.colour_index = 1
# 添加样式
header_style.font = font

# 设置对齐方式
align = xlwt.Alignment()
# 垂直方向的对齐方式
align.vert = xlwt.Alignment.VERT_CENTER
# 水平方向的对齐方式
align.horz = xlwt.Alignment.HORZ_CENTER
header_style.alignment = align

# 设置边框
borders = xlwt.Borders()

props = (
    ('top','top_colour'),('right','right_colour'),
    ('bottom','bottom_colour'),('left','left_colour')
)

# 通过循环设置边框四个方向的样式
for position,color in props:
    # 使用setattr内置函数动态给对象指定的属性设置值
    setattr(borders,position,xlwt.Borders.DASHED)
    setattr(borders,color,5)
header_style.borders = borders

# 设置行高的值
sheet.row(0).set_style(xlwt.easyxf(f'font:height {20 * 40}'))

for index,title in enumerate(titles):
    # 设置列宽为200px
    sheet.col(index).width = 20 * 200
    # 第一个参数表示行  第二个参数表示列  第三个参数表示内容 第四个参数表示样式
    sheet.write(0,index,title,header_style)

# 将学生的姓名和成绩写入到工作表中
for row in range(len(scores)):
    sheet.write(row+1,0,students[row])
    for col in range(len(scores[row])):
        sheet.write(row+1,col+1,scores[row][col])

# 将工作表数据保存到工作簿中去
wb.save("添加了样式的考试成绩.xls")
         


