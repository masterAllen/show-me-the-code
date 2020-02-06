from PIL import Image,ImageDraw,ImageFont

# 图片--->图片对象
avatar = Image.open("source/avatar.jpg")
# 图片对象--->绘图对象
draw = ImageDraw.Draw(avatar)

# 读取信息
width, height = avatar.size
# 确立字体样式，颜色
myfont = ImageFont.truetype('source/YaHei.Consolas.1.12.ttf', size=100)
fillcolor = "#ff0000"
# 写入文字
draw.text((width-200, 0), '99+', font=myfont, fill=fillcolor)

# 显示图片对象
avatar.show()
