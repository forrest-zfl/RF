# 安装pillow 模块   pip install pillow
from PIL import Image
# 打开图片 open()
# 显示图片 show()

img_path = r"C:\python基础\27-python办公自动化-操作ppt\resources\11.jpg"
# 打开图片
img = Image.open(img_path)
# 显示图片
# img.show()

# 旋转和翻转图片
'''
rotate() 返回旋转后的新图像,原图片不变,逆时针旋转
save()  保存图片
'''
# img.rotate(45).save("./hehe.jpg")

# 调整图片的大小 resize((width+-数字,height+-数字))   参数:(width+-数字,height+-数字)

# size 表示的是大小
width,height = img.size
print(width,height)

resizeImg = img.resize((width+300,height+150))
resizeImg.save("./调整后的图片.jpg")



