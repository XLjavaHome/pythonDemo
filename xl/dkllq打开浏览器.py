import webbrowser

import requests
url = "https://www.baidu.com"
get = requests.get(url)
print(get.text)
webbrowser.open(url)
