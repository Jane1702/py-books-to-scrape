import requests
from bs4 import BeautifulSoup
import csv
from category import *

def scrape_all_books(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        side_category = soup.find("div" , class_ = "side_categories")
        category2 = side_category.findAll("a")
        for ele in category2[1:] :
            category_href = ele.get("href")
            #print(category_href)
            parts = category_href.split("/")
            extracted_path = "/".join(parts[:-1])
            #print(extracted_path)
            name_category = parts[-2].split('_')[0]
            #print(name_category)
            url = "https://books.toscrape.com/" + extracted_path
            data = category(url)
            name_csv = name_category + ".csv"
            with open(name_csv, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = ['product_page_url', 'universal_product_code [upc]','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()

                for row in data:
                    writer.writerow(row)
            print("created" + name_csv)
            

"""
def scrape_book_info(base_url):
    data = []
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
                            #print(alt)
                            #print(src)
                            parts = src.split("/")
                            extracted_path = "/".join(parts[2:])
                            #print(extracted_path)
                            img_url = base_url + "/" +extracted_path
                            #print(img_url)
                            break
                        
                    p_tags = soup2.find('p', class_=lambda x: x and x.startswith('star-rating'))
                    #print(p_tags['class'][1])
                    review_rating = p_tags['class'][1]
                    article_tag = soup2.find('article', class_='product_page')
                    description_tag = article_tag.find('p', class_=lambda x: x is None)
                    if description_tag is not None :
                        description= description_tag.text.strip()
                    #print(description)
                    upc = article_tag.find('th', string='UPC').find_next('td').text.strip()
                    #print(upc)
                    price_including_tax = article_tag.find('th', string='Price (incl. tax)').find_next('td').text.strip()
                    price_excluding_tax = article_tag.find('th', string='Price (excl. tax)').find_next('td').text.strip()
                    #print(price_including_tax)
                    number_available = article_tag.find('th', string='Availability').find_next('td').text.strip()
                    category = soup2.find('ul', class_='breadcrumb').findAll('li')[2].text.strip()
                    #print(category)
                    data.append({'product_page_url': url2,'universal_product_code [upc]':upc, 'title': title , 'price_including_tax' : price_including_tax,'price_excluding_tax' :price_excluding_tax , 'number_available' : number_available , 'product_description' : description,'category':category,'review_rating' :review_rating,'image_url':img_url})
                    #print(title)
    return data

def save_to_csv(data):
    with open('all_books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code [upc]','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


data = scrape_book_info("https://books.toscrape.com")
save_to_csv(data)
"""

scrape_all_books("https://books.toscrape.com")