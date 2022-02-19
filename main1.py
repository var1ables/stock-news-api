import requests

ADVANTAGE_API = YOUR_API_KEY
NEWS_API = YOUR_API_KEY

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    'function': "TIME_SERIES_DAILY",
    'symbol': STOCK_NAME,
    'apikey': ADVANTAGE_API
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()

end_price = response.json()['Time Series (Daily)']
endprice_list = [value for (key, value) in end_price.items()]
yesterday = endprice_list[0]
yesterday_closing = yesterday['4. close']

day_before_yesterday = endprice_list[1]
day_before_closing = day_before_yesterday['4. close']

difference = abs(float(yesterday_closing) -float(day_before_closing))
percent = (difference / float(yesterday_closing)) * 100

news_params ={
    'apikey': NEWS_API,
    'qInTitle': COMPANY_NAME
}
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if percent > 1:
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles']
    three_articles = articles[:3]
    three_headlines = [f"Headline:{article['title']}. \n Brief: {article['description']}" for article in three_articles]
    for i in three_headlines:
        print(i)
