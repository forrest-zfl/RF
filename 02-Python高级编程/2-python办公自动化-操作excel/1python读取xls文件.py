import xlrd # 该模块用于读取xls文件
# 获取xls文件中的工作对象
wb = xlrd.open_workbook(r"C:\python07\day17\笔记\resources\阿里巴巴2020年股票数据.xls")
# print(wb)
# 获取所有的工作表名称
sheet_names = wb.sheet_names()
# print(sheet_names)
# 通过工作表名称获取具体的工作表对象
sheet = wb.sheet_by_name(sheet_names[0])
# 查看指定工作表的行数和列数
# print(sheet.nrows,sheet.ncols)
# 通过循环的方式查看工作表中具体单元格的数据
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        # print(row,col)
        # 通过cell对象中的value属性获取具体单元格的值
        value = sheet.cell(row,col).value
        # print(value)
        # 将第一行以外的数据进行格式化处理
        if row > 0:
            # 将第一列的日期数据转换为年月日的形式
            if col == 0:
                value = xlrd.xldate_as_tuple(value,0)
                # print(value)  # (2019, 12, 31, 0, 0, 0)
                value = f"{value[0]}年{value[1]:>02d}月{value[2]:>02d}日"
            else:
                # 将其他列的数据处理成小数位数为2位的数据
                value = f"{value:.2f}"
        #print(value,end="\t")
    #print()

# 获取单元格值的类型
# 0-空值   1-字符串   2-数字  3-日期   4-布尔  5-错误
last_cell_type = sheet.cell_type(sheet.nrows-1,sheet.ncols-1)
print(last_cell_type)

# 获取第一行的数据
print(sheet.row_values(0))
