import mysql.connector
import matplotlib.pyplot as plt

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="business_analytics"
)
cursor = conn.cursor()

# ---------------- QUERY 1: Revenue by Product ----------------
cursor.execute("""
SELECT pr.product_name, SUM(s.quantity * s.price)
FROM sales s
JOIN products pr ON s.product_id = pr.product_id
GROUP BY pr.product_name
""")
revenue_data = cursor.fetchall()

products = [row[0] for row in revenue_data]
revenue = [row[1] for row in revenue_data]

# ---------------- QUERY 2: High-Risk Customers ----------------
cursor.execute("""
SELECT c.customer_name, c.risk_score
FROM customers c
WHERE c.risk_score > 7
""")
risk_data = cursor.fetchall()

risk_customers = [row[0] for row in risk_data]
risk_scores = [row[1] for row in risk_data]

# ---------------- QUERY 3: Payment Delay ----------------
cursor.execute("""
SELECT c.customer_name, p.delay_days
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
JOIN payments p ON s.sale_id = p.sale_id
WHERE p.delay_days > 0
""")
delay_data = cursor.fetchall()

delay_customers = [row[0] for row in delay_data]
delay_days = [row[1] for row in delay_data]

conn.close()

# ---------------- DASHBOARD LAYOUT ----------------
plt.figure(figsize=(14, 8))

# Chart 1: Revenue by Product
plt.subplot(2, 2, 1)
plt.bar(products, revenue)
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# Chart 2: Risk Score by Customer
plt.subplot(2, 2, 2)
plt.bar(risk_customers, risk_scores)
plt.title("High-Risk Customers")
plt.xlabel("Customer")
plt.ylabel("Risk Score")

# Chart 3: Payment Delay Analysis
plt.subplot(2, 2, 3)
plt.bar(delay_customers, delay_days)
plt.title("Payment Delay (Days)")
plt.xlabel("Customer")
plt.ylabel("Delay Days")

plt.suptitle("Enterprise Sales Analytics & Risk Dashboard", fontsize=16)
plt.tight_layout()
plt.show()
