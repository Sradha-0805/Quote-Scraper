from bs4 import BeautifulSoup
import requests
source = requests.get('https://www.goodreads.com/quotes').text
soup = BeautifulSoup(source, 'lxml')
for obj in soup.find_all('div', class_ = 'quoteDetails'):
    quote = obj.div.text
    print(quote)
