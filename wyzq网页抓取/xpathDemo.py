# 输入
# from xml import etree
import requests
# 将文本转化为对象
from lxml import etree

url = "https://www.hao123.com/"
respson = requests.get(url)
def donnload():
    # html = requests.get("http://www.pearvideo.com/").text
    html = requests.get("http://www.pearvideo.com/shooters").text
    # etree 将html转化为对象
    html = etree.HTML(html)
    return html
html = donnload()
a=html.xpath('//*[@id="categoryList"]/li/div/a')
# //*[@id="categoryList"]/li[1]/div/a/div[2]
html.xpath('//*[@id="categoryList"]/div/a/div[@class=vervideo-title]')
print(a)