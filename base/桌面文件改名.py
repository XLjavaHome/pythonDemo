import os

from util import file
from util import regex
from util import 拼音
if __name__ == '__main__':
    deskdop = file.get_desktop()
    # deskdop = r'C:\Users\Administrator\Desktop\1'
    # 文件的全路径
    filePaths = file.list_file(deskdop)
    for filePath in filePaths:
        # 第一个文件名不为字符的话，改为字母加上当前文件名
        # 文件名
        file = os.path.basename(filePath)
        if not regex.isLetters(file[0]):
            initia = 拼音.getPinyin(file[0])
            try:
                os.rename(filePath, os.path.join(os.path.dirname(filePath), initia + file))
            except:
                print(filePath + "改名失败，该文件可能被占用")
                pass
    os.startfile(deskdop)
    print("改名结束")
