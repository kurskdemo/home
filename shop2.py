import requests
from bs4 import BeautifulSoup

url = "https://www.wildberries.ru/catalog/elektronika"


headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

}
req = requests.get(url, headers=headers)
src = req.text
print(src)
