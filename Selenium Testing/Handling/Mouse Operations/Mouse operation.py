import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#right click
text = driver.find_element('id','name')
ob = ActionChains(driver)
ob.context_click(text).perform()
time.sleep(2)

#double click
text.send_keys("Adarsh")
ob.double_click(text).perform()
time.sleep(2)


#mouse hover
point = driver.find_element('xpath','//button[text()="Point Me"]')
laptop = driver.find_element('xpath','//a[text()="Laptops"]')
ob.move_to_element(point).move_to_element(laptop).perform()
time.sleep(2)

