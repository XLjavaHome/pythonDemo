import requests
url = 'http://httpbin.org/post'
cookies = dict(some_cookie='working')
headers = {'user-agent': 'chrome'}
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080',
}
data = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(
    url,
    data=data,
    cookies=cookies,
    proxies=proxies,
    headers=headers
)
print(r.text)
