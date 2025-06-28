import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk 
from tkinter import filedialog, messagebox, ttk


def scrape(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code == 403:
        raise Exception("Access denied (403). Site may be blocking bots.")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    return soup

def soup2HTML(url, path):
    soup = scrape(url)
    # create the file if not exist and write the scrapped code or text
    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))


def soup2MD(url, path):
    soup = scrape(url)

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

def run_scraper():
    url = url_entry.get().strip()
    filename = filename_entry.get().strip()
    filetype = filetype_var.get()

    if not url or not filename:
        messagebox.showerror("Error", "Please enter both URL and filename.")
        return

    filepath = filedialog.asksaveasfilename(
        defaultextension=filetype,
        initialfile=filename,
        filetypes=[("HTML files", "*.html"), ("Markdown files", "*.md")]
    )

    if not filepath:
        messagebox.showwarning("Cancelled", "No file was selected.")
        return

    try:
        if filetype == ".html":
            soup2HTML(url, filepath)
        else:
            soup2MD(url, filepath)
        messagebox.showinfo("Success", f"File saved successfully:\n{filepath}")
    except FileNotFoundError:
        messagebox.showerror("Path Error", f"Invalid path:\n{filepath}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{str(e)}")


root = tk.Tk()
root.title("Web Scraper UI")
root.geometry("400x250")

tk.Label(root, text="Enter URL:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack()

tk.Label(root, text="Enter Filename (without extension):").pack(pady=5)
filename_entry = tk.Entry(root, width=50)
filename_entry.pack()

tk.Label(root, text="Select File Type:").pack(pady=5)
filetype_var = tk.StringVar(value=".html")
filetype_menu = ttk.Combobox(root, textvariable=filetype_var, values=[".html", ".md"], state="readonly")
filetype_menu.pack()

tk.Button(root, text="Scrape and Save", command=run_scraper).pack(pady=20)

root.mainloop()
