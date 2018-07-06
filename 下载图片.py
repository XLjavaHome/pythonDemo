import os

import requests

import 桌面路径
def downloadPath():
    # 项目的路径
    projectPath = 桌面路径.get_desktop();
    downloadPath = projectPath + "\\下载"
    if not os.path.exists(downloadPath):
        os.mkdir(downloadPath)
    return downloadPath;
    # 下载一张图片
path = downloadPath() + "\\logon.png"
r = requests.get("https://www.baidu.com/img/bd_logo1.png")
# 相比open来说，with有一个优点就是不用close(),其写入后自动关闭。
with open(path, 'wb') as f:
    f.write(r.content)
print("图片下载完成")
