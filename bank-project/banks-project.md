# World's Largest Banks ETL Pipeline

A comprehensive ETL (Extract, Transform, Load) pipeline that processes data about the world's largest banks by market capitalization. This project demonstrates data engineering skills including web scraping, data transformation, and database operations.

## 🎯 Project Overview

This project extracts bank data from Wikipedia, transforms it by adding multiple currency columns using live exchange rates, and loads the processed data into both CSV files and SQL databases. The system is designed to be executed quarterly for financial reporting.

## 📋 Features

- **Data Extraction**: Web scraping from Wikipedia using BeautifulSoup
- **Data Transformation**: Currency conversion using real-time exchange rates
- **Data Loading**: Dual output to CSV files and SQLite database
- **Query System**: Pre-built queries for different regional offices
- **Comprehensive Logging**: Detailed progress tracking and error handling
- **Error Resilience**: Fallback mechanisms for robust operation

## 🛠 Technologies Used

- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **BeautifulSoup4** - Web scraping
- **SQLite3** - Database operations
- **Requests** - HTTP requests
- **NumPy** - Numerical operations

## 📊 Data Flow

```
Wikipedia (Banks Data) → Extract → Transform (Add Currencies) → Load (CSV + Database) → Query
                            ↓
                    Exchange Rate CSV
```

## 🏗 Project Structure

```
banks-etl-pipeline/
│
├── banks_project.py          # Main ETL script
├── README.md                 # Project documentation
├── requirements.txt          # Dependencies
├── Largest_banks_data.csv    # Output CSV file
├── Banks.db                  # SQLite database
└── code_log.txt             # Execution logs
```

## 🚀 Quick Start

### Prerequisites

```bash
pip install pandas beautifulsoup4 requests numpy
```

### Running the Project

1. Clone the repository:
```bash
git clone [your-repo-url]
cd banks-etl-pipeline
```

2. Run the ETL pipeline:
```bash
python banks_project.py
```

### Expected Output

The script will:
- Extract data from Wikipedia
- Transform it with GBP, EUR, and INR conversions
- Save to `Largest_banks_data.csv`
- Load into `Banks.db` SQLite database
- Execute sample queries for different offices
- Generate detailed logs in `code_log.txt`

## 📈 Sample Data Output

| Name | MC_USD_Billion | MC_GBP_Billion | MC_EUR_Billion | MC_INR_Billion |
|------|----------------|----------------|----------------|----------------|
| JPMorgan Chase | 432.92 | 346.34 | 402.61 | 35,910.84 |
| Bank of America | 231.52 | 185.22 | 215.31 | 19,207.54 |

## 🔍 Database Queries

The system includes pre-built queries for regional offices:

- **London Office**: `Name` and `MC_GBP_Billion`
- **Berlin Office**: `Name` and `MC_EUR_Billion`  
- **New Delhi Office**: `Name` and `MC_INR_Billion`

## 📝 Logging

Comprehensive logging tracks:
- Pipeline initialization and completion
- Data extraction progress
- Transformation steps
- Loading operations
- Query executions
- Error handling

## 🎓 Learning Objectives

This project demonstrates:
- **Web Scraping** techniques with BeautifulSoup
- **Data Transformation** using Pandas
- **Database Operations** with SQLite
- **Data Visualization** with Altair and interactive charts
- **Statistical Analysis** and market insights
- **Error Handling** and robust programming practices
- **ETL Pipeline** design and implementation
- **Logging** and monitoring systems

## 🛡 Error Handling

The script includes robust error handling:
- Fallback to sample data if web scraping fails
- Approximate exchange rates if CSV loading fails
- Comprehensive logging for all operations
- Graceful error recovery mechanisms

## 🔄 Automation Ready

This pipeline is designed for quarterly execution:
- Automated data refresh
- Consistent output format
- Reliable error handling
- Comprehensive logging for monitoring

## 📜 License

This project is part of IBM Data Engineering training and is intended for educational purposes.

---

*This project was developed as part of IBM Data Engineering certification training.*