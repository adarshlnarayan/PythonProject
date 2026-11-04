import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)


#Simple alerts
# driver.find_element('id','alertBtn').click()
# time.sleep(2)
# simple = driver.switch_to.alert
# simple.accept()
# time.sleep(2)


#Confirmation alert
# driver.find_element('id','confirmBtn').click()
# time.sleep(2)
# con = driver.switch_to.alert
# # con.accept()
# # time.sleep(2)
# con.dismiss()
# time.sleep(2)


#Prompt alert
driver.find_element('id','promptBtn').click()
prom = driver.switch_to.alert
prom.send_keys("Adarsh")
time.sleep(2)
prom.accept()
time.sleep(2)