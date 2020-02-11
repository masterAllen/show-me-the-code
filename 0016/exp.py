import  json
from collections import  OrderedDict
import xlwt

with open('source/numbers.txt',encoding='utf-8') as f:
    numbers_list = json.load(f,object_pairs_hook=OrderedDict)
    print(numbers_list)

wb = xlwt.Workbook()  
ws = wb.add_sheet('numbers') 

for i in range( len(numbers_list) ):
    for j in range( len(numbers_list[i]) ):
        ws.write(i,j,numbers_list[i][j])

wb.save('numbers.xls')
