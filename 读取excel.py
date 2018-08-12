import xlrd
workbook = xlrd.open_workbook('resouces/武汉员工_20180705.xlsx')  # 打开excel文件

sheet_names = workbook.sheet_names()  # 获取excel中所有工作表名
for i in sheet_names:
    print(i);
worksheet1=workbook.sheet_by_index(0)
print(worksheet1.name)
# sheet2 = worksheet.sheet_by_name('Sheet2')  # 根据Sheet名获取数据
#
# sheet2 = worksheet.sheet_by_index(1)  # 根据索引获取数据，索引为0开始，1表示获取第二张工作表数据
#
# rows = sheet2.row_values(3)  # 表示获取Sheet2中第4行数据
#
# cols10 = sheet2.col_values(9)  # 表示获取Sheet2中第10列数据（数据保存为list）
