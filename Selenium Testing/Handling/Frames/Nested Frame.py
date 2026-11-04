import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://demoapps.qspiders.com/ui/frames/nested?sublist=1')
driver.maximize_window()

out = driver.find_element('xpath','//iframe[@class="w-full h-96"]')
driver.switch_to.frame(out)
inner = driver.find_element('xpath','//div[@class="form_container"]/iframe')
driver.switch_to.frame(inner)
driver.find_element('id','email').send_keys('Admin@gmail.com')
time.sleep(1)
driver.find_element('id','password').send_keys('Admin@1234')
time.sleep(1)
driver.find_element('id','confirm-password').send_keys('Admin@1234')
time.sleep(1)
driver.find_element('xpath','//button[@type="submit"]').click()
time.sleep(1)
