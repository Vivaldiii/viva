# -*- coding: utf-8 -*-
# @Time   :2021/7/17 19:04
# @Author :Kevin
# @File   :git_demo_01.py

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = WebDriver()
driver.get("https://www.cnblogs.com/yoyoketang/p/6123834.html")
driver.implicitly_wait(5)
driver.quit()