import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://demoapps.qspiders.com/ui/scroll/newTabHorizontal")
driver.maximize_window()
time.sleep(5)


#scroll horizontal end and back
driver.execute_script('window.scrollBy(document.body.scrollWidth,0)')
time.sleep(2)
driver.execute_script('window.scrollBy(-document.body.scrollwidth,0)')
time.sleep(2)


#based on axis value
driver.execute_script("window.scrollBy(1000,0)")
time.sleep(2)
driver.execute_script("window.scrollBy(-1000,0)")
time.sleep(2)


#to get x-axis value
driver.execute_script('window.scrollBy(document.body.scrollWidth,0)')
time.sleep(2)
x_axis = driver.execute_script('return window.pageXOffset;')
print(x_axis)


# # based on element for x-axis
# ele = driver.find_element('id','taskTable')
# driver.execute_script("argument[0].scrollIntoView({behaviour:'smooth',block:'center',inline:'center'});",ele)
# time.sleep(2)
