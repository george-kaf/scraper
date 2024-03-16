from bs4 import BeautifulSoup
import requests
import re


def product_scraperino(url):
    try:
        html = requests.get(url)

        s = BeautifulSoup(html.content, 'html.parser')

        #Get title from product page
        title_html = s.body.findAll('h1', {'class': 'h2 product-single__title'})
        title = re.findall('">[a-zA-Z]+.+.?', str(title_html))[0].split('">')[1].capitalize()
        
        #Get allergen info from description and filter the allergens
        allergen_html = s.body.findAll('div', {'class': 'rte'})
        allergens = re.findall('Allergens:.[a-zA-Z]+.+.?', str(allergen_html))[0].split("Allergens:")
        allergens = allergens[1].split("</span>")[0].capitalize()

        print(title + " - " + allergens)
    
    except:
        print("Oops...")


product_scraperino('https://punkcake.rocks/products/sticky-toffee-pecan-and-custard-cake?pr_prod_strat=jac&pr_rec_id=8c5b43646&pr_rec_pid=4805918818406&pr_ref_pid=4590468104294&pr_seq=uniform')