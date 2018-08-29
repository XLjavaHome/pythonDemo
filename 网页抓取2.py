# 输入
# from xml import etree
# 正则
import re

import chardet
import requests

url = "https://www.baidu.com/"
# url = "http://www.jingcaiyuedu.com/book/368416.html"
respson = requests.get(url)
respson = requests.urlopen(url)
# 知道编码
charset = chardet.detect(respson.read)
respson.encoding=charset
# 正则
title=re.findall(r'<meta property="og:type" content="(.*?)"/>', respson.text)
print(title)