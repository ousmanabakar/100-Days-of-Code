from selenium import webdriver

chrome_driver_path = "/home/ousman/Development/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# URL = "https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/ref=lp_16225007011_1_4"
# driver.get(URL)
# # price = driver.find_element_by_id("price_inside_buybox")
# # print(price.text)
URL = "https://www.python.org/"
driver.get(URL)
event_times = driver.find_elements_by_css_selector('.event-widget time')
event_titles = driver.find_elements_by_css_selector('.event-widget li a')
events = {}
for i in range(5):
    events[i] = {
        "time": event_times[i].text,
        "name": event_titles[i].text
    }

print(events)

driver.quit()
#driver.close()









