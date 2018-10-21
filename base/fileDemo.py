# 当前路径
import os
# 文件可以加r
path = r'%s\filedemo.txt' % os.getcwd()
print(path)
# encoding解决写入文件中文乱码
# 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入
# with open(path, 'a', encoding='utf8') as f:
# 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件
with open(path, 'w', encoding='utf8') as f:
    # f.write(unicode("测试",'tuf-8)'))
    f.write("测试")
