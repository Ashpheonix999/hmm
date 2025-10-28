import requests
from bs4 import BeautifulSoup
from selenium import webdriver

"""

url = "http://quotes.toscrape.com"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

quotes = soup.find_all("div", class_="quote")


with open("quotes.txt", "w", encoding="utf-8") as f:
    for quote in quotes:
        text = quote.find("span", class_="text").text.strip()
        author = quote.find("small", class_="author").text.strip()
        f.write(f"'{text}' - {author}\n")

"""

print("END")
