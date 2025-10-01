import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
books = []


num_pages = 5  

for page in range(1, num_pages + 1):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"  
    
    soup = BeautifulSoup(response.text, "html.parser")


    book_containers = soup.find_all("article", class_="product_pod")

    for book in book_containers:
        
        title = book.h3.a['title']

        
        price_raw = book.find("p", class_="price_color").text
        price = float(price_raw.replace("£", "").strip())

        
        rating = book.p['class'][1]  # e.g., "Three", "Five"

        
        availability = book.find("p", class_="instock availability").text.strip()

        books.append({
            "Title": title,
            "Price": "£"+str(price),
            "Rating": rating,
            "Availability": availability
        })
    
    time.sleep(1)  


df = pd.DataFrame(books)


df.to_csv("books.csv", index=False)
print("Scraping complete! CSV saved as books.csv")
