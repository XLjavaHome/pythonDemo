import time

from selenium import webdriver

import xl.文件


def screenshot():
    # 截图,两个一起用会报错
    tempfile = xl.文件.get_tempfile("百度.png")
    driver.save_screenshot(tempfile)
    # tempfile = xl.文件.get_tempfile("百度.jpg")
    # driver.save_screenshot(tempfile)


driver = webdriver.Firefox()
# driver.get("http://www.hao123.com")
driver.get("http://www.baidu.com")

# driver.find_element_by_id("search-input").send_keys("测试111")
# driver.find_element_by_class_name("button-hook").click()
time.sleep(3)

driver.get("http://www.hao123.com")

# 界面的html
# msg = driver.page_source
# print(msg)
# cookies = driver.get_cookies()
# print(cookies)
# 设置图片的大小
# driver.set_window_size(1920, 1080)
# 截图
screenshot()
time.sleep(5)
# 退出
driver.quit()
