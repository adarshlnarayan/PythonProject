import time
import requests
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

images = driver.find_elements('tag name','img')
url = []
for i in images:
    if i.get_attribute('src')!=None:
        url.append(i.get_attribute('src'))

for i in url:
    response = requests.get(i)
    if response.status_code>=400:
        print(f'{i} is broken image')
    else:
        print(f'{i} is not a broken image')
time.sleep(1)