from bs4 import BeautifulSoup
import re
from IPython.display import HTML
import requests
from pprint import pprint

def scraper(url):
    # Remove duplicate links from file
    def remove_duplicates():
        lines = open('scraped_links.txt', 'r')
        lines_set = set(lines.readlines())
        out  = open('scraped_links.txt', 'w')
        for line in lines_set:
            out.write(line)
        lines.close()
        out.close()

    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'html.parser')

    # Write HTML to file
    with open('scraped_data.txt', 'w') as file:
        file.write(soup.prettify())

    # Create a .txt file with all the links of the scraped page
    # For a tags with href add , attrs={'href': re.compile('^https')} to find_all()
    with open('scraped_links.txt', 'w+') as file:
        for link in soup.find_all('a'):
            soup_link = str(link.get('href'))

            # remove any id links
            if '#' not in soup_link:
                # convert relative links to base url + link
                if 'punkcake.rocks' and 'https' not in soup_link:
                    soup_link = 'punkcake.rocks' + soup_link
                    file.write(soup_link + ', \n')
                else:
                    file.write(soup_link + ', \n')
           
    # Create a file with the allergens
    try:
        #Get title from product page
        title_html = soup.body.findAll('h1', {'class': 'h2 product-single__title'})
        title = re.findall('">[a-zA-Z]+.+.?', str(title_html))[0].split('">')[1].capitalize()
        
        #Get allergen info from description and filter the allergens
        allergen_html = soup.body.findAll('div', {'class': 'rte'})
        allergens = re.findall('Allergens:.[a-zA-Z]+.+.?', str(allergen_html))[0].split("Allergens:")
        allergens = allergens[1].split("</span>")[0].capitalize()

        # Create a file with the allergens
        file = open('allergen_data.txt', 'w')
        file.write(title + ' - ' + allergens)
        file.flush()
        file.close()
    except:
        pass

    remove_duplicates()

scraper('https://punkcake.rocks')
