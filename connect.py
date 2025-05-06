import os
import pandas as pd
import mysql.connector

# === MySQL Connection ===
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Vyomesh9612',
    database='blinkit_database'
)
cursor = conn.cursor()

# === Folder Path ===
folder_path = r"D:\Excel_csv\Blinkit"

# === Create Table Function ===
def create_table_from_df(df, table_name):
    column_defs = []

    for col in df.columns:
        col_clean = col.replace(" ", "_").replace("-", "_")
        series = df[col]
        dtype = series.dtype

        if pd.api.types.is_integer_dtype(dtype):
            sql_type = "BIGINT" if series.max() > 2147483647 else "INT"

        elif pd.api.types.is_float_dtype(dtype):
            sql_type = "FLOAT"

        elif pd.api.types.is_object_dtype(dtype):
            try:
                series_numeric = pd.to_numeric(series, errors='coerce')
                if pd.notnull(series_numeric).all():
                    # It’s all numbers
                    sql_type = "BIGINT" if series_numeric.max() > 2147483647 else "INT"
                else:
                    sql_type = "VARCHAR(255)"
            except:
                sql_type = "VARCHAR(255)"
        else:
            sql_type = "VARCHAR(255)"

        column_defs.append(f"`{col_clean}` {sql_type}")

    create_sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` ({', '.join(column_defs)});"
    cursor.execute(create_sql)


# === Insert Data Function ===
def insert_data(df, table_name):
    df.columns = [col.replace(" ", "_").replace("-", "_") for col in df.columns]
    cols = ", ".join([f"`{col}`" for col in df.columns])
    placeholders = ", ".join(["%s"] * len(df.columns))

    for row in df.itertuples(index=False, name=None):
        # Convert empty strings to None to handle NULLs in MySQL
        cleaned_row = [None if (pd.isna(val) or val == '') else val for val in row]

        sql = f"INSERT INTO `{table_name}` ({cols}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(cleaned_row))

    conn.commit()
    print(f"✅ Data inserted into `{table_name}`")


# === Main Import Loop ===
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if file.endswith(".csv") or file.endswith(".xlsx"):
        table_name = os.path.splitext(file)[0].lower().replace(" ", "_").replace("-", "_")
        print(f"\n📂 Processing File: {file} → Table: {table_name}")

        try:
            if file.endswith(".csv"):
                df = pd.read_csv(file_path)
            else:  # Excel file
                df = pd.read_excel(file_path)

            if df.empty:
                print(f"⚠️ Skipped {file}: Empty file")
                continue

            create_table_from_df(df, table_name)
            insert_data(df, table_name)

        except Exception as e:
            print(f"❌ Error processing {file}: {e}")

# === Cleanup ===
cursor.close()
conn.close()
print("\n✅ All files processed successfully.")
