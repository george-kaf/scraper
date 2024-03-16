from bs4 import BeautifulSoup
import requests
import re

def scraperino(url):
    website = str(url)
    html = requests.get(website)

    s = BeautifulSoup(html.content, 'html.parser')
    description = s.body.findAll('div', {'class': 'rte'})

    print(description)

scraperino('https://punkcake.rocks/collections/cakes/products/triple-hazelnut-cake')