import pandas as pd
import matplotlib.pyplot as plt

def histogram():
    df = pd.read_csv('your_data.csv')
    avg_price_in_category = df['price_including_tax']
    plt.figure(figsize=(10, 6))
    plt.bar(avg_price_in_category.index, avg_price_in_category.values)
    plt.xlabel('Category')
    plt.ylabel('Average Price')
    plt.title('Average Book Prices by Category')
    plt.xticks(rotation=45, ha='right')  # Rotate category labels for better readability
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.show()  