import tkinter.filedialog
from tkinter import *

import 读取excel
root = Tk()
def xz():
    # filename = tkinter.filedialog.askopenfilename()
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        result = 读取excel.get_week(filename)
        lb.delete('1.0', 'end')
        lb.insert(1.0, result)
    else:
        lb.config(text="您没有选择任何文件");
# lb = Label(root, text='')
lb = Text(root, height=10)
lb.pack()
root.title("上周内容、本周计划")
btn = Button(root, text="请选择excel所在目录", command=xz)
btn.pack()
root.mainloop()
