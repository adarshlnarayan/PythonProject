import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

drop=driver.find_element('xpath','//select[@id="animals"]')
ob=Select(drop)
animals=ob.options
print(len(animals))
for i in animals:
    print(i.text)
    time.sleep(2)

ob.select_by_visible_text("Deer")
ob.select_by_visible_text("Elephant")
ob.select_by_visible_text("Giraffe")

s=ob.all_selected_options
for i in s:
    print(i.text)
time.sleep(2)