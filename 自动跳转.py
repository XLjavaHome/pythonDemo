import requests
# 不跳转
r = requests.get('http://github.com/', allow_redirects=False)
print(r.status_code)
print(r.text)
# 跳转
r = requests.get('http://github.com/')
print(r.status_code)
print(r.text)
