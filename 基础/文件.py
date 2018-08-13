import os

from util import 文件
for root, dirs, files in os.walk(文件.get_Temp()):
    print(root)  # 当前目录路径
    print(dirs)  # 当前路径下所有子目录
    print(files)  # 当前路径下所有非目录子文件
