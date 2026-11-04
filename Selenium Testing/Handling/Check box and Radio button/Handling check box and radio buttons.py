import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

#count radio buttons
radio = driver.find_elements('xpath', "//input[@type='radio']")
print("radio button count is ", len(radio))

#to click radio:
for i in radio:
    i.click()
time.sleep(2)

#count check box
check_box = driver.find_elements('xpath', "//input[@type='checkbox']")
print("check box count is ", len(check_box))

#to select only days check box
days = driver.find_elements('xpath', "//input[@type='checkbox' and @value]")

#to check all box:
for i in days:
    i.click()
    time.sleep(2)

#to check in reverse:
for i in days[::-1]:
    i.click()
    time.sleep(2)

#check specific days
for i in days:
    if i.get_attribute('id') in ['sunday', 'wednesday', 'saturday']:
        i.click()
        time.sleep(2)
