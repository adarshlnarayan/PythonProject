import time
import openpyxl
import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(r"https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(2)

path = r"C:\Api DDT\selenium ddt.xlsx"
rows = Utilities.get_row(path,"Sheet1")
for r in range(1,rows+1):
    un = Utilities.read_data(path,"Sheet1",r,2)
    pwd = Utilities.read_data(path,"Sheet1",r,3)
    driver.find_element("id","username").send_keys(un)
    time.sleep(1)
    driver.find_element("id","password").send_keys(pwd)
    time.sleep(1)
    driver.find_element("id","submit").click()
    time.sleep(1)
    if driver.current_url == "https://practicetestautomation.com/logged-in-successfully/":
        print('passed')
        Utilities.write_data(path,"Sheet1",r,5,"pass")
        driver.find_element("xpath","//a[text()='Log out']").click()
        time.sleep(1)
    else:
        print('failed')
        Utilities.write_data(path, "Sheet1", r, 5, "fail")
        time.sleep(1)
time.sleep(2)
