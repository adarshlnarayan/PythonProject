import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
time.sleep(2)

rows=driver.find_elements('xpath','//table[@id="taskTable"]/tbody/tr')
columns=driver.find_elements('xpath','//tr[@id="headers"]/th')

for r in range(1,len(rows)+1):
    out=[]
    for c in range(1,len(columns)+1):
        data=driver.find_element('xpath',f'//tbody[@id="rows"]/tr[{r}]/td[{c}]').text
        out.append(data)
    if "Chrome" in out:
        ch=[i for i in out if ('/' not in i and 'MB' in i) or 'C' in i]
        print(ch)
time.sleep(2)