# 输入
# from xml import etree
# 将文本转化为对象
import requests

# 实际登录页面

_data = {'j_username':'guest','j_password':'sinitek'}
login_url = 'http://sinitek2.3322.org:8126/xwiki/bin/loginsubmit/XWiki/XWikiLogin'
r = requests.post(login_url, data=_data)
print(r.cookies)
# # 具体
grade_url = 'http://sinitek2.3322.org:8126/xwiki/bin/view/Main/?srid=2ShyM6Se'
user_agent = r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
# headers = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
# # 使用session方法，可以在多次访问中保留cookie
requests_session = requests.session()
response1 = requests.get(url=grade_url, cookies=r.cookies)
# html1 = response1.text
# response2 = requests_session.get(url=grade_url)
html2 = response1.text
print(html2)