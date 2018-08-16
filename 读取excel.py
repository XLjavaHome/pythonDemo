import xlrd

import util.文件
'''
 作者：徐立
 2018-08-15 11:35
'''
num = 1  # 任务
# 上周计划
lastTaskSet = set()
# 类型
lastbugSet = set()
# 本周计划
taskSet = set()
bugSet = set()
# 扫描的文件目录
downloads = "D:\Downloads"
for file in util.文件.get_excel(downloads):
    excelFile = xlrd.open_workbook(file)
    # print(file)
    # 获取第一个sheet，第一行是日志类型就进行。
    sheet = excelFile.sheet_by_index(0)
    maxrow = sheet.nrows
    # 根据第一行的第一个单元格是日志类型来判断
    row0 = sheet.row(0)
    cell0 = sheet.cell(0, 0)
    #  上周工作内容
    if (cell0.value == '日志类型'):
        for row in range(0, maxrow):
            # 第一列的内容
            cellType = sheet.cell(row, 0)
            if cellType.value == 'BUG修复':
                lastbugSet.add(sheet.cell(row, 5).value)
            elif cellType.value == '开发任务':
                lastTaskSet.add(sheet.cell(row, 5).value)
    # 本周工作计划
    if cell0.value == 'BUG编号':
        for row in range(0, maxrow):
            bugSet.add(sheet.cell(row, 1).value)
            # 本周工作计划
    if cell0.value == '任务名称':
        for row in range(0, maxrow):
            taskSet.add(sheet.cell(row, 0).value)

result = "上周工作内容：\n"
if lastTaskSet:
    result += "{0}.开发{1}任务。\n".format(*[num, '、'.join(lastTaskSet)])
    num = num + 1
if lastbugSet:
    result += "{0}.修复{1}的BUG。\n".format(*[num, '、'.join(lastbugSet)])
result += '本周工作计划：\n'
num = 1
if taskSet:
    result += "{0}.开发{1}任务。\n".format(*[num, '、'.join(taskSet)])
    num = num + 1
if bugSet:
    result += "{0}.修复{1}的BUG。\n".format(*[num, '、'.join(bugSet)])
print(result)
