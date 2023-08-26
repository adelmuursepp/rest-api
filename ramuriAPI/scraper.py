import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.urbanoutfitters.com/shop/bdg-high-waisted-comfort-stretch-flare-jean?category=sale&color=003&type=REGULAR&quantity=1")

print(html)