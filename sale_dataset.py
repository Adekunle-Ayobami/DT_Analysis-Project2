import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('supermarket_sales.csv')

# Handle missing values
df.fillna({'Rating': df['Rating'].mean()}, inplace=True)  # Impute missing values in 'Rating' with the mean

# Feature Engineering
# Example: Calculate the total sales per branch
df['Total Sales'] = df['Unit price'] * df['Quantity']

# Exploratory Data Analysis (EDA)
# Check for missing values
print("Missing values in each column:")
print(df.isnull().sum())

# Group by product line and calculate total sales
product_sales = df.groupby('Product line').sum()['Total Sales']
product_sales.plot(kind='bar', title='Total Sales by Product Line')
plt.xlabel('Product Line')
plt.ylabel('Total Sales')
plt.show()

# Analyze sales by branch
branch_sales = df.groupby('Branch').sum()['Total Sales']
branch_sales.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Branch')
plt.ylabel('')  # Hide y-label for better readability of the pie chart
plt.show()

# Additional EDA: Analyze the relationship between 'Unit price' and 'Rating'
plt.scatter(df['Unit price'], df['Rating'], alpha=0.5)
plt.title('Unit Price vs. Rating')
plt.xlabel('Unit Price')
plt.ylabel('Rating')
plt.show()

# Additional EDA: Check sales trends over time
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
# Use pd.Grouper to group by month
monthly_sales = df.groupby(pd.Grouper(key='Date', freq='ME')).sum()['Total Sales']
monthly_sales.plot(kind='line', title='Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.show()
