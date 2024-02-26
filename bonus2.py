import pandas as pd
import matplotlib.pyplot as plt

def histogram():
    df = pd.read_csv('books_details_by_category.csv')
    df.set_index('category', inplace=True)
    avg_price_in_category = df['avg_price_in_category']
    avg_price_in_category_sorted = avg_price_in_category.sort_values()
    plt.figure(figsize=(10, 6))
    plt.bar(avg_price_in_category_sorted.index, avg_price_in_category_sorted.values)
    plt.xlabel('Category')
    plt.ylabel('Average Price')
    plt.title('Average Book Prices by Category')
    plt.yticks(fontsize = 6)
    plt.xticks(rotation=45, ha='right', fontsize=8) 
    plt.tight_layout() 
    plt.savefig('histogramme_bonus2.png') 
    plt.show()  

histogram()