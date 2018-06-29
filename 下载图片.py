import os

import requests
def downloadPath1():
    # 项目的路径
    projectPath = os.getcwd();
    downloadPath = projectPath + "\\下载"
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
# 下载一张图片
path = '下载\\image.png'

downloadPath1()
r = requests.get("https://www.baidu.com/img/bd_logo1.png")
# 相比open来说，with有一个优点就是不用close(),其写入后自动关闭。
with open(path, 'wb') as f:
    f.write(r.content)
