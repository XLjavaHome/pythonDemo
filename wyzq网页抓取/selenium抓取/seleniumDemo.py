import time

from selenium import webdriver

import util.file
def baidu():
    driver.get("https://www.baidu.com")
    # 必须要下对应的浏览器版本
    driver.find_element_by_id("kw").send_keys("hello 世界")
    driver.find_element_by_id("su").click()
    # driver.find_element_by_id("search-input").send_keys("测试111")
    # driver.find_element_by_class_name("button-hook").click()
def screenshot(driver):
    # 截图,两个一起用会报错
    tempfile = util.file.get_tempfile("百度.png")
    driver.save_screenshot(tempfile)
    # tempfile = xl.文件.get_tempfile("百度.jpg")
    # driver.save_screenshot(tempfile)
def 公司网站():
    driver.get("https://sirm.sinitek.com/first.jsp")
    # Sinitek@pm1
    time.sleep(10)
    driver.find_element_by_id("J_username").send_keys("song.chen")
    driver.find_element_by_id("J_password").send_keys("123")
    time.sleep(2)
    driver.find_element_by_id("loginBtn").click()
    # 不加会报错
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="J_common_sec_aside_nav"]/ul/li[10]/ul/li[3]/a')
    driver.page_source
    # driver.get('http://localhost:8383/sirmpm/requirement/addrequirement.jsp?type=1')
    # driver.find_element_by_id('name').send_keys("这是需求名称")
    # driver.switch_to_frame(driver.find_element_by_xpath('//*[@id="J_common_panel_section"]/iframe[4]'))
    # driver.find_element_by_xpath('//*[@id="UUID8b1746df373a40f782c89ced9ee5156c"]/span').click()
    # driver.get("http://www.hao123.com")
driver = webdriver.Firefox()

# baidu()
公司网站()

# 界面的html
# msg = driver.page_source
# print(msg)
# okies = driver.get_cookies()
# print(cookies)
# 设置图片的大小
# driver.set_window_size(1920, 1080)
# 截图
# screenshot(driver)
def exsit():
    time.sleep(5)
    driver.quit()
# 退出
