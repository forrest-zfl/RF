import PyPDF2
# 创建读取pdf文件的对象
reader = PyPDF2.PdfFileReader(r"C:\python基础\28-python办公自动化-操作pdf\XGBoost.pdf")
# 创建写pdf文件的writer对象
writer = PyPDF2.PdfFileWriter()
# 获取pdf文件的所有页码
# print(reader.numPages)   # 13
# 对pdf文件中的所有的页码进行循环遍历
for page_num in range(reader.numPages):
    # 获取当前页码的对象
    current_page = reader.getPage(page_num)
    # 奇数页顺时针旋转90度
    if page_num % 2 != 0:
        current_page.rotateClockwise(90)
    # 偶数页逆时针旋转90度
    else:
        current_page.rotateCounterClockwise(90)
    writer.addPage(current_page)

# 添加空白页面,并且旋转90度
page = writer.addBlankPage()
page.rotateClockwise(90)
# 通过writer对象的write方法将将旋转后的pdf写入到新文件中
with open(r"C:\python07\day19\代码\XGBoost-旋转.pdf","wb") as file:
    writer.write(file)

