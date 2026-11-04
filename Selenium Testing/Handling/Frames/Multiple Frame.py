import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://demoapps.qspiders.com/ui/frames/multiple?sublist=2')
driver.maximize_window()

f1 = driver.find_element('xpath','//iframe[@class="w-full h-96"]')
driver.switch_to.frame(f1)
driver.find_element('id','email').send_keys('Admin@gmail.com')
driver.find_element('id','password').send_keys('Admin@1234')
driver.find_element('id',"confirm-password").send_keys('Admin@1234')
driver.find_element('id','submitButton').click()
time.sleep(5)

driver.switch_to.default_content()

f2 = driver.find_element('xpath','//div[@class="px-8 pt-8 rounded-xl "]/section/div[2]/iframe')
driver.switch_to.frame(f2)
driver.find_element('id','username').send_keys('SuperAdmin@gmail.com')
driver.find_element('id','password').send_keys('SuperAdmin@1234')
driver.find_element('id','submitButton').click()
time.sleep(5)