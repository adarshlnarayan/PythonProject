import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element('xpath','//li[text()="Disabled"]').click()
time.sleep(2)

name = driver.find_element('id','name')
email = driver.find_element('id','email')
password = driver.find_element('id','password')

driver.execute_script("arguments[0].removeAttribute('disabled');", name)
driver.execute_script("arguments[0].removeAttribute('disabled');", email)
driver.execute_script("arguments[0].removeAttribute('disabled');", password)

name.send_keys("adarsh")
email.send_keys("adarsh@gmail.com")
password.send_keys("Admin@123")
time.sleep(2)
