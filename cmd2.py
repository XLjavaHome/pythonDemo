import datetime
import os
# todo 解决乱码

nowTime = datetime.datetime.now().strftime('%Y%m%d')  # 现在
fileName = r"d:\1\sirmpm{0}.dmp".format(nowTime)
cmd = "exp sirmpm/sirmpm@172.16.2.16:1521/orcl file={0} owner=sirmpm".format(fileName)
cmd = "dir"
print(cmd)
print(os.popen(cmd).read())

# 导入
cmd = "imp sirmpm/sirmpm@orcl file={0} full=y".format(fileName)
