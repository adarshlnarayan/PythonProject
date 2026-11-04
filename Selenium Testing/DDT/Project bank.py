import time
import Utilities
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.sbisecurities.in/calculators/home-loan-calculator")
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(5)

la = driver.find_element("id","input_loan_amount")
roi = driver.find_element("id","input_interest")
tenure = driver.find_element("id","tenure")
calc = driver.find_element("xpath","//button[@type='submit']")

def remove_char(a):
    b=''
    for i in a:
        if '0'<=i<='9':
            b+=i
    return int(b)

path = r"C:\Api DDT\selenium ddt.xlsx"
rows = Utilities.get_row(path,"Sheet2")

for r in range(2,rows+1):
    amount = Utilities.read_data(path,"Sheet2",r,1)
    interest = Utilities.read_data(path,"Sheet2",r,2)
    years = Utilities.read_data(path,"Sheet2",r,3)

    la.clear()
    la.send_keys(amount)
    time.sleep(1)

    roi.clear()
    roi.send_keys(interest)
    time.sleep(1)

    tenure.clear()
    tenure.send_keys(years)
    time.sleep(1)

    calc.click()
    time.sleep(1)

    emi = driver.find_element("xpath","//span[@style='color:green; ']")
    Utilities.write_data(path,"Sheet2",r,5,remove_char(emi.text))
    time.sleep(1)
time.sleep(2)