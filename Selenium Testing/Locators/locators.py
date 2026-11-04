import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://practicetestautomation.com/practice-test-login/')
time.sleep(4)
driver.maximize_window()
driver.find_element('id','username').send_keys('student')
driver.find_element('name','password').send_keys('Password123')
driver.find_element('class name','btn').click()
images=driver.find_elements('tag name','img')
print('no of images in the link is',len(images))
#driver.find_element('link text','Practice Test Automation.').click()
driver.find_element('partial link text','Test').click()

time.sleep(1)