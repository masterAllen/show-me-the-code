# !/usr/bin/python3
from PIL import Image
from pathlib import Path, PosixPath
import os

def get_img_list(source):
    srcpath = Path(source)
    imgname_list = list(srcpath.glob('*.jpg'))
    return imgname_list

def resize_img(img_list, des, height, width):
    Path(des).mkdir(parents=True, exist_ok=True)
    dirpath = Path(des)

    for imgname in img_list:
        img = Image.open(imgname)
        if max(img.size)>height:
            scale = max(img.size)/width
            #调整大小
            new_maxsize = height
            new_minsize = min(img.size)/scale
            #修改大小               
            newimg = img.resize((int(new_maxsize),int(new_minsize)),Image.ANTIALIAS)
        else:
            newimg = img

        filename = str(imgname.name)
        newimg.save(dirpath.joinpath('new_'+filename))

if __name__ == '__main__':
    PHONE = {'iPhone5':(1136,640), 'iPhone6':(1134,750), 'iPhone6P':(2208,1242)}
    img_list = get_img_list('./source')
    height, width = PHONE['iPhone6']
    resize_img(img_list, './newimg', height, width)
