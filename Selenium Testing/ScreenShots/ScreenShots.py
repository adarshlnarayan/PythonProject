import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://demoapps.qspiders.com/ui')
driver.maximize_window()
driver.implicitly_wait(10)

#to save in current working directory
driver.save_screenshot('demo.png')

#to save in particular file
driver.save_screenshot(r'C:\Users\adars\OneDrive\Pictures\Screenshots\demo.png')

#for particular element
name = driver.find_element('id','name')
login = driver.find_element('xpath','//a[@href="/ui/login"]')
name.screenshot('name.png')
login.screenshot('login.png')

time.sleep(2)