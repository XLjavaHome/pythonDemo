import winreg
def get_desktop():
      key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                           r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')  # 利用系统的链表
      return str(winreg.QueryValueEx(key, "Desktop")[0])  # 返回的是Unicode类型数据
if __name__ == '__main__':
      Desktop_path = get_desktop()  # Unicode转化为str
      print(Desktop_path)
