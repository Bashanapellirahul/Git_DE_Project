import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Define the number of rows
num_rows = 5000

# Generate sample sales data
data = {
    'transaction_id': [fake.uuid4() for _ in range(num_rows)],
    'product_id': np.random.randint(1, 101, size=num_rows),
    'quantity': np.random.randint(1, 20, size=num_rows),
    'amount_price': np.round(np.random.uniform(5, 100, size=num_rows), 2),
    'sales_date': [fake.date_this_year() for _ in range(num_rows)]
}

sales_df = pd.DataFrame(data)

# Save to CSV
sales_df.to_csv('sales_data.csv', index=False)

print("Sales data generated and saved to 'sales_data.csv'")
