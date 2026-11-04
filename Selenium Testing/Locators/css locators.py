import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
#using css id
driver.find_element('css selector','#name').send_keys('adarsh')
#using css attribute
driver.find_element('css selector',"input[id='email']").send_keys('adarsh@gmail.com')
#using css class name and attribute
driver.find_element('css selector',"input.form-control[placeholder='Enter Phone']").send_keys('9964411115')
driver.find_element('css selector',"textarea.form-control[id='textarea']").send_keys('subash nagar')
#using css class name
driver.find_element('css selector',".form-check-input").click()
#using css attribute
driver.find_element('css selector',"input[id='tuesday']").click()
time.sleep(5)