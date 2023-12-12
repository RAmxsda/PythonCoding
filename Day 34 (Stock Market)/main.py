import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMETER = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "HV7F700A355B809Z",
}

NEWS_PARAMETER = {"q": COMPANY_NAME, "apiKey": "0e0ee57a33364d60ada482bc9d6aadf7"}

response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMETER)
response.raise_for_status()
print(response)
data = response.json()["Time Series (Daily)"]
stock_data_price = [value for (key, value) in data.items()]
# print(stock_data_price)
yesterday_closing_price = stock_data_price[0]["4. close"]
before_yesterday_closing_price = stock_data_price[1]["4. close"]

difference_in_price = float(yesterday_closing_price) - float(
    before_yesterday_closing_price
)
up_down = None
if difference_in_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

change_stock_percentage = (difference_in_price / float(yesterday_closing_price)) * 100

if change_stock_percentage >= 1:
    news_response = requests.get(NEWS_ENDPOINT, params=NEWS_PARAMETER)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"]
    three_articles = articles[:3]
    formated_articles = [
        f"{STOCK}:{up_down} {change_stock_percentage} %\nHeadline: {article['title']} \nBrief:{article['description']}"
        for article in three_articles
    ]

    for news in formated_articles:
        print(news)


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.



