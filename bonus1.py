import pandas as pd
import os
import matplotlib.pyplot as plt

def create_csv_category() :
    folder_path = "all_category"
    categories = []
    num_books = []
    avg_prices = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path)
        num_books_in_category = len(df)
        #price_in_category = df['price_including_tax'].replace('£', '')
        #price_in_category_float = price_in_category.astype(float)
        #avg_price_in_category = price_in_category_float.mean()
        price_in_category_float = df['price_including_tax'].replace('£', '', regex=True).astype(float)  
        avg_price_in_category = price_in_category_float.mean()
        avg_price_with_currency = '£{:.2f}'.format(avg_price_in_category)
        category = filename.split(".csv")[0]
        categories.append(category)
        num_books.append(num_books_in_category)
        avg_prices.append(avg_price_with_currency)
    data = {
    'category': categories,
    'num_books_in_category': num_books,
    'avg_price_in_category': avg_prices
    }
    result_df = pd.DataFrame(data)
    result_csv_file = "books_details_by_category.csv"
    result_df.to_csv(result_csv_file, index=False)
    print("File saved successfully.")

create_csv_category()

def circle_diagram():
    df = pd.read_csv('books_details_by_category.csv')
    top_categories = df.nlargest(20, 'num_books_in_category')
    plt.figure(figsize=(10, 10))
    plt.pie(top_categories['num_books_in_category'], labels=top_categories['category'], autopct='%1.1f%%', startangle=140,textprops={'fontsize': 6})
    plt.rcParams.update({'font.size': 15})
    plt.axis('equal')
    plt.title('Top 20 Book Categories by Percentage')
    plt.savefig('circle_diagram_bonus1.png')
    plt.show()

circle_diagram()