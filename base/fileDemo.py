# 当前路径
import os
# 文件可以加r
path = r'%s\filedemo.txt' % os.getcwd()
print(path)
# encoding解决写入文件中文乱码
with open(path, 'w', encoding='utf8') as f:
    # f.write(unicode("测试",'tuf-8)'))
    f.write("测试")
