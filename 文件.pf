import requests
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)

# 一个是关于 SSL，也就是 https 证书的问题。如果碰到 HTTPS 证书无效导致无法访问的错误，可以尝试加参数 verify=False 忽略：
r = requests.get('https://www.12306.cn/', verify=False)
if r.text != "":
    print("不为空")
r = requests.get('https://www.12306.cn/')
if r.text != "":
    print("不为空")