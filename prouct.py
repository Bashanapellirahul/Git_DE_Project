import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Define the number of products
num_products = 1000

# Generate sample product data
data = {
    'product_id': range(1, num_products + 1),
    'product_name': [fake.word() for _ in range(num_products)],
    'product_description': [fake.sentence() for _ in range(num_products)],
    'amount_price': np.round(np.random.uniform(5, 100, size=num_products), 2)
}

product_df = pd.DataFrame(data)

# Save to CSV
product_df.to_csv('product_data.csv', index=False)

print("Product data generated and saved to 'product_data.csv'")
