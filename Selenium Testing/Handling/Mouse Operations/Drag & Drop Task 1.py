import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/dragDrop?sublist=0")
driver.maximize_window()
ob = ActionChains(driver)

ele = driver.find_element('xpath','//div[text()="Drag Me"]')
ob.drag_and_drop_by_offset(ele,200,0).pause(2).drag_and_drop_by_offset(ele,-200,0).perform()
ob.drag_and_drop_by_offset(ele,0,200).pause(2).drag_and_drop_by_offset(ele,0,-200).perform()
time.sleep(2)
