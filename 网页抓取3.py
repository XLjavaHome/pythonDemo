# 输入
# from xml import etree
import requests
# 将文本转化为对象
url = "http://sinitek2.3322.org:8126/xwiki/bin/view/Main/?srid=2ShyM6Se"
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
cookie_str = r'JSESSIONID=E152207987360DBCBE4A3AB8C033773B; username="nvtCeiOx73A_"; password="D1MjkURCfzw_"; rememberme="false"; validation="f81f38f06872daa7fe7943b967cc8004"'
cookies = {}
for line in cookie_str.split(';'):
    key, value = line.split('=', 1)
    cookies[key] = value
respson = requests.get(url, headers=header, cookies=cookies)
print(respson.text)
