import os
import winreg


def get_desktop():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return str(winreg.QueryValueEx(key, "Desktop")[0])  # 返回的是Unicode类型数据


def get_Temp(file='file'):
    deskdop = get_desktop()
    # 获取临时文件
    temp = os.path.join(deskdop, 'temp')
    # 判断文件是否存在
    if not os.path.exists(temp):
        os.mkdir(temp)
    temp = os.path.join(temp, file)
    if not os.path.exists(temp):
        os.mkdir(temp)


if __name__ == '__main__':
    # 就是获取当前目录，并组合成新目录
    getcwd = os.getcwd()
    print(getcwd)
    # 当前文件的名称
    print(os.path.basename(__file__))
    # 获取当前文件的绝对路径
    print(__file__)
    # 新建临时文件
    get_Temp('测试11')
