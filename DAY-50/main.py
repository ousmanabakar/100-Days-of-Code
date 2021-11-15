import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

PASSWORD = "ur password"
EMAIL = "ur email"

chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Get The URL
driver.get("https://www.tinder.com")
time.sleep(5)

# Click to accept cookies
acceptCookies = driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[2]/div/div/div[1]/button/span')
acceptCookies.click()

# Click in Login button
time.sleep(5)
loginButton = driver.find_element_by_xpath("//*[text()='Log in']")
loginButton.click()

# choose Login with facebook option
time.sleep(5)
logInWithFacebook = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div[1]/div/div[3]/span/div[2]/button')
logInWithFacebook.click()
time.sleep(5)

# Switch to Facebook login window
time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email = driver.find_element_by_xpath('//*[@id="email"]')
password = driver.find_element_by_xpath('//*[@id="pass"]')
time.sleep(5)
email.send_keys(EMAIL)
password.send_keys(PASSWORD)
time.sleep(5)
password.send_keys(Keys.ENTER)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
#
time.sleep(10)
location_button = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div/div/div[3]/button[1]')
location_button.click()
time.sleep(5)
not_interested = driver.find_element_by_xpath('//*[@id="u1408193709"]/div/div/div/div/div[3]/button[2]/span')
not_interested.click()
time.sleep(15)
# acceptCookies = driver.find_element_by_xpath('//*[@id="u1186853273"]/div/div[2]/div/div/div[1]/button')
# time.sleep(10)
# acceptCookies.click()


for _ in range(10):
    try:
        time.sleep(10)
        print("called")
        like_button = driver.find_element_by_xpath(
            '//*[@id="u1186853273"]/div/div[1]/div/div/main/div/div[1]/div[1]/div/div[5]/div/div[4]/button/span/span')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element_by_css_selector(".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(10)
