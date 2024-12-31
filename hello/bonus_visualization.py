import sqlite3
import matplotlib.pyplot as plt  # Import matplotlib.pyplot

# Connect to the database
conn = sqlite3.connect('data_analysis.db')
cursor = conn.cursor()

# 2. Retrieve Data
query = """
SELECT Product, SUM(Price * Quantity) AS TotalRevenue
FROM Sales
GROUP BY Product
ORDER BY TotalRevenue DESC;
"""
cursor.execute(query)
data = cursor.fetchall()

# Extract products and revenues from the query results
products = [row[0] for row in data]
revenues = [row[1] for row in data]

# Close the cursor and connection
cursor.close()
conn.close()

# Create a bar chart
plt.bar(products, revenues, color="skyblue")
plt.xlabel('Product')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product')
plt.xticks(rotation=60)  # Rotate x-axis labels for better readability
plt.tight_layout()       # Adjust layout to fit x-axis labels
plt.savefig("revenue_chart.png")
plt.show()

