import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

#without using select class

dropdowns=driver.find_elements('xpath','//select[@id="country"]')
for i in dropdowns:
    if i.text == 'Brazil':
        i.click()
time.sleep(5)


#with using Select class

#drop=driver.find_element('xpath','//select[@id="country"]')
#ob=Select(drop)

#ob.select_by_visible_text("Canada")
#time.sleep(2)
#or
#ob.select_by_index(4)
#time.sleep(2)
#or
#ob.select_by_value("france")
time.sleep(2)