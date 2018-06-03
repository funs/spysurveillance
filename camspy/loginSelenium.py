#coding=utf-8
#test seleniym 登入

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


try:
    title = 'none'
    Browser = webdriver.Chrome("C:\selenium_driver_chrome\chromedriver.exe")
    LoginUrl= ('http://114.32.1.144/Login.htm')
    UserName= ('admin1')
    #UserPass= ('#####')

    Browser.get(LoginUrl)
    Browser.find_element_by_id('username').send_keys(UserName)
    #Browser.find_element_by_id('password').send_keys(UserPass)
    Browser.find_element_by_id('username').send_keys(Keys.ENTER)
    #Browser.save_screenshot('test.png')
    title = Browser.title
    print(title)
    Browser.quit()
except:
    print(title)
    Browser.quit()

