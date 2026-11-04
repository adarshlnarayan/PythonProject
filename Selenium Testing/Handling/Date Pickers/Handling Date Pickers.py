import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(3)

driver.find_element('id', 'datepicker').click()
while True:
    month=driver.find_element('class name','ui-datepicker-month').text
    year=driver.find_element('class name','ui-datepicker-year').text
    if month=='September' and year=='2024':
        break
    else:
        driver.find_element('xpath','//a[@data-handler="prev"]').click()
        time.sleep(1)
driver.find_element('xpath',"//a[text()='6']").click()
time.sleep(2)

driver.find_element('id',"txtDate").click()
month=driver.find_element('class name','ui-datepicker-month')
m=Select(month)
m.select_by_visible_text('Sep')
year=driver.find_element('class name','ui-datepicker-year')
y=Select(year)
y.select_by_visible_text('2024')
driver.find_element('xpath','//a[text()="6"]').click()
time.sleep(2)
