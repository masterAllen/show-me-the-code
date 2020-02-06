import  json
from collections import  OrderedDict
import xlwt

with open('source/students.txt',encoding='utf-8') as f:
    students_dict = json.load(f,object_pairs_hook=OrderedDict)
    print(students_dict)

# 1. Python 与excel文件打交道
# 创建一个工作簿
wb = xlwt.Workbook()  
# 创建一个sheet
ws = wb.add_sheet('student') 

row = 0
for k,v in students_dict.items():
    ws.write(row,0,k)
    col = 1
    for item in v:
        ws.write(row,col,item)
        col += 1
    row +=1
wb.save('student.xls')  #保存
