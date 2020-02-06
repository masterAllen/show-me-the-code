import urllib.request
import re
import chardet
from pathlib import Path, PosixPath

# 重要参考
# https://blog.csdn.net/sunon_/article/details/90634253
# https://blog.csdn.net/xiaowanggedege/article/details/8650034
 
# 打开网页--->读取网页源代码
page = urllib.request.urlopen('http://tieba.baidu.com/p/2166231880')
htmlCode = page.read().decode('utf-8')

# 打印网页源代码
# print(htmlCode.decode('utf-8'))

# 正则表达式查找，记得要事先查看网页结构，保证正确性
# re.compile --> 要和其他函数配合使用(find_all, search)
reg = r'src="(.*?\.jpg)" bdwater='
imgre = re.compile(reg)
imglist = re.findall(imgre, htmlCode)

Path('./img').mkdir(parents=True, exist_ok=True)

i = 0
for imgurl in imglist:
    urllib.request.urlretrieve(imgurl, 'img/%s.jpg'%i)
    i+=1
