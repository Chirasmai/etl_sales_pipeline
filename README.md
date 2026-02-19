
# ETL Sales Pipeline

This project demonstrates an **end‑to‑end ETL (Extract, Transform, Load) pipeline** for retail sales data.

It extracts raw sales data from CSV, transforms it using Python (pandas), loads it into a MySQL database, and includes a sample visualization to show results.

---

## 🛠️ Tools & Skills Used

- **Python** (pandas, matplotlib, seaborn)  
- **MySQL** for database  
- **ETL Concepts** (Extract → Transform → Load)  
- **Data Cleaning & Transformation**  
- **Data Visualization**

---

## 📁 Project Structure
```

etl_sales_pipeline/
│
├─ scripts/                 # ETL scripts
│   ├─ extract.py
│   ├─ transform.py
│   └─ load.py
│
├─ rawdata/                 # Data files
│   ├─ retail_sales_dataset.csv
│   └─ transformed_sales.csv
│
├─ images/                  # Visual assets
│   └─ sales_by_category.png
│
└─ README.md                # Project documentation

```

## 🚀 Project Workflow

1. **Extract**  
   Read raw CSV file using Python (pandas).

2. **Transform**  
   Clean and manipulate the dataset — formats, calculated fields, missing values.

3. **Load**  
   Load the cleaned data into a MySQL database table.

4. **Visualize**  
   Generate charts to show insights from transformed data.

---

## 📊 Example Output

Total Sales by Product Category:

![Total Sales by Product Category](https://github.com/Chirasmai/etl_sales_pipeline/blob/main/etl%20image.png)

---



