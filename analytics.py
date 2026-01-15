import mysql.connector
import matplotlib.pyplot as plt

# Database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="business_analytics"
)

cursor = conn.cursor()

# Query: Revenue by Product
query = """
SELECT product_name, SUM(quantity * price)
FROM sales
GROUP BY product_name
"""

cursor.execute(query)
data = cursor.fetchall()

# Process data
products = [row[0] for row in data]
revenue = [row[1] for row in data]

# Plot
plt.bar(products, revenue)
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.title("Revenue by Product")
plt.show()

# Close connection
conn.close()
