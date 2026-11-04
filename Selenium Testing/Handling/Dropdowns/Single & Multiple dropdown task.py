import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui/dropdown?sublist=0")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element('id','phone').send_keys('9988776655')
driver.find_element('id','male').click()

country=driver.find_element('xpath','//select[@id="select3"]')
c=Select(country)
c.select_by_visible_text('India')
time.sleep(1)

state=driver.find_element('xpath','//select[@id="select5"]')
s=Select(state)
s.select_by_visible_text('Karnataka')
time.sleep(1)

city=driver.find_element('xpath','//option[@id="optionCity"]/..')
ci=Select(city)
ci.select_by_visible_text('Bangalore Rural')
time.sleep(1)

driver.find_element('xpath','//a[text()="Multi Select"]').click()
time.sleep(5)

cart=driver.find_element('xpath','//select[@id="select-multiple-native"]')
l=Select(cart)
l.select_by_visible_text('Mens Casual Premium ...')
l.select_by_visible_text('Mens Cotton Jacket...')
l.select_by_visible_text('Mens Casual Slim Fit...')

driver.find_element('xpath','//button[text()="Add"]').click()
time.sleep(3)