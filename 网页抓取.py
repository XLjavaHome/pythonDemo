# 输入
# from xml import etree
import requests
from lxml import etree

url = "https://www.hao123.com/"
respson = requests.get(url)
# respson.
# print(respson.text)
# 查看对象的属性 dir
def donnload():
    html = requests.get("http://www.pearvideo.com/").text
    html = etree.HTML(html)
    return html
html = donnload()
