import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://demoapps.qspiders.com/ui/frames/nestedWithMultiple?sublist=3')
driver.maximize_window()

main = driver.find_element('xpath','//iframe[@class="w-full h-96"]')
driver.switch_to.frame(main)

inner = driver.find_element('xpath','//section[@class="main_form_container"]/div[2]/iframe')
driver.switch_to.frame(inner)

email=driver.find_element('xpath','//div[@class="form-group"][1]/iframe')
driver.switch_to.frame(email)
driver.find_element('id','email').send_keys('Admin@gmail.com')
time.sleep(1)
driver.switch_to.parent_frame()

password = driver.find_element('xpath','//div[@class="form-group"][2]/iframe')
driver.switch_to.frame(password)
driver.find_element('id','password').send_keys('Admin@1234')
time.sleep(1)
driver.switch_to.parent_frame()

confirm = driver.find_element('xpath','//div[@class="form-group"][3]/iframe')
driver.switch_to.frame(confirm)
driver.find_element('id','confirm').send_keys('Admin@1234')
time.sleep(1)
driver.switch_to.parent_frame()

sub = driver.find_element('xpath','//div[@class="form-group"][4]/iframe')
driver.switch_to.frame(sub)
driver.find_element('id','submitButton').click()
time.sleep(5)