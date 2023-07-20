# 安装 PyPDF2 三方库用于读取pdf文件中的文本
# pip install PyPDF2

import PyPDF2
# 读取pdf文件
reader = PyPDF2.PdfFileReader(r"C:\python基础\28-python办公自动化-操作pdf\test.pdf")
# print(reader)
# 获取指定的页码文本
page = reader.getPage(0)
# 输出当前页码的文本
print(page.extractText())
