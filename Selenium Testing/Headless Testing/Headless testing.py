import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

ob = Options()
ob.add_argument("--headless")
driver = webdriver.Chrome(options=ob)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(2)

links = driver.find_elements('tag name','a')
print(len(links))
time.sleep(1)
