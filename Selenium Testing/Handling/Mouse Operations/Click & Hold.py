import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/clickHold?sublist=0")
driver.maximize_window()

circle = driver.find_element('id','circle')
ob = ActionChains(driver)
ob.click_and_hold(circle).pause(2).release(circle).perform()
time.sleep(2)