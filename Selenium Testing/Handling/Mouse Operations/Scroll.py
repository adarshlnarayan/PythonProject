import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
mouse = ActionChains(driver)

#based on axis
mouse.scroll_by_amount(0,1000).perform()
time.sleep(2)
mouse.scroll_by_amount(0,-1000).perform()
time.sleep(2)

#based on element
ele = driver.find_element('id','taskTable')
mouse.scroll_to_element(ele).perform()
time.sleep(2)
