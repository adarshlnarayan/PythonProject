import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.msense.ai/")
driver.implicitly_wait(10)
driver.maximize_window()

links = driver.find_elements("tag name", "a")
videos = driver.find_elements("tag name","video")
images = driver.find_elements("tag name","img")
time.sleep(2)

print(len(links))
print(len(videos))
print(len(images))