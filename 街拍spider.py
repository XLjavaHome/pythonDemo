import os
from hashlib import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import requests
GROUP_START = 1
GROUP_END = 5
def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',
        'from': 'gallery',
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None
def get_images(json):
    data = json.get('data')
    if data:
        for item in data:
            # print(item)
            image_list = item.get('image_list')
            title = item.get('title')
            # print(image_list)
            if image_list:
                for image in image_list:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }
def save_image(item):
    directroyPath = "d:/街拍"
    if (not os.path.exists(directroyPath)):
        os.mkdir(directroyPath)
    itemPath = directroyPath + "/" + item.get('title')
    # if not os.path.exists(itemPath):
    #     os.mkdir(itemPath)
    try:
        local_image_url = item.get('image')
        new_image_url = local_image_url.replace('list', 'large')
        response = requests.get('http:' + new_image_url)
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            # 文件直接放在该目录下
            file_path = '{0}.{1}'.format(md5(response.content).hexdigest(), 'jpg')
            if os.path.exists(directroyPath):
                with open(directroyPath + "/" + file_path, 'wb')as f:
                    f.write(response.content)
            else:
                print('Already Downloaded', file_path)
    except requests.ConnectionError:
        print('Failed to save image')
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)
# 当前文件是主函数时
if __name__ == '__main__':
    # 有些情况下，所要完成的工作可以分解并独立地分布到多个工作进程，对于这种简单的情况，可以用Pool类来管理固定数目的工作进程。作业的返回值会收集并作为一个列表返回。（以下程序cpu数量为2，相关函数解释见python
    # 进程池2 - Pool相关函数）
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    # 将func应用于迭代中的每个元素，在返回的列表中收集结果。
    pool.map(main, groups)
    pool.close()
    pool.join()
