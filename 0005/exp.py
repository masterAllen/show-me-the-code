# !/usr/bin/python3
from PIL import Image
from pathlib import Path, PosixPath
import os

# https://docs.python.org/3/library/pathlib.html
# 2. 获取某个文件夹，获取某个文件夹下文件
# 路径-->路径对象
srcpath = Path('source')
# 获取图片名字列表
imgname_list = list(srcpath.glob('*'))
# imgname_list = list(srcpath.glob('*.jpg'))

# 1. 创建文件夹，如果不存在，就创建
Path('newimg').mkdir(parents=True, exist_ok=True)
dirpath = Path('newimg')

# Iphone5 : 1136*640
# 按比例缩放即可
# 3. 调整图片大小
for imgname in imgname_list:
    img = Image.open(imgname)
    if max(img.size)>1136:
        scale = max(img.size)/1136.0
        #调整大小
        new_maxsize = 1136
        new_minsize = min(img.size)/scale
        #修改大小               
        newimg = img.resize((int(new_maxsize),int(new_minsize)),Image.ANTIALIAS)
    else:
        newimg = img

    # 5. 获取文件的前缀，后缀
    # dirpath = imgname.parent
    # dirpath.ttt
    # 返回的是PurePath，要转为string
    filename = str(imgname.name)

    # 4. 储存图片
    newimg.save(dirpath.joinpath('new_'+filename))
