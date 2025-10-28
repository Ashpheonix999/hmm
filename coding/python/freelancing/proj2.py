import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

# Set headers to pretend like you're a normal browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Example Amazon search URL (laptops US marketplace)

url = "https://www.amazon.com/s?k=laptops&crid=1DZ0BO6HOGCKY&sprefix=lapto%2Caps%2C729&ref=nb_sb_noss_2"


response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Lists to store data
titles, prices, ratings, reviews, links = [], [], [], [], []

# Loop through product containers
for item in soup.select("div.s-main-slot div[data-component-type='s-search-result']")[:10]:
    # Title
    title = item.h2.text.strip() if item.h2 else "N/A"
    titles.append(title)

    # Product Link
    link = "https://www.amazon.com" + item.h2.a["href"] if item.h2 and item.h2.a else "N/A"
    links.append(link)

    # Price
    whole_price = item.select_one("span.a-price-whole")
    frac_price = item.select_one("span.a-price-fraction")
    if whole_price:
        price = whole_price.text.strip() + (frac_price.text.strip() if frac_price else "")
    else:
        price = "N/A"
    prices.append(price)

    # Rating
    rating = item.select_one("span.a-icon-alt")
    ratings.append(rating.text.strip() if rating else "N/A")

    # Reviews
    review_count = item.select_one("span.a-size-base.s-underline-text")
    reviews.append(review_count.text.strip() if review_count else "N/A")

    # Be nice to Amazon servers
    time.sleep(random.uniform(1, 2))

# Save to DataFrame
df = pd.DataFrame({
    "Title": titles,
    "Price": prices,
    "Rating": ratings,
    "Reviews": reviews,
    "Link": links
})

# Save to CSV/Excel
df.to_csv("amazon_laptops_demo.csv", index=False)
df.to_excel("amazon_laptops_demo.xlsx", index=False)

print("✅ Scraping done! Data saved to amazon_laptops_demo.csv and amazon_laptops_demo.xlsx")
