# 输入
# from xml import etree
import requests
from lxml import etree

url = "https://www.hao123.com/"
respson = requests.get(url)
print(respson.text)


def donnload():
    html = requests.get("http://www.pearvideo.com/").text
    html = etree.HTML(html)
    print(html)


donnload()
