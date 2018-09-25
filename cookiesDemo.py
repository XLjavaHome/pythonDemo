# todo
# !/usr/bin/env python
# coding=utf-8
# 简单的验证登录以及登陆后获取想要的页面内容
import requests
from lxml import etree
# 这个是网站在登录的时候验证密码的界面，一般不是登录的界面，需要抓包获取到
headUrl = "http://sinitek2.3322.org:8126"
post_url = "%s/xwiki/bin/loginsubmit/XWiki/XWikiLogin" % headUrl
username = 'guest'
password = 'sinitek'
session = requests.session()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Referer": post_url,
           "X-Requested-With": "XMLHttpRequest"
           }
# 表单数据
data = {
    "j_username": username,
    "j_password": password
}

try:
    login_page = session.post(post_url, data=data, headers=headers)
    if "loginerror" in login_page.text:
        print("登录失败，错误的手机号码或密码！")
    if '导航' in login_page.text:
        print("欢迎您'%s'，成功登陆POS管理系统！" % username)
except Exception as e:
    print(e)
def openUrl(url):
    item_list = session.post(url, headers=headers)
    html = etree.HTML(item_list.text)
    return html
openUrl(
    'http://sinitek2.3322.org:8126/xwiki/bin/view/Main/%E8%AE%A1%E6%80%BB%E5%8A%9E/CSRF%E5%8A%9F%E8%83%BD%E5%A2%9E%E5%BC%BA/')
# 需要登录后才能访问的页面网址
# html = openUrl('http://sinitek2.3322.org:8126/xwiki/bin/view/Main/?srid=TK0mripx')
# Total_list = html.xpath('//a[@class="typePage type"]')
# for i in Total_list:
#     href属性,内容
# ahref = headUrl + i.attrib.get('href')
# print("%s:%s" % (i.text, ahref))
# ahtml = openUrl(ahref)
# bodyText= ahtml.xpath('//*[@id="body"]')
    # print(bodyText)