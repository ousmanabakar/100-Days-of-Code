import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

google_form_url = "your google form urm"
web_site_url = "https://www.apartments.com/houses/boston-ma/1-bedrooms/?bb=6oxmh1_5qHimhylhE"
header = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 '
                  'Safari/537.36',
    'Accept-Language': "en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6,ar;q=0.5"
}
response = requests.get(web_site_url, headers=header)
zillow_web_page = response.text

soup = BeautifulSoup(zillow_web_page, "html.parser")
links = soup.select("article > section > div > div.property-info > div > div.property-title-wrapper > a")
new_href = []
for i in links:
    href = i["href"]
    new_href.append(href)
list_of_all_links = new_href[2:]

# All the prices
all_prices = soup.select("div.price-range")
all_prices_list = []
for i in all_prices:
    all_prices_list.append(i.text)


# Get the addresses
all_addresses = soup.select("article > section > div > div.property-info > div > div > a > div.property-address.js-url")
list_of_addresses = []
for i in all_addresses:
    list_of_addresses.append(i.text)

CHROME_DRIVER_PATH = "Your chromedriver path"
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for n in range(len(list_of_all_links)):
    driver.get(google_form_url)
    time.sleep(2)
    address = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(list_of_addresses[n])
    time.sleep(1)
    price.send_keys(all_prices_list[n])
    time.sleep(1)
    link.send_keys(list_of_all_links[n])
    time.sleep(1)
    submit_button.click()
