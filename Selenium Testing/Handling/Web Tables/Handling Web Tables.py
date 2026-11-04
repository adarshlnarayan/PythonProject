import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

rows=driver.find_elements("xpath",'//table[@name="BookTable"]/tbody/tr')
columns=driver.find_elements('xpath', '//table[@name="BookTable"]/tbody/tr/th')

for r in range(2,len(rows)+1):
    for c in range(1,len(columns)+1):
        data=driver.find_element("xpath",f'//table[@name="BookTable"]/tbody/tr[{r}]/td[{c}]').text
        print(data,end=' ')
    print()
time.sleep(2)