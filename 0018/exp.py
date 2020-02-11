import xlrd
import json
import xml.dom.minidom as xdm

def read_xls(file_name):
    # 1. Python 读取(excel/xls)文件
    xls_file = xlrd.open_workbook(file_name)
    xls_sheet = xls_file.sheet_by_name('city')
    data = {}
    for i in range(xls_sheet.nrows):
        data[xls_sheet.row_values(i)[0]] = xls_sheet.row_values(i)[1]

    return json.dumps(data, ensure_ascii=False)

# 3. Python 存储为(XML)文件
def save_to_xml(data, comment, new_file_name):
    # 新建xml文档对象
    xml = xdm.Document()
    # 创建根节点，student节点
    root = xml.createElement('root')
    child = xml.createElement('city')
    # 先加入root节点，在root节点下加入student节点
    xml.appendChild(root)
    root.appendChild(child)
    # 在student节点下添加注释
    comment = xml.createComment(comment)
    child.appendChild(comment)
    # 在student节点下写入文字内容
    content = xml.createTextNode(data)
    child.appendChild(content)
    # 写入文件，其中双引号会被转义为&quot，所以要replace
    with open(new_file_name, 'w+') as f:
        # f.write(data)
        f.write(xml.toprettyxml().replace('&quot;', '"'))


content = read_xls('source/city.xls')
comment = '城市信息'
save_to_xml(content, comment, 'city.xml')

