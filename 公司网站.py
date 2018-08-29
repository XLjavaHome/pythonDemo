import ssl
import urllib.request

import chardet

weburl = "https://sirm.sinitek.com/first.jsp"
webheader = {
    'Accept': 'text/html, application/xhtml+xml, */*',
    # 'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'DNT': '1',
    'Connection': 'Keep-Alive',
    'Host': 'sirm.sinitek.com/first.jsp'
}

context = ssl._create_unverified_context()
weburl='https://www.baidu.com/'
req = urllib.request.Request(url=weburl, headers=webheader)
webPage = urllib.request.urlopen(req, context=context)
html = webPage.read()
charset = chardet.detect(html)
data = webPage.read().decode('utf-8')

print(data)
print(type(webPage))
print(webPage.geturl())
print(webPage.info())
print(webPage.getcode())
