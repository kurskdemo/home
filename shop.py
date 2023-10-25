from bs4 import BeautifulSoup

with open("/home/ddmitriev/py/test.html") as file:
          src = file.read()
#print(src)

soup = BeautifulSoup(src, "lxml")
        
#title = soup.title
#print(title)
#print(title.string)
#print(title.text)

# page_h1 = soup.find("h1")

# print(page_h1.text)
# page_h2 = soup.find_all("product-card__link j-card-link j-open-full-product-card")

# for item in page_h1:
#         print(item.text)

        
# card_name = soup.find_all("p", class_="product-card__tip product-card__tip--sale")
# print(card_name)

# for item in card_name:
#         print(item.text)

# card_name = soup.find_all("div", class_="product-card__wrapper")
url = soup.find_all("a", class_="product-card__link j-card-link j-open-full-product-card")
# url = url.get("href")
print(url)
# card_name = soup.find("a")
# card_name2 = soup.find("a", class_="simple-menu__link j-wba-header-item")

sale = soup.find_all("a", class_="product-card__link j-card-link j-open-full-product-card")
sale = soup.find_all("p", class_="product-card__tip product-card__tip--sale")

# for item in url:
#         print(item)

for item in sale:
        print(item.text)

#test
