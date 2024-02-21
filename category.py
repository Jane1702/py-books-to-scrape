import requests
from bs4 import BeautifulSoup
import csv 

def category(base_url):
    data = []
    response_page = requests.get(base_url)
    if response_page.status_code == 200:
        soup_page = BeautifulSoup(response_page.content, 'html.parser')
        page_tag_class = soup_page.find('ul', class_='pager')
        if page_tag_class is not None :
            page_tag = page_tag_class.find('li', class_='current')
            page = page_tag.text.strip()
            print(page[-1])
            num_page = int(page[-1])
            for i in range(1,num_page + 1) :
                url = f"{base_url}/page-{i}.html"
                response = requests.get(url)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    a_tag = soup.findAll('a')
                    for ele in a_tag : 
                        title = ele.get('title')
                        if title is not None : 
                            href = ele.get("href")
                            #print(href)
                            parts_href = href.split("/")
                            extracted_path_href = "/".join(parts_href[3:])
                            #print(extracted_path_href)
                            url2 = "https://books.toscrape.com/catalogue/" + extracted_path_href
                            response2 = requests.get(url2)
                            soup2 = BeautifulSoup(response2.content, 'html.parser')
                            img_tags = soup2.findAll('img')
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
                            print(title)
        else:
            a_tag = soup_page.findAll('a')
            for ele in a_tag : 
                title = ele.get('title')
                if title is not None : 
                    href = ele.get("href")
                    #print(href)
                    parts_href = href.split("/")
                    extracted_path_href = "/".join(parts_href[3:])
                    #print(extracted_path_href)
                    url2 = "https://books.toscrape.com/catalogue/" + extracted_path_href
                    response2 = requests.get(url2)
                    soup2 = BeautifulSoup(response2.content, 'html.parser')
                    img_tags = soup2.findAll('img')
                    img_url = ""
                    for img in img_tags:
                        src = img.get('src')
                        alt = img.get('alt')
                        if alt == title :
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
                    upc = article_tag.find('th', string='UPC').find_next('td').text.strip()
                    price_including_tax = article_tag.find('th', string='Price (incl. tax)').find_next('td').text.strip()
                    price_excluding_tax = article_tag.find('th', string='Price (excl. tax)').find_next('td').text.strip()
                    number_available = article_tag.find('th', string='Availability').find_next('td').text.strip()
                    category = soup2.find('ul', class_='breadcrumb').findAll('li')[2].text.strip()
                    #print(category)
                    data.append({'product_page_url': url2,'universal_product_code [upc]':upc, 'title': title , 'price_including_tax' : price_including_tax,'price_excluding_tax' :price_excluding_tax , 'number_available' : number_available , 'product_description' : description,'category':category,'review_rating' :review_rating,'image_url':img_url})
                    print(title)
            

    return data

       

def save_to_csv(data):
    with open('books.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['product_page_url', 'universal_product_code [upc]','title','price_including_tax','price_excluding_tax','number_available','product_description','category','review_rating','image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow(row)


data = category("https://books.toscrape.com/catalogue/category/books/mystery_3")
#save_to_csv(data)
