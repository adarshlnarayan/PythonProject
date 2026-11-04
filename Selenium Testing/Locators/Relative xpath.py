import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://practicetestautomation.com/practice-test-login/')
driver.maximize_window()
driver.find_element('id','username').send_keys('student')
driver.find_element('id','password').send_keys('Password123')
driver.find_element('xpath',"//button[text()='Submit']").click()
time.sleep(2)
driver.find_element('xpath',"//a[text()='Log out']").click()