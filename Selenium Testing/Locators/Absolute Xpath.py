import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")
driver.maximize_window()
time.sleep(20)
driver.find_element('xpath',"/html/body/ytd-app/div/div[2]/ytd-masthead/div[4]/div[2]/yt-searchbox/div[1]/div/div/form/input").send_keys("tabahii")
time.sleep(2)