import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=2")
driver.maximize_window()
ob = ActionChains(driver)

lcharger = driver.find_element('xpath','//div[text()="Laptop Charger"]')
mcover = driver.find_element('xpath','//div[text()="Mobile Cover"]')
lcover = driver.find_element('xpath','//div[text()="Laptop Cover"]')
mcharger = driver.find_element('xpath','//div[text()="Mobile Charger"]')

mobile = driver.find_element('xpath','//div[@class="columns flex gap-6"]/section[2]/div[1]')
laptop = driver.find_element('xpath','//div[@class="columns flex gap-6"]/section[2]/div[2]')

ob.drag_and_drop(lcharger,laptop).perform()
ob.drag_and_drop(mcover,mobile).perform()
ob.drag_and_drop(lcover,laptop).perform()
ob.drag_and_drop(mcharger,mobile).perform()
time.sleep(2)
