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
    soup = scrape(url)
    path = path + filename

    md_lines = []

    for tag in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'p', 'b', 'i', 'a', 'img']):
        if tag.name in ['h1', 'h2', 'h3', 'h4', 'h5']:
            md_lines.append(f"{'#' * int(tag.name[1])} {tag.get_text(strip=True)}\n")
        
        elif tag.name == 'p':
            text = tag.get_text(strip=True)
            if text:
                md_lines.append(f"{text}\n")

        elif tag.name == 'b':
            text = tag.get_text(strip=True)
            if text:
                md_lines.append(f"**{text}**\n")

        elif tag.name == 'i':
            text = tag.get_text(strip=True)
            if text:
                md_lines.append(f"*{text}*\n")

        elif tag.name == 'a':
            href = tag.get('href', '')
            text = tag.get_text(strip=True)
            if href and text:
                md_lines.append(f"[{text}]({href})\n")

        elif tag.name == 'img':
            src = tag.get('src', '')
            alt = tag.get('alt', 'Image')
            if src:
                md_lines.append(f"![{alt}]({src})\n")

    # Write the Markdown lines to a file
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))


if __name__ == "__main__":
    url = input("Enter the URL : ")
    path = input("Enter the path : ")
    file_name = input("Enter the filename : ")
    try:
        soup2HTML(url, path, file_name)
    except Exception as e:
        print("ERROR OCCURED")
        

