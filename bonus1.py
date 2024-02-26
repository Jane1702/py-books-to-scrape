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
        avg_price_in_category = df['price_including_tax'].replace('£', '').astype(float).mean()
        category = filename.split(".csv")[0]
        categories.append(category)
        num_books.append(num_books_in_category)
        avg_prices.append(avg_price_in_category)
    data = {
    'category': categories,
    'num_books_in_category': num_books,
    'avg_price_in_category': avg_prices
    }
    result_df = pd.DataFrame(data)
    result_csv_file = "aggregated_data.csv"
    result_df.to_csv(result_csv_file, index=False)
    print("Aggregated data saved successfully.")

create_csv_category()

def circle_diagram():
    df = pd.read_csv('aggregated_data.csv')
    top_categories = df.nlargest(20, 'num_books_in_category')
    plt.figure(figsize=(10, 10))
    plt.pie(top_categories['num_books_in_category'], labels=top_categories['category'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.title('Top 20 Book Categories by Percentage')
    plt.savefig('circle_diagram_bonus1.png')
    plt.show()

