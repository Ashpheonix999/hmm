import requests
from bs4 import BeautifulSoup

url = "https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Get the 'Current Weather' card
weather_card = soup.find("a", class_="cur-con-weather-card")

if weather_card:
    # Temperature
    temp = weather_card.find("div", class_="temp")
    real_feel = weather_card.find("div", class_="real-feel")
    condition = weather_card.find("span", class_="phrase")

    # Details container (RealFeel Shade, Wind, etc.)
    details = weather_card.find_all("div", class_="spaced-content detail")
    extras = {}
    for detail in details:
        label = detail.find("span", class_="label").text.strip()
        value = detail.find("span", class_="value").text.strip()
        extras[label] = value

    # Print everything
    print("Current Temperature:", temp.text.strip())
    print("RealFeel:", real_feel.text.strip())
    print("Condition:", condition.text.strip())
    print()

    for k, v in extras.items():
        print(f"{k}: {v}")
else:
    print("Weather card not found.")

print("END")

