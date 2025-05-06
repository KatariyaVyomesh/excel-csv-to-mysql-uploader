# 📂 Excel & CSV to MySQL Uploader

This Python script automates the process of reading `.csv` and `.xlsx` files from a folder, creating corresponding MySQL tables, and inserting the data into those tables. It's designed to make bulk data import into a MySQL database easy and efficient.

---

## 🚀 Features

- Automatically detects and creates MySQL tables based on file structure
- Supports both `.csv` and `.xlsx` formats
- Handles empty files gracefully
- Converts column names for SQL compatibility
- Cleans data (e.g., converts empty strings to NULL)
- Commits all inserts efficiently

---

## 🛠️ Requirements

- Python 3.6+
- MySQL Server
- Python Libraries:
  - `pandas`
  - `mysql-connector-python`
  - `openpyxl` (for `.xlsx` support)

Install requirements using:

```bash
pip install pandas mysql-connector-python openpyxl
```

---

## ⚙️ Setup

1. Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/excel-csv-to-mysql-uploader.git
cd excel-csv-to-mysql-uploader
```

2. Update the script:

Edit the following section in the script with your details:
```python
conn = mysql.connector.connect(
    host='localhost',
    user='ENTER YOUR USERNAME',
    password='YOUR MYSQL PASSWORD',
    database='ENTER YOUR DATABASE NAME'
)

folder_path = "ENTER YOUR FOLDER PATH"
```

3. Place your `.csv` or `.xlsx` files into the folder specified in `folder_path`.

---

## 🧠 How It Works

1. Loops through each file in the given folder
2. Creates a MySQL table based on the file's columns
3. Inserts cleaned data row by row
4. Handles missing/empty values appropriately
5. Commits changes and closes the connection at the end

---

## 📁 Example File Names

If your folder contains files like:
```
SalesData.xlsx
Product-List.csv
```

The script will create tables named:
```
salesdata
product_list
```

---

## 🧹 Output

- ✅ Creates and populates tables in MySQL
- ⚠️ Skips empty files
- ❌ Prints error for corrupt or invalid files

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have a suggestion for a feature, feel free to open an issue.

---

## 📜 License

This project is licensed under the MIT License.

---

## 📧 Contact

Maintained by **Vyomesh Katariya**  
[GitHub](https://github.com/KatariyaVyomesh) • [LinkedIn](https://www.linkedin.com/in/vyomesh-katariya-b9b86b289)
