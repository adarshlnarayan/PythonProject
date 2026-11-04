import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.redbus.in/")
driver.maximize_window()
time.sleep(2)

driver.find_element('xpath','//*[@id="srcinput"]').send_keys('benga')
time.sleep(2)
driver.find_element('xpath','//div[text()="Majestic"]').click()
time.sleep(2)


driver.find_element('id','destinput').send_keys('mant')
time.sleep(2)
driver.find_element('xpath','//div[text()="Mantralayam"]').click()
time.sleep(2)

#driver.find_element('xpath','//button[@aria-label="Search for Today"]').click()


driver.find_element('xpath','//div[@aria-label="Select date of journey"]').click()
while True:
    month= driver.find_element('xpath','//p[@aria-live="polite"]').text
    if month=='September 2026':
        break
    else:
        driver.find_element('xpath','//i[@class="icon icon-arrow arrow___8b9155 right___d93b9b "]').click()
        time.sleep(2)
driver.find_element('xpath','//span[text()="6"]').click()
time.sleep(2)