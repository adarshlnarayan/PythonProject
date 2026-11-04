import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.amazon.com/')
driver.maximize_window()
time.sleep(5)
driver.find_element('name',"search_query").send_keys('adarsh')
driver.find_element('css selector','value=Google Search').click()
time.sleep(5)