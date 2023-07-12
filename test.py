from bs4 import BeautifulSoup
import requests

url = "https://bookcourt.mu/14-books?page=5"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = soup.select(".thumbnail-container")

# for book in books:
#     mylist.append(book.select_one(".product-cat").getText())




# print(books[0].select_one(".h3").getText())

# print(book_list[1]["name"])


book_list = []


for book in books:
    book_list.append({"title": book.select_one(".h3").getText(),
                      "price": book.select_one(".price").getText(),
                      "category": book.select_one(".product-cat").getText(),
                      "author": book.select_one(".product-auth").getText()})


for i in book_list:
    if i["category"] == "Bestseller":
        print(i)

