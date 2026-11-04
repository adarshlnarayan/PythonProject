import time
from selenium import webdriver
driver = webdriver.Chrome()

#username= admin
#password= admin


driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")
driver.maximize_window()
time.sleep(2)