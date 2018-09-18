# todo
# !/usr/bin/env python
# coding=utf-8
# 简单的验证登录以及登陆后获取想要的页面内容
import requests
from lxml import etree
# 这个是网站在登录的时候验证密码的界面，一般不是登录的界面，需要抓包获取到
headUrl = "http://sinitek2.3322.org:8126/"
post_url = "%sxwiki/bin/loginsubmit/XWiki/XWikiLogin" % headUrl
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

# 需要登录后才能访问的页面网址
url = (
    headUrl + "xwiki/bin/login/XWiki/XWikiLogin?srid=2ShyM6Se&xredirect=%2Fxwiki%2Fbin%2Fview%2FMain%2F%3Fsrid%3D2ShyM6Se")
item_list = session.post(url, headers=headers)
html = etree.HTML(item_list.text)
# //*[@id="document:xwiki:Blog.如何给Android手机刷机并安装Xposed框架.WebHome_anchor"]
Total_list = html.xpath('//a[@class="typePage type"]/@href')
for i in Total_list:
    body = session.post(headUrl + i, headers=headers)
    bodyEtree = etree.HTML(body.text)
    # bodyText = bodyEtree.xpath("//div[@class='main']/text()")
    # print(bodyText)
# 导航的url
headUrl = (
    headUrl + 'xwiki/bin/get/Main/WebHome?outputSyntax=plain&sheet=XWiki.DocumentTree&showAttachments=false&showTranslations=false&&data=children&id=document%3Axwiki%3AMain.WebHome')
headHtml = session.get(headUrl, headers=headers)
headerG = etree.HTML(headHtml.text)
print(headHtml.text)
