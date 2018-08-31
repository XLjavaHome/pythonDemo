import os

from util import file
for root, dirs, files in os.walk(file.get_Temp()):
    print(root)  # 当前目录路径
    print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件
title = '文件'
# 没有回创建，当前目录
filePath = '%s.txt' % title
# file = open(filePath, 'w', encoding='utf-8')
# file.write("这是写入的文件！！")
# file.close()
with open(filePath,'wb') as file:
    # 这必须要数组
    file.write(bytes('测试', encoding = "utf8")
)
