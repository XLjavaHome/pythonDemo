from urllib.parse import urlencode

import os

params = {
    'tn': 'resultjson_com',
    'ipn': 'rj',
    'ct': '201326592',
    'is': '',
    'fp': 'result',
    'queryWord': '街拍',
    'cl': '2',
    'lm': '-1',
    'ie': 'utf-8',
    'oe': 'utf-8',
    'adpicid': '',
    'st': '-1',
    'z': '',
    'ic': '0',
    'word': '街拍',
    's': '',
    'se': '',
    'tab': '',
    'width': '',
    'height': '',
    'face': '0',
    'istype': '2',
    'qc': '',
    'nc': '1',
    'fr': '',
    'pn': 3,
    'rn': '30',
    'gsm': '1e',
    '1527421468357': '',
}
str = urlencode(params)
print(str)
path = os.path.join("./baidu_pic")
print(path)
# 就是获取当前目录，并组合成新目录
getcwd = os.getcwd()
print(getcwd)
ospath=os.path.join(getcwd, 'data')
print(ospath)
