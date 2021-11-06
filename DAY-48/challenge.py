from selenium import webdriver
from selenium.webdriver.common.keys import Keys
chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# URL = "https://en.wikipedia.org/wiki/Main_Page"
# driver.get(URL)
# article_count = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
# # article_count = driver.find_element_by_css_selector('#articlecount a')
# # print(article_count.text)
# # article_count.click()
#
# All_portals = driver.find_element_by_link_text("All portals")
# # All_portals.click()
#
# # search = driver.find_element_by_name("search")
# # search.send_keys("python")
# # search.send_keys(Keys.ENTER)

URL = "http://secure-retreat-92358.herokuapp.com/"
firstName = driver.find_element_by_name('fName')
firstName.send_keys("ousman")

lastName = driver.find_element_by_css_selector("form lName")
lastName.send_keys("aba")

email = driver.find_element_by_css_selector("email")
email.send_keys("ousman@gmail.com")

submit = driver.find_element_by_css_selector("form button")
submit.click()
submit.send_keys(Keys.ENTER)
