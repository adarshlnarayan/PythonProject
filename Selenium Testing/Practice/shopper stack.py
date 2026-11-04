import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.shoppersstack.com/")
driver.maximize_window()
time.sleep(50)
driver.find_element('xpath',"/html/body/div[1]/section/article/div[2]/button").click()
time.sleep(5)
driver.find_element('xpath', "//input[@id='Email']").send_keys("adarsh@gmail.com")
time.sleep(2)
driver.find_element('xpath', "//input[@name='Password']").send_keys("adarsh")
time.sleep(2)