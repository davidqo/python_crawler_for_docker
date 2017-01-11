#import requests

#url = 'http://www.bash.im/'

#result = requests.get(url)

#with open('test.html', 'w') as output_file:
#  output_file.write(result.text.encode('utf-8'))

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()
driver.get("http://192.168.23.74:8081/index.html")
#assert "Python" in driver.title
elem = driver.find_element_by_id("user")
elem.clear()
elem.send_keys("3")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("number")
elem.clear()
elem.send_keys("103")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("domain")
elem.clear()
elem.send_keys("test.domain")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("url")
elem.clear()
elem.send_keys("192.168.23.80:8086")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("pass")
elem.clear()
elem.send_keys("1234")
elem.send_keys(Keys.RETURN)
elem = driver.find_element_by_id("button_sign")
elem.send_keys(Keys.RETURN)
time.sleep(5)
#elem = driver.find_element_by_id("call_number")
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "call_number")))
elem.clear()
elem.send_keys("102")
elem.send_keys(Keys.RETURN)
elem = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "reject")))
time.sleep(5)
driver.execute_script("document.getElementById('reject').click()")
time.sleep(3)
driver.execute_script("document.getElementById('logout').click()")
assert "No results found." not in driver.page_source
driver.close()
