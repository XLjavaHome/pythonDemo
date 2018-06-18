# 输入

import requests

url = "https://www.hao123.com/"
respson = requests.get(url)
s = vars(respson)
print(s)
dir(respson)
# print(respson.text)
