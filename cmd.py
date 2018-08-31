import datetime
import os
# todo 解决乱码
userName = 'sirmpm'
password = 'sirmpm'
owner = 'sirmpm'
nowTime = datetime.datetime.now().strftime('%Y%m%d')  # 现在
fileName = r"d:\数据备份\sirmpm{0}.dmp".format(nowTime)
# cmd = "exp {0}/{1}@172.16.2.16:1521/orcl file={2} owner={3}".format(userName, password, fileName, owner)
# print(cmd)
# print(os.popen(cmd).read())
# print('备份结束')
# 导入
cmd = "imp {0}/{1}@orcl file={2} full=y".format(userName, password, fileName)
print(os.popen(cmd).read())
# @echo off
# date /t
