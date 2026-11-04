import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
ob = ActionChains(driver)

#drag and drop based on element
ele = driver.find_element('id','draggable')
target = driver.find_element('id','droppable')
ob.drag_and_drop(ele,target).perform()
time.sleep(2)

#drag and drop based on axis / sliders
pointer = driver.find_element('xpath','//div[@id="slider-range"]/span[2]')
ob.drag_and_drop_by_offset(pointer,40,0).perform()
time.sleep(2)
