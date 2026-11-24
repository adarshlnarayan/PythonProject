import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.msense.ai/")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)


home_page = driver.find_elements("tag name", "a")
url=[]
for i in home_page:
    url.append(i.get_attribute("href"))


driver.find_element('xpath','//a[text()="Products"]').click()
time.sleep(2)
prod_page = driver.find_elements('tag name','a')
for i in prod_page:
    if i.get_attribute("href") not in url:
        url.append(i.get_attribute("href"))


driver.find_element('xpath','//a[text()="Blogs"]').click()
time.sleep(2)
blog = driver.find_elements("tag name","a")
for i in blog:
    if i.get_attribute("href") not in url:
        url.append(i.get_attribute("href"))

print(len(url))
print(url)