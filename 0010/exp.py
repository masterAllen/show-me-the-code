import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter

# 很大部分参考： https://blog.csdn.net/shifanfashi/article/details/89422324

# 之前担心一个问题，背景颜色随机，字母随机，那么会不会字母和背景相容
# 不会这样，因为字母画上去就是整个字母，比如4这个数字，它的每个像素点都是一样颜色

def get_char():
    base = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return random.choice(base)

def generator_font_color():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 背景颜色
def generator_bgcolor():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def imag_produce():
    w = 260
    h = 120

    # 生产新图片
    img = Image.new('RGB',(w,h),(255,255,255))

    font = ImageFont.truetype('source/YaHei.Consolas.1.12.ttf',60)
    draw = ImageDraw.Draw(img)

    # 画背景，每个点的颜色随机
    for i in range(w):   
        for j in range(h):
            draw.point((i,j),fill=generator_bgcolor())

    # 画四个字母，每个字母颜色随机
    for i in range(4):  
        draw.text((i*60+10,10),get_char(),font=font,fill=generator_font_color())

    # 模糊处理
    img = img.filter(ImageFilter.BLUR)
    img.show()

if __name__ == '__main__':
    imag_produce()
