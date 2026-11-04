import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://practicetestautomation.com/practice-test-login/')
driver.maximize_window()
driver.implicitly_wait(5)

#to count links
links = driver.find_elements('tag name', 'a')
print('count is', len(links))

#to print the text from link
for i in links:
    print(i.text)

    #to click a particular link
    if i.text == 'Practice Test Automation.':
        i.click()
        time.sleep(2)
        break
