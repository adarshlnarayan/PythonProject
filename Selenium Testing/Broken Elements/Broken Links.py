import time
import requests
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

links = driver.find_elements('tag name','a')
url = []
for i in links:
    if i.get_attribute('href')!=None:
        url.append(i.get_attribute('href'))

for i in url:
    response = requests.get(i)
    if response.status_code>=400:
        print(f'{i} is broken link')
    else:
        print(f'{i} is not a broken link')
time.sleep(1)
