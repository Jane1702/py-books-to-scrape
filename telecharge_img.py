import random
import string
import os
import requests
from bs4 import BeautifulSoup

def download_image(image_url,folder,filename):
    if not os.path.exists(folder):
        os.makedirs(folder)
    full_path = os.path.join(folder, filename)
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(full_path, 'wb') as file:
            file.write(response.content)
        print(f"Image downloaded and saved as: {full_path}")
    else:
        print(f"Failed to download image from URL: {image_url}")

def scrawl_img(base_url):
    for i in range(1,51) :
        url = f"{base_url}/catalogue/page-{i}.html"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            a_tag = soup.findAll('a')
            for ele in a_tag : 
                title = ele.get('title')
                if title is not None : 
                    href = ele.get("href")
                    #print(title)
                    #print(href)
                    url2 = f"{base_url}/catalogue/{href}"
                    response2 = requests.get(url2)
                    soup2 = BeautifulSoup(response2.content, 'html.parser')
                    img_tags = soup2.findAll('img')
                    #, class_='item active'
                    img_url = ""
                    for img in img_tags:
                        src = img.get('src')
                        alt = img.get('alt')
                        if alt == title :
                            parts = src.split("/")
                            extracted_path = "/".join(parts[2:])
                            img_url = base_url + "/" +extracted_path
                            #print(img_url)
                            break
                    category = soup2.find('ul', class_='breadcrumb').findAll('li')[2].text.strip()
                    #print(category)
                    random_string = ''.join(random.choices(string.ascii_letters, k=8))
                    filename = category + "_" + random_string + ".png"
                    download_image(img_url , "images",filename)


scrawl_img("https://books.toscrape.com")