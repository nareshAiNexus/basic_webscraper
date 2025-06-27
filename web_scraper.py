import requests
from bs4 import BeautifulSoup


def scrape(url):
    # for i in range(len(urls)):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup)
    with open("soup1.html", "w") as f:
        f.write(str(soup))
        # selected_content = tag_extractions(soup)

    # title = soup.select_one('h1').text
    # text = soup.select_one('p').text
    # link = soup.select_one('a').get('href')

def tag_extractions(soup):
    basic_tags = set('h1', 'h2', 'h3', 'h3', 'h4', 'h5', 'h6',
                  'p', 'a', 'span', 'strong', 'b', 'img')
    # just the basic text and images we need to extract from the url 
    # still our main objective is to extract the content.

    content = ""
    for tag in soup:
        if tag in basic_tags:
            pass
        pass

if __name__ == "__main__":
    url = "https://www.example.com"
    scrape(url)

