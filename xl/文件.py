import os
import winreg


def get_desktop():
    """桌面路径"""
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
    return str(winreg.QueryValueEx(key, "Desktop")[0])  # 返回的是Unicode类型数据


def get_tempfile(fileName=''):
    """获取临时目录文件"""
    path = os.path.join(get_desktop(), "temp")
    if not os.path.exists(path):
        os.makedirs(path)
    if (fileName):
        path = os.path.join(path, fileName)
    return path;


if __name__ == '__main__':
    Desktop_path = get_desktop()  # Unicode转化为str
    print(Desktop_path)
    file_object = open('test.txt')
