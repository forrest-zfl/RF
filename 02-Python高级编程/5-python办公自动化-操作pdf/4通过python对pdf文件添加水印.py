import PyPDF2

# 读取原pdf文件
reader1 = PyPDF2.PdfFileReader(r"C:\python基础\28-python办公自动化-操作pdf\XGBoost.pdf")
# 读取水印文件
reader2 = PyPDF2.PdfFileReader(r"C:\python基础\28-python办公自动化-操作pdf\watermark.pdf")

# 创建写入pdf文件的对象
writer = PyPDF2.PdfFileWriter()

# 获取水印页
watermark_page = reader2.getPage(0)

for page_num in range(reader1.numPages):
    # 获取当前页对象
    current_page = reader1.getPage(page_num)
    # 将原文件的每一页和水印页合并
    current_page.mergePage(watermark_page)
    writer.addPage(current_page)

# 将添加完水印页的文件写入到新文件中去
with open("C:\python基础\28-python办公自动化-操作pdf\XGBoost-添加水印.pdf","wb") as file:
    writer.write(file)