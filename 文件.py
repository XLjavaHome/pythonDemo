import os

# 就是获取当前目录，并组合成新目录
getcwd = os.getcwd()
print(getcwd)
ospath = os.path.join(getcwd, 'xl.txt')
print(ospath)
# 当前文件的名称
print(os.path.basename(__file__))
# 获取当前文件的绝对路径
print(__file__)
# 打包后__file__是不存在的。这时候用os.path.realpath(sys.argv[0])
f = open(ospath, 'a')
# 当前目录
print(os.path.join("./baidu_pic"))
# 返回文件的当前位置，即文件指针当前位置。
print(f.tell())
print(f.read())

# f.write("这是写入的数据")
f.close()
