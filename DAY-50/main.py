import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
PASSWORD = ""
EMAIL = ""

chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Get The URL
driver.get("http://www.tinder.com")
time.sleep(5)

# Click to accept
acceptCookies = driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[2]/div/div/div[1]/button/span')
acceptCookies.click()

# Click in Login button
time.sleep(5)
loginButton = driver.find_element_by_xpath(("//*[text()='Log in']"))
loginButton.click()

# choose Login with facebook option
time.sleep(5)
logInWithFacebook = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
logInWithFacebook.click()
time.sleep(5)

#Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Login and hit enter
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
email.send_keys(EMAIL)
password.send_keys("FB_PASSWORD")
password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)









