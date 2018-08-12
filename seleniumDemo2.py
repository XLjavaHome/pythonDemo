from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import util.文件

# 无界面浏览器
chrome = Options()
chrome.add_argument("--headless")
chrome.add_argument("--disable-gpu")
driver = webdriver.Firefox(chrome_option=chrome)
driver.get("http://www.hao123.com")
driver.set_window_size(600,800)
tempfile = util.文件.get_tempfile("百度.png")
driver.save_screenshot(tempfile)
