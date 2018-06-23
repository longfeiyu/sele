#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait  #导入包
from selenium.webdriver.support import expected_conditions as EC  #导入包
from selenium.webdriver.common.by import By  #导入包

browser=webdriver.Chrome()  #打开浏览器
browser.get(r"C:\Users\zhazha\Desktop\alter.html")  #地址
browser.implicitly_wait(15)  #隐式等待
browser.find_element_by_xpath("//*[@value='显示输入提示框']").click()
browser.switch_to_alert().send_keys("po[o[o[o")







