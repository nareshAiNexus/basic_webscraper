import requests
from bs4 import BeautifulSoup


def scrape(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup

def soup2HTML(url, path, filename):
    soup = scrape(url)
    path = path + filename
    # create the file if not exist and write the scrapped code or text
    with open(path, "w") as f:
        f.write(str(soup))


def soup2MD(url, path, filename):
    # just the basic text and images we need to extract from the url 
    # still our main objective is to extract the content.
    soup = scrape(url)
    
    MD_map = {'h1':"#", 'h2':'##', 'h3':'###', 'h4':'####', 'h5':'#####',
              'a': '[', 'p':'', 'i':'*', 'b':'**'}

    

if __name__ == "__main__":
    url = input("Enter the URL : ")
    path = input("Enter the path : ")
    file_name = input("Enter the filename : ")
    try:
        soup2HTML(url, path, file_name)
    except Exception as e:
        print("ERROR OCCURED")
        

