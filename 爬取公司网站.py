import time

from selenium import webdriver

driver = webdriver.Firefox()
# driver.get("http://www.hao123.com")
driver.get("https://sirm.sinitek.com/first.jsp")
msg=driver.page_source
print(msg)
# driver.find_element_by_id("search-input").send_keys("测试111")
# driver.find_element_by_class_name("button-hook").click()

# 界面的html
# msg = driver.page_source
# print(msg)
# cookies = driver.get_cookies()
# print(cookies)
# 设置图片的大小
# driver.set_window_size(1920, 1080)
# 截图
time.sleep(5)
# 退出
# driver.quit()
