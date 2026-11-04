import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


#scroll to the bottom and top
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(2)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(2)


#based on axis value
driver.execute_script("window.scrollBy(0,1000)")
time.sleep(2)


#to get value of y-axis
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
y_axis = driver.execute_script("return window.pageYOffset;")
print(y_axis)


#based on element for y-axis
ele = driver.find_element('id','taskTable')
driver.execute_script("arguments[0].scrollIntoView();",ele)
time.sleep(2)
