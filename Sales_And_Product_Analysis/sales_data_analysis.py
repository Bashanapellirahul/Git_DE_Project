import pandas as pd

from sqlalchemy import create_engine, text
# Load sales data
sales_data = pd.read_csv('sales_data.csv')

# Load product data
product_data = pd.read_csv('product_data.csv')

##########################################################

# Example transformation: Merge sales data with product data
data = pd.merge(sales_data, product_data, on='product_id')

# Handle missing values
data.fillna({'product_description': 'Unknown'}, inplace=True)

# Strip any leading or trailing spaces from column names
sales_data.columns = sales_data.columns.str.strip()
product_data.columns = product_data.columns.str.strip()

#print(sales_data.dtypes)  # Check data types

# Convert columns to numeric if necessary
if 'amount_price' in sales_data.columns and 'quantity' in sales_data.columns:
    sales_data['amount_price'] = pd.to_numeric(sales_data['amount_price'], errors='coerce')
    sales_data['quantity'] = pd.to_numeric(sales_data['quantity'], errors='coerce')
    sales_data['total_sales'] = sales_data['quantity'] * sales_data['amount_price']
    print("\nData with total_sales column:")
    print(sales_data.head())
else:
    print("Column names 'amount_price' or 'quantity' not found in the dataset.")



# Create a database connection
engine = create_engine('mysql+mysqlconnector://rahul:R1302984r@127.0.0.1/sqlcasestudy')
sales_data.to_sql('sales_summary', engine, if_exists='replace', index=False)

with engine.connect() as conn:
    # Execute SQL query
    query = text('''
        SELECT product_id, SUM(total_sales) AS total_sales
        FROM sales_summary
        GROUP BY product_id;
    ''')
    result = conn.execute(query)
    
    # Fetch and display results
    for row in result:
        print(row)

import matplotlib.pyplot as plt

# Example: Plot monthly sales trend
monthly_sales = pd.read_sql_query('''
    SELECT EXTRACT(MONTH FROM sales_date) AS month, SUM(total_sales) AS total_sales
    FROM sales_summary
    GROUP BY EXTRACT(MONTH FROM sales_date)
    ORDER BY month;
''', engine)

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales['month'], monthly_sales['total_sales'], marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(range(1, 13))
plt.grid(True)

file_path = 'Sales_And_Product_Analysis/monthly_sales_trend.png'
plt.savefig(file_path, format='png')  # Save the figure
print(f"Plot saved to {file_path}")