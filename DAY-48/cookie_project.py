from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
cookie = driver.find_element_by_id("cookie")

timeout = time.time() + 5
five_min = time.time() + 60*5

while True:
    cookie.click()
    time.sleep(2)




