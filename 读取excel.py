import xlrd

import util.文件
for file in util.文件.get_excel("D:\Downloads"):
    excelFile = xlrd.open_workbook(file)
    sheet_names = excelFile.sheet_by_index(0)  # 获取excel中所有工作表名
    # 获取第一个sheet，第一行是日志类型就进行。
    # 如果是BUG修复就获取所对应的需求类型加入一个集合中
    # 如果是开发任务就加入到另一个值中
    print(sheet_names.cell(0))

# for i in sheet_names:
#     print(i);
# worksheet1 = workbook.sheet_by_index(0)
# print(worksheet1.name)
# sheet2 = worksheet.sheet_by_name('Sheet2')  # 根据Sheet名获取数据
#
# sheet2 = worksheet.sheet_by_index(1)  # 根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
#
# rows = sheet2.row_values(3)  # 表示获取Sheet2中第4行数据
#
# cols10 = sheet2.col_values(9)  # 表示获取Sheet2中第10列数据（数据保存为list）
