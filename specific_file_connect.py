import pandas as pd
import mysql.connector

# File path
file_path = "D:/Excel_csv/Blinkit/blinkit_order_items.csv"  # or .xlsx

# Read file without modifying blanks or nulls
if file_path.endswith(".csv"):
    df = pd.read_csv(file_path)
elif file_path.endswith(".xlsx"):
    df = pd.read_excel(file_path)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Vyomesh9612',
    database='blinkit_database'
)
cursor = conn.cursor()

# Table name
table_name = "blinkit_order_items"

# Create table: all columns as TEXT (you can customize types later)
columns = ", ".join([f"`{col}` TEXT" for col in df.columns])
create_table_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({columns});"
cursor.execute(create_table_sql)

# Insert rows as-is (NaN will go as NULL in MySQL)
for _, row in df.iterrows():
    values = [None if pd.isna(val) else val for val in row]
    placeholders = ", ".join(["%s"] * len(row))
    insert_sql = f"INSERT INTO `{table_name}` VALUES ({placeholders})"
    cursor.execute(insert_sql, values)

# Commit and close
conn.commit()
cursor.close()
conn.close()

print("✅ Data imported with original blank/null values (not replaced).")
