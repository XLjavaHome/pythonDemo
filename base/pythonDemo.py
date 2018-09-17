from urllib.parse import urlencode
# 拼接URL后面的参数
params = {
    'offset': 1,
    'format': 'json',
    'keyword': '街拍',
    'autoload': 'true',
    'count': '20',
    'cur_tab': '1',
    'from': 'search_tab'
}
print(urlencode(params))
