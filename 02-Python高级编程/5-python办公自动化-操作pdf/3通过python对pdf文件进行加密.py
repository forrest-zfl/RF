import PyPDF2
# 创建读取pdf文件的对象
reader = PyPDF2.PdfFileReader(r"C:\python基础\28-python办公自动化-操作pdf\XGBoost.pdf")
# 创建写入pdf文件的对象
writer = PyPDF2.PdfFileWriter()

for page_num in range(reader.numPages):
    # 将原文件的每一页追加到writer对象中去
    writer.addPage(reader.getPage(page_num))

# 给writer对象设置密码
writer.encrypt("123456")
# 创建文件,将加密后的内容写入到新文件中去
with open("C:\python07\day19\代码\XGBoost-加密.pdf","wb") as file:
    writer.write(file)
