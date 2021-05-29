import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
news_api = "32df706db9f74597baba418eae771b48"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameter = {
    "apikey": STOCK_NAME,
    "function": "TIME_SERIES_DAILY",
    "outputsize": "compact",
    "symbol": STOCK_NAME,
}
stockResponse = requests.get(url=STOCK_ENDPOINT, params=parameter)
stockData = stockResponse.json()["Time Series (Daily)"]
ClosingPrice = [value for (key, value) in stockData.items()]
day1 = ClosingPrice[0]["4. close"]
day2 = ClosingPrice[1]["4. close"]

differenceBetween2days = abs(float(day1) - float(day2))
print(differenceBetween2days)

difference_Percentage = (differenceBetween2days / float(day1)) * 100
print(difference_Percentage)

if difference_Percentage > 0:
    newsParams = {
        "q": COMPANY_NAME,
        "apiKey": news_api,
        "sortBy": "top-headlines",

    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=newsParams)
    newsData = response.json()["articles"]

    three_articles = newsData[0:3]


    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    print(formatted_articles)