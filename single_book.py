import requests
from bs4 import BeautifulSoup
import csv 

def single_book(url2):
    data = []
    response2 = requests.get(url2)
    soup2 = BeautifulSoup(response2.content, 'html.parser')
    img = soup2.find('img')
    src = img.get('src')
    title = img.get('alt')
    parts = src.split("/")
    extracted_path = "/".join(parts[2:])
    #print(extracted_path)
    img_url = "https://books.toscrape.com/" +extracted_path
    #print(img_url)
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
    return data

def save_to_csv(data):
    with open('single_book.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code [upc]','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


#data = single_book("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
data = single_book("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html")
save_to_csv(data)