try:
    import time
    from selenium import webdriver
    driver = webdriver.Chrome()
    driver.get('https://demoapps.qspiders.com/ui')
    driver.maximize_window()
    driver.implicitly_wait(10)

    driver.find_element('id','name').send_keys('admin')
    driver.find_element('id','emailid').send_keys('admin@gmail.com')
    time.sleep(1)
except:
    driver.save_screenshot('error.png')


