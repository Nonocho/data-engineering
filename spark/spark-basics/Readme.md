# Employee Data Analysis with Apache Spark

A PySpark project demonstrating basic data analysis operations on employee data. Completed as part of the IBM Data Engineering Professional Certificate.

## 🎯 What This Project Covers

- Loading CSV data into Spark DataFrames
- Defining schemas and data types
- SQL queries with Spark SQL
- Data transformations (filtering, sorting, aggregations)
- GroupBy operations and joins

## 🛠️ Technologies

- Apache Spark 3.x
- PySpark
- Python 3.7+
- Jupyter Notebook

## 📁 Project Structure

```
spark-employee-data-analysis/
├── Employee_Analysis.ipynb    # Main notebook with all solutions
├── employees.csv              # Sample dataset (auto-downloaded)
├── requirements.txt           # Python dependencies
└── README.md
```

## 🚀 Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/Nonocho/spark-employee-data-analysis.git
cd spark-employee-data-analysis
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the notebook:**
```bash
jupyter notebook Employee_Analysis.ipynb
```

The dataset will be automatically downloaded when you run the notebook.

## 📊 Analysis Tasks

This project includes 15 hands-on tasks:

1. Load CSV data into DataFrame
2. Define explicit schema
3. Display DataFrame structure
4. Create temporary SQL view
5. Filter data with SQL queries
6. Calculate average salary by department
7. Filter specific departments
8. Add calculated columns (salary bonus)
9. Find maximum values by groups
10. Perform self-joins
11. Calculate aggregations
12. Group and sum data
13. Multi-level sorting
14. Count records by category
15. String pattern matching

## 💡 Key Learning Points

- **DataFrame API**: Working with distributed data structures
- **Spark SQL**: Querying data using SQL syntax
- **Transformations**: map, filter, groupBy operations
- **Aggregations**: sum, avg, max, count functions
- **Joins**: Combining datasets

## 📝 Sample Results

**Average Salary by Department:**
```
+------------+-----------+
|  Department|Avg_Salary |
+------------+-----------+
|     Finance|   80000.00|
|          IT|   75000.00|
|          HR|   65000.00|
+------------+-----------+
```

## 🔧 Requirements

See `requirements.txt` for full list. Main dependencies:
- pyspark==3.5.0
- jupyter
- pandas (for comparison)

## 👤 Author

**Arnaud Demes**  
AI Engineering Leader @ Amundi

- LinkedIn: [arnaud-demes](https://www.linkedin.com/in/arnaud-demes-19101990a)
- GitHub: [@Nonocho](https://github.com/Nonocho)

## 📜 License

This project is open source and available under the MIT License.
