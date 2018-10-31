'''
1.抓取公司wiki网站
2.登录获取cookies
3.抓取所有网友
4.存储mySql中
'''

import requests
url = "http://sinitek2.3322.org:8126/xwiki/bin/loginsubmit/XWiki/XWikiLogin"
postData = {'j_username': 'guest', 'j_password': 'sinitek'}
# 构造 Request headers
agent = 'Mozilla/5.0 (Windows NT 5.1; rv:33.0) Gecko/20100101 Firefox/33.0'
headers = {
    'User-Agent': agent
}
if __name__ == '__main__':
    session = requests.session()
    login = session.post(url, data=postData, headers=headers)
    res = requests.get(url)
    print(res.text)
    session = requests.session()
    cookies = requests.utils.dict_from_cookiejar(res.cookies)
    print(cookies)
