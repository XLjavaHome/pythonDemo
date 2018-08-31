def sayhi():
    # 单行注释不打印
    """
   用该函数打印Hi
    """
    print("Hi")
sayhi()
doc=sayhi.__doc__
# 有回车和换行
print(doc)