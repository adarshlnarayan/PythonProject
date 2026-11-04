import time
from selenium import webdriver
from selenium.webdriver import ActionChains,Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
ob = ActionChains(driver)

driver.find_element('id','name').send_keys('adarsh')
time.sleep(2)

#select text
ob.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(2)

#copy text
ob.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(2)

#next line
ob.key_down(Keys.TAB).perform()
time.sleep(2)

#paste
ob.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(2)

#delete
ob.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
ob.key_down(Keys.BACKSPACE).perform()

#scroll down and up
ob.key_down(Keys.PAGE_DOWN).perform()
time.sleep(2)
ob.key_down(Keys.PAGE_UP).perform()
time.sleep(2)

#scroll for 5 times down and up
for i in range(1,6):
    ob.key_down(Keys.PAGE_DOWN).perform()
    time.sleep(1)


for i in range(1,6):
    ob.key_down(Keys.PAGE_UP).perform()
    time.sleep(1)

time.sleep(2)
