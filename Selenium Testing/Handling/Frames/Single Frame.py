import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://demoapps.qspiders.com/ui/frames?sublist=0')
driver.maximize_window()

single = driver.find_element('xpath','//iframe[@class="w-full h-96"]')
driver.switch_to.frame(single)
driver.find_element('id','username').send_keys('admin')
time.sleep(5)