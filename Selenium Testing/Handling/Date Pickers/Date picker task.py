import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui/datePick?sublist=0")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element('xpath','//input[@type="text"]').click()
while True:
    month=driver.find_element('xpath','//div[@class="react-datepicker__current-month"]').text
    if month=='September 2025':
        break
    else:
        driver.find_element('xpath','//button[@aria-label="Previous Month"]').click()

driver.find_element('xpath','//div[text()="6"]').click()

time.sleep(2)