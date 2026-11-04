import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(2)

rows=driver.find_elements("xpath",'//table[@name="BookTable"]/tbody/tr')
columns=driver.find_elements('xpath', '//table[@name="BookTable"]/tbody/tr/th')

for r in range(2,len(rows)+1):
    out=[]
    for c in range(1,len(columns)+1):
        data=driver.find_element("xpath",f'//table[@name="BookTable"]/tbody/tr[{r}]/td[{c}]').text
        out.append(data)
    #print(out)

    #to print book name with respect to author
    #print(out[:2:])

    #to print books which cost more than 1000
    if int(out[3])>1000:
        print(out[:1:])

    #to print books of author Mukesh
    #if 'Mukesh' in out:
    #    print(out)
