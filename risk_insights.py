import mysql.connector

# Connect to database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="business_analytics"
)

cursor = conn.cursor()

print("\n--- HIGH RISK TRANSACTIONS REPORT ---\n")

query = """
SELECT c.customer_name,
       c.region,
       c.risk_score,
       p.payment_status,
       p.delay_days
FROM customers c
JOIN sales s ON c.customer_id = s.customer_id
JOIN payments p ON s.sale_id = p.sale_id
WHERE c.risk_score > 7 OR p.delay_days > 10;
"""

cursor.execute(query)
results = cursor.fetchall()

if not results:
    print("No high-risk customers found.")
else:
    for row in results:
        customer, region, risk, status, delay = row
        print(f"Customer: {customer}")
        print(f"Region: {region}")
        print(f"Risk Score: {risk}")
        print(f"Payment Status: {status}")
        print(f"Delay Days: {delay}")
        print("-" * 40)

conn.close()
