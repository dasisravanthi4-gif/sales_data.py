import os
print("Current working directory:", os.getcwd())
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Sales_data.csv")
print(df.head())
sales_summary = df.groupby('Product')['Sales'].sum()
print(sales_summary)
sales_summary.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()