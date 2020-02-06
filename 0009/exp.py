# !/usr/bin/python3
from bs4 import BeautifulSoup


# https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/

# 注意后面有个read
html_handle = open('sample.html','r',encoding='utf-8').read()

soup = BeautifulSoup(html_handle,'html.parser')

#输出标题
# print(soup.title)
#输出p标签的内容
# print(soup.p)
#输出a链接
print(soup.a)
#输出body标签的内容也就是正文
# print(soup.find_all('body'))
#输出整个html文件
# print(soup.get_text)
