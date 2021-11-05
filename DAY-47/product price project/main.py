import requests
from bs4 import BeautifulSoup
import lxml
import smtplib


URL = "https://www.amazon.com/Seagate-Portable-External-Hard-Drive/dp/B07CRG94G3/ref=lp_16225007011_1_4"
header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Accept-Language": "en-GB,en;q=0.9,tr-TR;q=0.8,tr;q=0.7,en-US;q=0.6,ar;q=0.5"
}
response = requests.get(URL, headers=header)
# web_page = response.text
soup = BeautifulSoup(response.content, "lxml")

# 4. Use BeautifulSoup to get hold of the price of the item and print it out.
price = soup.find(name="span", class_="a-size-medium a-color-price").getText()
price_as_float = float(price.split("$")[1])
print(price_as_float)

# 5. Get the title and link of the product
target_price = 1005
product_title = soup.find(name="span", class_="a-size-large product-title-word-break").getText().strip("\n")
print(product_title)
product_link = soup.find(name="link", rel="canonical").get("href")
print(product_link)

myemail = "your-e-mail@gmail.com"
mypassword = "Your paswrd"

if price_as_float < target_price:
    message = f"{product_title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(user=myemail, password=mypassword)
        connection.sendmail(
            from_addr=myemail,
            to_addrs="tosend-email@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode('utf-8')
        )

