from bs4 import BeautifulSoup
import requests

url = "https://www.binance.com/en/markets/overview"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

coins = soup.select(".css-hwo5f4")

for coin in coins:
    print(coin.select_one(".css-ovtrou").getText())

