import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/mouseHover/tab?sublist=3")
driver.maximize_window()

men = driver.find_element('xpath','//li[@class="Men p-4 relative"]')
t_wear = driver.find_element('xpath','''//span[text()="Men's Top wear"]''')
t_shirt = driver.find_element('xpath','''//span[text()="Men's T-Shirts"]''')
disc = driver.find_element('xpath','//section[@class="Men_List_2"]/ul/li[2]')

ob = ActionChains(driver)
ob.move_to_element(men).move_to_element(t_wear).move_to_element(t_shirt).move_to_element(disc).click().perform()
time.sleep(2)