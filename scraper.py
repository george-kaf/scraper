import requests
from bs4 import BeautifulSoup


def scraper(url, base_url):
    # Remove duplicate links from file
    def remove_duplicates():
        lines = open("scraped_links.txt", "r")
        lines_set = set(lines.readlines())
        out = open("scraped_links.txt", "w")
        for line in lines_set:
            out.write(line)
        lines.close()
        out.close()

    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")

    # Write HTML to file
    with open("scraped_data.txt", "w") as file:
        file.write(soup.prettify())

    # Create a .txt file with all the links of the scraped page
    # For a tags with href add , attrs={'href': re.compile('^https')} to find_all()
    with open("scraped_links.txt", "w+") as file:
        for link in soup.find_all("a"):
            soup_link = str(link.get("href"))

            # remove any id links
            if "#" not in soup_link:
                # convert relative links to base url + link
                if base_url and "http" not in soup_link:
                    soup_link = str(base_url) + soup_link
                    file.write(soup_link + ", \n")
                else:
                    file.write(soup_link + ", \n")

    remove_duplicates()
