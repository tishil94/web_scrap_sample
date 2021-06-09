import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get("https://www.flipkart.com/search?q=laptop%20ideapad%20300&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
soup = BeautifulSoup(r.content, 'html.parser')

products=[] #List to store name of the product
prices=[] #List to store price of the product
ratings=[] #List to store rating of the prod
data = soup.find_all('a')

one_a_tag = soup.findAll('a', href=True)

text = soup.get_text()

for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
    name=a.find('div', attrs={'class':'_4rR01T'})
    price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
    rating=a.find('div', attrs={'class':'_3LWZlK'})
    products.append(name.text)
    prices.append(price.get_text())
    ratings.append(rating.text if rating else "not rated") 
df = pd.DataFrame({'Price':prices,'Rating':ratings,'Product Name':products}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
