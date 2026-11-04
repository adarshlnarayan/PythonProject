import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()


driver.find_element('xpath','//button[text()="New Tab"]').click()
time.sleep(2)
tab = driver.window_handles
print(tab)
driver.switch_to.window(tab[1])
time.sleep(2)

driver.find_element('xpath','//input[@type="text"]').send_keys('adarsh')
time.sleep(2)
driver.close()

driver.switch_to.window(tab[0])
time.sleep(2)
driver.close()
