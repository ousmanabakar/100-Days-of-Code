import time

from selenium import webdriver

PASSWORD = ""
EMAIL = ""


chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%" \
      "2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0"

driver.get(URL)
time.sleep(10)
signInButton = driver.find_element_by_xpath('/html/body/div[1]/header/nav/div/a[2]')
signInButton.click()
time.sleep(15)
email = driver.find_element_by_xpath('//*[@id="username"]')
email.send_keys(EMAIL)
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys(PASSWORD)
time.sleep(10)

login = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
login.click()
time.sleep(20)
jobClicker = driver.find_element_by_xpath('//*[@id="main-content"]/section[2]/ul/li[2]/div/a')
jobClicker.click()
time.sleep(20)
applyButton = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div/section[2]/div/div[1]/div/div/button[1]')
applyButton.click()

# fillPhoneNumber = driver.find_element_by_xpath('//*[@id="urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2794178751,2348680586354666230,phoneNumber~nationalNumber)"]')
# fillPhoneNumber("12345678")
nextButton = driver.find_element_by_xpath('//*[@id="ember464"]/span')
nextButton.click()
reviewsButton = driver.find_element_by_xpath('//*[@id="ember467"]/span')
reviewsButton.click()
submitButton = driver.find_element_by_xpath('//*[@id="ember477"]')
submitButton.click()

time.sleep(100)
