
import requests
import pandas as pd
from bs4 import BeautifulSoup

headers = {}
url = 'https://www.trendyol.com/sr?wc=103108&os=1&sk=1&sst=BEST_SELLER&pi=1'
response = requests.get(url, headers=headers)
html_request = response.content
soup = BeautifulSoup(html_request, "html.parser")

urun_name = soup.find_all("span", attrs={"class": "prdct-desc-cntnr-name hasRatings"})
urun_price = soup.find_all("div", attrs={"class": "price-promotion-container"})


liste =list()

try:
    for i in range(len(urun_name)):

        urun_name[i] = (urun_name[i].text).strip("\n").strip()
        urun_price[i] = (urun_price[i].text).strip("\n").strip()
        liste.append([urun_name[i], urun_price[i]])
        output = pd.DataFrame(liste, columns=["Names", "Prices"])
except :
    pass



print(output.to_string())
