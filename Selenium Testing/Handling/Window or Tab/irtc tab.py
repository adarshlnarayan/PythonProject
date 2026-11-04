import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()

driver.find_element('xpath','//button[text()="English"]').click()
driver.find_element('xpath','//span[@class="railDrishti fa fa-bus"]').click()
time.sleep(2)
tab = driver.window_handles
driver.switch_to.window(tab[1])

driver.find_element('xpath','//div[@class="Nav-icons Flights"]').click()
time.sleep(2)
tab = driver.window_handles
driver.switch_to.window(tab[-1])

driver.find_element('xpath','//div[@class="Nav-icons IRCTCHotels"]').click()
time.sleep(2)
tab = driver.window_handles
driver.switch_to.window(tab[-1])

driver.find_element('xpath','//button[@tabindex="6"]').click()
time.sleep(5)
